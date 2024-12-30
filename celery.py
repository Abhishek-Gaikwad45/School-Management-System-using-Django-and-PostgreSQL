# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 11:20:02 2024

@author: rajwa
"""

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_project.settings')
app = Celery('school_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# tasks.py
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_attendance_report(user_email):
    send_mail(
        'Daily Attendance Report',
        'Here is the attendance report for today.',
        'school@example.com',
        [user_email],
    )