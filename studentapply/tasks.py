import os

from celery import shared_task
from viewflow.flow.job import flow_job

@shared_task()
@flow_job()
def send_hello_world_request(activation):
    with open(os.devnull, "w") as world:
        world.write(activation.process.text)

@shared_task()
@flow_job()
def send_student_apply_request(activation):
    with open(os.devnull, "w") as world:
        world.write(activation.process.text)