# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 11:20:45 2024

@author: rajwa
"""

from django.contrib import admin
from .models import CustomUser, Student, Teacher, Attendance

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_student', 'is_teacher')
    search_fields = ('username', 'email')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'roll_number', 'class_name')
    search_fields = ('user__username', 'roll_number')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'employee_id', 'subject')
    search_fields = ('user__username', 'employee_id')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'status')
    list_filter = ('date', 'status')
