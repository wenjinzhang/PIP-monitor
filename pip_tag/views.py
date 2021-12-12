from django.shortcuts import render
from django.http import JsonResponse
import json
import ast
from .models import Data
import time
# Create your views here.
last_time = time.time()

def ajax_submit(request):
    global last_time
    context = {}
    if request.method == 'POST':
        sensor_data = request.body.decode()
        data_dic = ast.literal_eval(sensor_data)
        data = Data(temp=data_dic['temp'],
                    light=data_dic['light'],
                    humidity=data_dic['humidity'])
        now = time.time()
        if last_time - now >= 60:
            print(data.temp)
            data.save()
            last_time=now
        else:
            pass
        return render(request,'index.html')

    return render(request, 'index.html')

def index(request):
    return render(request, 'app/index.html')


def history(request):
    data = Data.objects.all()
    date_time = data[0].time.strftime("%m/%d/%Y-%H")

    data = [(m.time, m.temp, m.light, m.humidity) for m in data]

    print(date_time)
    arrays = {
        "times":[ d[0].strftime("%M:%S") for d in data],
        "temp":[ d[1] for d in data],
        "light" : [ d[2] for d in data],
        "humidity" :[ d[3] for d in data],
        "latest": date_time,
    }

    return JsonResponse(arrays)


# def models_to_array(data):
    





