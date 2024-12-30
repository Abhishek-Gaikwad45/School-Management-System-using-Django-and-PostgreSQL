# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 11:18:43 2024

@author: rajwa
"""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser, Student, Teacher, Attendance
from .serializers import CustomUserSerializer, StudentSerializer, TeacherSerializer, AttendanceSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]