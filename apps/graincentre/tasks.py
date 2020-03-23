import logging
import time

from celery.decorators import periodic_task
# 定时任务
from celery.task.schedules import crontab
from django.conf import settings

from .utils.sendmail import file_mail
from .utils.zipfunc import zip_file

CRITICA=50 	#关键错误/消息
ERROR=40 	#错误
WARNING=30 	#警告消息
INFO=20 	#通知消息
DEBUG=10 	#调试
NOTSET=0 	#无级别

info_logger = logging.getLogger('info')


# 每分钟执行一次
@periodic_task(run_every=crontab(minute=0, hour='*/3'))
def send_db_bak_email():
    try:
        zbfn = zip_file(settings.DB_PATH, settings.DB_BAK_PATH)
        s_time = time.strftime('%Y.%m.%d_%H.%M.%S', time.localtime(time.time()))
        print(zbfn)
        file_mail(zbfn, subject=settings.EMAIL_SUBJECT + "_" + s_time,
                  email_from=settings.EMAIL_HOST_USER, email_to=settings.EMAIL_TO)
        info_logger.log(INFO, msg=zbfn)
    except Exception as e:
        info_logger.log(ERROR, str(e))
    

@periodic_task(run_every=crontab())
def send_db_test_email():
    try:
        print('send_db_test_email')
    except Exception as e:
        info_logger.log(ERROR, str(e))
    

