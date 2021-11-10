import os
from app import app
import redis
from rq import Connection, Worker
from flask.cli import FlaskGroup

config_name = os.getenv('FLASK_CONFIG')
#app = create_app()

cli = FlaskGroup(create_app=app)

#@cli.command("run_worker")
def run_worker():
    redis_url = app.config["REDIS_URL"]
    redis_connection = redis.from_url(redis_url)
    with Connection(redis_connection):
        worker = Worker(app.config["QUEUES"])
        worker.work()

if __name__ == '__main__':
    run_worker()
