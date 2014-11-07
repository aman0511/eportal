import uuid
from django.db.models import Q
from django.shortcuts import render_to_response,HttpResponseRedirect,render,redirect
from django.core.mail import send_mail
from django.conf import settings
from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.conf import settings
from student.models import user,student
from django.core import serializers

# Create your views here.
import datetime

#function that generates random password
def get_password():
    temp_pass = str(uuid.uuid4())[:11].replace('-','').lower()
    try:
        pass_exists = user.objects.get(password=temp_pass)
        get_password()
    except:
        return temp_pass
    
    


def login(request):
	
	
	if('login' in request.POST):
		username = request.POST.get('username', '')
		password=request.POST.get('password', '')
		if(username!='' and password!=''):
			try:
				result=user.objects.filter(username=username).values()[0]
				if(result['password']==password):
					request.session['uname'] = username
					return redirect('home')
					#return render(request,'login_register.html',{'message_login':request.session['uname']})
				else:
					return render(request,'login_register.html',{'message_login':"wrong Username or Password"})
			except:
				return render(request,'login_register.html',{'message_login':"wrong Username or Password"})

	if('register' in request.POST):

		R_username = request.POST.get('R_username', '')
		if(R_username!=''):
			try:
				user_exists = user.objects.get(username=R_username)
				return render(request,'login_register.html',{'message_register_alert':"User with this email is already registered"})
			except:
				temp_pass = get_password()
				b = user(username=R_username,password=temp_pass,status=True)
				b.save()
				subject="Confirmation  mail"
				message = "your password is " + temp_pass
				from_email = settings.EMAIL_HOST_USER
				to_list=[R_username,settings.EMAIL_HOST_USER]
				send_mail(subject,message,from_email,to_list, fail_silently=True)
				return render(request,'login_register.html',{'message_register_success':"your password has been sent to your e-mail"})
	return render(request,'login_register.html',{'message':""})


def home(request):
	if 'uname' in request.session:
		try:
			info = student.objects.get(username=request.session['uname'])
		#	request.session['info']=serializers.serialize('json',info)
			return render(request,'index.html',{'student':info})
		except:
			return render(request,'index.html')
	now = datetime.datetime.now()
	now = datetime.datetime.now()
	return render(request,'index.html')
	
def courses(request):
	return render_to_response('courses.html')
def faculty(request):
	return render_to_response('courses.html')

def logout(request):
	if 'uname' in request.session:
		del request.session['uname']
		#del request.session['info']
	return redirect('home')

