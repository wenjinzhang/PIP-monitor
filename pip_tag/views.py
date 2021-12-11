from django.shortcuts import render
from django.http import JsonResponse
import json
import ast
from .models import Data
# Create your views here.

def ajax_submit(request):
    context = {}
    if request.method == 'POST':
        sensor_data = request.body.decode()
        data_dic = ast.literal_eval(sensor_data)
        data = Data(temp=data_dic['temp'],
                    light=data_dic['light'],
                    humidity=data_dic['humidity'])
        print(data.temp)
        data.save()
        context['data'] = data
        return render(request,'index.html', context)
    else:
        # most_recent_data = Data.objects.order_by('-id')[0]
        # context['data'] = most_recent_data
        recent_num_data = Data.objects.all()
        context['data'] = recent_num_data
        return render(request,'index.html', context)
    #return render(request, 'ajax1.html')

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
    





