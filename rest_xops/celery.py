from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

#获取当前文件夹名，即为该Django的项目名
project_name = os.path.split(os.path.abspath('.'))[-1]
project_settings = '%s.settings' % project_name

#设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', project_settings)

#实例化Celery
app = Celery(project_name)

app.config_from_object('django.conf:settings')

#Celery加载所有注册的应用
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
# 以下内容也可以写在settings.py文件中


BROKER_URL = 'redis://localhost:6379/1' # Broker配置，使用Redis作为消息中间件

CELERY_RESULT_BACKEND = 'redis://localhost:6379/1' # Backend设置，使用redis作为后端结果存储

CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_ENABLE_UTC = False

CELERYD_FORCE_EXECV = True # 防止任务死锁

CELERYD_CONCURRENCY = 8 # 并发的worker数量

CELERY_ACKS_LATE = True

CELERYD_MAX_TASKS_PER_CHILD = 100 # 每个worker最多执行的任务数

CELERYD_TASK_TIME_LIMIT = 15 * 60 # 任务超时时间

