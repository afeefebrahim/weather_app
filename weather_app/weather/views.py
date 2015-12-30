from django.shortcuts import render
from django.http import HttpResponse
from weather.api import run_query

# Create your views here.

def  index(request):
	#context_dict = {'boldmessage': "I am bold font from the context"}
	return render(request,'weather/index.html')
	
    #return HttpResponse("Hello, world. You're at the polls index.")

def  find(request):
	result_list = []

	if request.method == 'POST':
		query = request.POST['query'].strip()

		if query:
		    result_list = run_query(query) 
	return render(request,'weather/get_weather.html',{'result_list': result_list})




	