from .utils.zipfunc import zip_file
from .utils.sendmail import file_mail
from django.conf import settings
import time
# 定时任务
from celery.task.schedules import crontab
from celery.decorators import periodic_task

# 每分钟执行一次
# http://docs.celeryproject.org/en/master/userguide/periodic-tasks.html
@periodic_task(run_every=crontab())
def send_db_bak_email():
    zbfn = zip_file(settings.DB_PATH, settings.DB_BAK_PATH[0])
    s_time = time.strftime('%Y.%m.%d_%H.%M.%S', time.localtime(time.time()))

    file_mail(zbfn, subject=settings.EMAIL_SUBJECT + "_" + s_time,
              email_from=settings.EMAIL_HOST_USER, email_to=settings.EMAIL_TO)
