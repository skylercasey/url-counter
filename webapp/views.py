from django.shortcuts import render,redirect
import operator
from .models import domain,word


def mainview(request):
	data1=request.POST.get('text')
	if data1!="":
		try:
			obj=domain.objects.create(url1=data1)
			return redirect('my_function')	
		except:
			obj=domain.objects.get(url1=data1)
			obj.freq=freq+1
			obj.save()
			context['count']=obj.freq
			return redirect('my_function')
			
	return render(request,'webapp/main.html')

def url_ex(url1):
	data=url1
	punc='''~!@#$%^&*:()_+//?.><,'''
	data=data.replace("/"," ")
	data=data.replace("@"," ")
	data=data.replace("~"," ")
	data=data.replace("`"," ")
	data=data.replace("!"," ")
	data=data.replace("#"," ")
	data=data.replace("$"," ")
	data=data.replace("%"," ")
	data=data.replace("^"," ")
	data=data.replace("&"," ")
	data=data.replace("("," ")
	data=data.replace(")"," ")
	data=data.replace("_"," ")
	data=data.replace("//"," ")
	data=data.replace(":"," ")
	data=data.replace("."," ")
	data=data.replace("+"," ")
	data=data.replace("="," ")
	data=data.replace("?"," ")
	data=data.replace("<"," ")
	data=data.replace(">"," ")
	data=data.replace("https"," ")
	data=data.replace("org"," ")
	data=data.replace("www"," ")
	data=data.replace("com"," ")

	word_list=data.split()

	return word_list

	# word_dictionary={}

	# list_length=len(word_list)

	

	# for word in word_list:
	# 	if word in word_dictionary:
	# 		word_dictionary[word] = word_dictionary[word] + 1
	# 	else:
	# 		word_dictionary[word] = 1

	# sorted_list=sorted(word_dictionary.items(), key=operator.itemgetter(1),reverse=True)

	# context={'data':data, 'word_dictionary':sorted_list}

	# return render(request,'webapp/result.html',context)

def unknown(request):
	url_list=domain.objects.all()

	for i in url_list:
		word_list=url_ex(i.url1)
		for j in word_list:
			try:
				obj=word.objects.get(w=j)
				obj.x=obj.x+1
				obj.save()
			except:
				obj=word.objects.create(w=j)
				obj.save()
	context={
		'data':word.objects.all().order_by('-x')
	}
	
	return render(request,'webapp/result.html',context)







