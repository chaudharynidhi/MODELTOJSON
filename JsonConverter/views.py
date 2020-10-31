from django.shortcuts import render
from .models import Users, ActivityPeriod
from .serializer import UserSerializer, ActPeriodSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def showMultiplemodels(request):
    userobj = Users.objects.all()
    activityobj = ActivityPeriod.objects.all()
    UserSerializerObj =  UserSerializer(userobj, many=True)
    ActPeriodSerializerObj = ActPeriodSerializer(activityobj, many=True)

    user = UserSerializerObj.data
    activity = ActPeriodSerializerObj.data

    resultmodel = []
    
    change = {} 

    for da in user:
        d = {}
        li = []
        for period in activity:
            if period['activity_id'] == da['user_id']:
                d = {'start_time': period['start_time'], 'end_time': period['end_time']}
                li.append(d)
        change = {'id' : da['user_id'], 'real_name': da['real_name'], 
        'tz': da['tz'], 'activity_period': li} 
        resultmodel.append(change)       

    dic = {"ok": True, "users": resultmodel}

    return Response(dic) 

# Create your views here.
