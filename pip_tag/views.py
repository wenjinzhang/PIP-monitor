from django.shortcuts import render
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
        return render(request,'chart.html', context)
    #return render(request, 'ajax1.html')






