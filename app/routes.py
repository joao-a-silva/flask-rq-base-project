# -*- coding: utf-8 -*-
import os
import logging
from datetime import datetime
# TO-DO rever o import do datetime
import multiprocessing as mp
from re import I
from flask import jsonify
import redis
from rq import Queue, Connection
from app import app 
from app import tasks
import json
import hashlib
import datetime
from app import helpers
import uuid



@app.route('/task_example', methods=["GET"])
def task_example():

  try:
      with Connection(redis.from_url(app.config["REDIS_URL"])):
            queue = Queue(app.config['QUEUES'][0])
            queue.default_timeout = app.config['TIME_OUT']['QUEUE']

            queue.enqueue(tasks.task,
                      result_ttl=app.config['TIME_OUT']['RESULT_TTL'],
                      job_timeout=app.config['TIME_OUT']['TASK']
            )
      return   jsonify({'status':'success'}), 200
  except:
      return jsonify({'status':'error'}), 500

