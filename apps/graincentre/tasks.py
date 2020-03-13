from __future__ import absolute_import
from rest_xops.celery import app
import time
@app.task
def period_task(a, b):
    print("开始周期性任务...")
    time.sleep(3)
    print("周期性任务执行完毕:%d!" % (a + b))