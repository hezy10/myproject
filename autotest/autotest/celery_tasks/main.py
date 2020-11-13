from celery import Celery


# 为celery的配置使用django的配置文件进行设置

import os
if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'autotest.settings.dev'



# 创建celery的应用
celery_app = Celery('autotest')

# 导入celery配置文件
celery_app.config_from_object('celery_tasks.config')

# 导入任务
celery_app.autodiscover_tasks(['celery_tasks.msm','celery_tasks.email'])