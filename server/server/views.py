from django.shortcuts import render,redirect
from api.models import Result
import datetime

def index(request):
    object_list = Result.objects.order_by('score').reverse()
    result_list = []
    for (i,data) in enumerate(object_list):
        created_at = data.created_at + datetime.timedelta(hours=9)
        date = str(created_at.year) + '年' + str(created_at.month) + '月' + str(created_at.day) + '日 ' + str(created_at.hour) + '時' + str(created_at.minute) + '分'
        result = {'rank': i+1, 'username':data.username, 'score':data.score, 'date':date}
        result_list.append(result)
    return render(request,'index.html', {'result_list': result_list})

