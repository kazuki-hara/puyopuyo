from django.shortcuts import render
import json
from .models import Result
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse

RANK = 10

# Create your views here.
@csrf_exempt
def save(request):
    if request.method=='POST':
        username = request.POST['username']
        score = int(request.POST['score'])
        result_list = Result.objects.order_by('score').reverse()
        flag = 0
        rank = 0
        if len(result_list) < RANK:
            result = Result.objects.create(username=username, score=score)
            flag = 1
        else:
            if score > result_list[RANK-1].score:
                result_list[RANK-1].delete()
                result = Result.objects.create(username=username, score=score)
                
                flag= 1
        if flag == 1:
            id_num = result.id
            result_list = Result.objects.order_by('score').reverse()
            for (i,result) in enumerate(result_list):
                if result.id == id_num:
                    rank = i+1

        res = {"rank": rank}
    else:
        res = {"rank": -1}
    res = json.dumps(res)
    return HttpResponse(res)


def reset(resquest):
    Result.objects.all().delete()
    res = {'message': 'All datas are deleted'}
    res = json.dumps(res)
    return HttpResponse(res)