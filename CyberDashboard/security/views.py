from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import json
import os
# from ip2geotools.databases.noncommercial import DbIpCity
import requests
import joblib

# Load the trained model and vectorizer
# sql 
model_filename = os.path.join(settings.BASE_DIR, 'ml_models/sql_svm_model.joblib')
vectorizer_filename = os.path.join(settings.BASE_DIR, 'ml_models/sql_count_vectorizer.joblib')  # Assuming you saved the CountVectorizer

sql_svm_model = joblib.load(model_filename)
sql_vectorizer = joblib.load(vectorizer_filename)

# phishing
model_filename = os.path.join(settings.BASE_DIR, 'ml_models/phishing_dt_model.joblib')
vectorizer_filename = os.path.join(settings.BASE_DIR, 'ml_models/phishing_count_vectorizer.joblib')  # Assuming you saved the CountVectorizer

phishing_dt_model = joblib.load(model_filename)
phishing_vectorizer = joblib.load(vectorizer_filename)


# dns tunneling
model_filename = os.path.join(settings.BASE_DIR, 'ml_models/dns_svm_model.joblib')
vectorizer_filename = os.path.join(settings.BASE_DIR, 'ml_models/dns_count_vectorizer.joblib')  # Assuming you saved the CountVectorizer

dns_svm_model = joblib.load(model_filename)
dns_vectorizer = joblib.load(vectorizer_filename)


# new work started
def home(request):
    return render(request, 'sample.html')

def index(request):
    all_users = User.objects.all()
    context = {
        'no_of_users' : len(all_users)
    }
    return render(request, 'index.html', context)


def prediction(request):
    all_users = User.objects.all()
    context = {
        'no_of_users' : len(all_users)
    }
    if request.method == "POST":
        if 'sql' in request.POST:
            sql_query = request.POST.get('sql_query')
            sql_query = sql_vectorizer.transform([sql_query])
            prediction = sql_svm_model.predict(sql_query)
            if prediction[0] == 1:
                messages.warning(request, "SQL Injection Attack Detected...")
            else:
                messages.success(request, "No SQL Injection Attack Detected...")

        elif 'phishing' in request.POST:
            url = request.POST.get('url')
            url = phishing_vectorizer.transform([url])
            prediction = phishing_dt_model.predict(url)
            if prediction[0] == 1:
                messages.warning(request, "Phishing Attack Detected...")
            else:
                messages.success(request, "No Phishing Attack Detected...")
        elif 'dns-tunneling' in request.POST:
            dns = request.POST.get('dns')
            dns = dns_vectorizer.transform([dns])
            prediction = dns_svm_model.predict(dns)
            if prediction[0] == 1:
                messages.warning(request, "DNS Tunneling Attack Detected...")
            else:
                messages.success(request, "No DNS Tunneling Attack Detected...")
    return render(request, 'prediction.html', context)



def user_awareness(request):
    all_users = User.objects.all()
    context = {
        'no_of_users' : len(all_users)
    }
    return render(request, 'user_awareness.html', context)

def solutions(request):
    all_users = User.objects.all()
    context = {
        'no_of_users' : len(all_users)
    }
    return render(request, 'solutions.html', context)

def json_data(request):
    with open(os.path.join( settings.BASE_DIR, 'json_data/100_attacks.json')) as json_file:
                data = json.load(json_file)
    return JsonResponse(data, safe=False)


def login_page(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username = email)
        if len(user_obj) == 0 :
            messages.warning(request, "Email is not registered")
            return HttpResponseRedirect(request.path_info)
        
        user_obj = authenticate(username = email, password = password)

        if not user_obj :
            messages.warning(request, "Password is wrong")
            return HttpResponseRedirect(request.path_info)
        
        if user_obj : 
            login(request, user_obj)
            return redirect('/dashboard')

    return render(request, 'login.html')


def register_page(request):

    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        # phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username = email)

        if user_obj.exists():
            messages.warning(request, "Email is already registered")
            return HttpResponseRedirect(request.path_info)

        user_obj = User.objects.create(first_name = fname, last_name = lname, email= email, username = email)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, "You are registered with CyberDashboard")
        messages.success(request, "Login With you Credentials")
        return redirect('/login')
    return render(request, 'register.html')


def logout_page(request):
    logout(request)
    messages.success(request, "You are Logged Out from Dashboard")
    return redirect('/')


def get_geo_cordinates_ajax(request):
    # src_ip = request.GET.get('src_ip')
    # dst_ip = request.GET.get('dst_ip')

    # payload_src = {'key': '9B4C80763C9402E38824BDA5439E8BA8', 'ip': src_ip, 'format': 'json'}
    # api_result_src = requests.get('https://api.ip2location.io/', params=payload_src)
    # json_data_src = api_result_src.json()

    # payload_dst = {'key': '9B4C80763C9402E38824BDA5439E8BA8', 'ip': dst_ip, 'format': 'json'}
    # api_result_dst = requests.get('https://api.ip2location.io/', params=payload_dst)
    # json_data_dst = api_result_dst.json()

  
    # return JsonResponse({
    #     'src' : [json_data_src.get('longitude'), json_data_src.get('latitude')],
    #     'dst' : [json_data_dst.get('longitude'), json_data_dst.get('latitude')],
    # })
    return JsonResponse({})