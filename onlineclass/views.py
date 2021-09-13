from onlineclass.serializers import AttendanceSerializer, ScheduleSerializer
from django.shortcuts import render
from django.http import Http404, HttpResponse, response
from django.db.models.aggregates import Max

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
  
from users.models import User
from .models import Attendance, Schedule
import datetime, time
from itertools import chain
import pytz

utc=pytz.UTC

class OnlineClassSchedule(APIView):
    """
    List all online classes or create a online class
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        users = Schedule.objects.all()
        serializer = ScheduleSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            if not request.user.user_type:
                serializer.save()
                return Response(serializer.data,
                                status=status.HTTP_201_CREATED)
            else:
                resp = {'message': 'Unauthorized: Student cannot schedule a class.'}
                return Response(resp, status=401)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JoinLog(APIView):
    """
    View for joining and leaving the class
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, schedule_id, format=None):
        if not request.user.user_type:
            Attendancedata = Attendance.objects.filter(classid = schedule_id)
            if Attendancedata.exists():
                serializer = AttendanceSerializer(Attendancedata, many=True)
                return Response(serializer.data)
            else:
                resp = {'message': "No students in the class."}
                return Response(resp)
        else:
            resp = {'message': 'Unauthorized: Student cannot view the log.'}
            return Response(resp, status=401)
                
    def post(self, request, schedule_id, log_status, format=None):
        try: 
            session = Schedule.objects.get(pk = schedule_id)
        except:
            resp = {'message': "Requested online class doesn't exists."}
            return Response(resp)
        ctime = utc.localize(datetime.datetime.now()) 
        stime = session.start_time + datetime.timedelta(hours=5, minutes=30)
        etime = session.end_time + datetime.timedelta(hours=5, minutes=30)
        if ctime >= stime and ctime <= etime or not session.is_completed:
            user = User.objects.get(username = request.user.username)
            schedule = Schedule.objects.get(pk = schedule_id)
            minutes = 0
            
            if not log_status:
                try:
                    lastactive = Attendance.objects.filter(user = user, classid = schedule_id).order_by('pk').last()
                    time_delta = (ctime - (lastactive.time + datetime.timedelta(hours=5, minutes=30)))
                    total_seconds = time_delta.total_seconds()
                    minutes = total_seconds/60
                    minutes += int(lastactive.active_time)
                except:
                    resp = {'message': 'Please Join the class before leaving.'}
                    return Response(resp)
                try:
                    if lastactive.type == log_status:
                        resp = {'message': 'User already left class. Join again to continue the class'}
                        return Response(resp)
                except:
                    pass
                # print(lastactive.time + datetime.timedelta(hours=5, minutes=30))
                # print(ctime)
                
                # print('update time', minutes)
                
                log = Attendance(user = user, type = log_status, time = time.strftime("%H:%M:%S", time.localtime()), classid = schedule,
                    active_time = minutes)
                log.save()

                if schedule.teacher.pk == request.user.pk:
                    schedule.is_completed = True
                    schedule.save()
                    resp = {'message': 'Class completed successfully. Teacher ended the class.'}
                    return Response(resp)
                resp = {'message': 'User left the class.'}
                return Response(resp)
            else:
                lastactive = Attendance.objects.filter(user = user, classid = schedule_id).order_by('pk').last()
                try:
                    if lastactive.type == log_status:
                        resp = {'message': 'User already in class.'}
                        return Response(resp)
                except:
                    pass
                log = Attendance(user = user, type = log_status, time = time.strftime("%H:%M:%S", time.localtime()), classid = schedule)
                log.save()
                resp = {'message': 'Ongoing class by ' + schedule.teacher.username}
                return Response(resp)

            
        elif ctime < stime:
            resp = {'message': 'Class start at ' + stime}
            return Response(resp)
        else:
            resp = {'message': 'Class completed at ' + etime}
            return Response(resp)

class ClassLog(APIView):
    """
    View for attendance statistics
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, schedule_id, format=None):
        if not request.user.user_type:
            Scheduledata = Schedule.objects.get(pk = schedule_id)
            if not Scheduledata.is_completed:
                resp = {'message': 'It is an ongoing class. Please check after the completion of class.'}
                return Response(resp)
            else:
                allStudents = User.objects.filter(grade = Scheduledata.teacher.grade, user_type = True)
                alldict = []
                for x in allStudents:
                    alldict.append({'user':x.id, 'first_name': x.first_name, "ActiveMinutes": 0, "Attendance": "Absent"})
                request_values = Attendance.objects.filter(classid__pk = schedule_id).values('user').annotate(ActiveMinutes=Max('active_time'))
                for dct in request_values:
                    dct['Attendance'] = 'Present'
                for x in request_values:
                    cnt = 0
                    for y in alldict:
                        if x['user'] == y['user']:
                            alldict[0]['user'] = x['user']
                            alldict[0]['ActiveMinutes'] = x['ActiveMinutes']
                            alldict[0]['Attendance'] = x['Attendance']
                        cnt += 1
                classdetails = {'classid': schedule_id, 'teacher':Scheduledata.teacher.first_name, 
                                'grade': Scheduledata.teacher.grade, 'course': Scheduledata.teacher.course, 
                                'start_time':Scheduledata.start_time, 'end_time':Scheduledata.end_time, 
                                'completion_status': Scheduledata.is_completed}
                alldict.insert(0, classdetails)
                return Response(alldict)
        else:
            resp = {'message': 'Unauthorized: Student cannot view the statistics.'}
            return Response(resp, status=401)