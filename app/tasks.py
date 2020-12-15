import os
import hashlib

from io import BytesIO
from urllib.parse import urlparse
from celery.utils.log import get_task_logger
from worker import app


logger = get_task_logger(__name__)


@app.task(bind=True, name='print_some_stuff')
def print_some_stuff(self):
    logger.info('some_stuff')
    print('some_stuff')

    
    

