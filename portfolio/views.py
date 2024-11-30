from django.shortcuts import render
from django.http import HttpResponse
from .models import Job
import json     # json use krne ke liye json ki library import karlete hain
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(req):
    return HttpResponse("Hello, Welcome to my portfolio.") 

@csrf_exempt
# Creating GET api
def job(request):
    if request.method =="GET":
        # result = []     # We will store our all data in result variable. But first we have to GET all of our data from our database for that we will use Django ORM.
        jobs = Job.objects.all()    # means job ke saare objects lee aao
        # for job in jobs:            # and parse each of them
        #     data = {
        #         "company": job.company,
        #         "description": job.description
        #     }
        #     result.append(data)     # Aur result ke array mein append krdo apne data ko.
        # return HttpResponse(json.dumps(result))     # json.dumps will convert our result in json format.
        return render(request, "portfolio/index.html", {"jobs":jobs})

    if request.method =="POST":
        body_unicode = request.body.decode("utf-8")     # body jab bhi request mei aati hai to encoded format mei aati hai so we are decoding it.
        data = json.loads(body_unicode)     # ab isme se body ka data nikalenge
        company = data['company']   # ab iss data mein se company ka data nikaal lenge
        description = data['description']   # ab iss data mein se description ka bhi data nikaal lenge

        job = Job(company = company, description = description)     # ab uper waali chize database mei daalne ke liye object create karenge Job name se
        job.save()
        return HttpResponse({"company Added successfully"}) 

    if request.method =="DELETE":
        body_unicode = request.body.decode("utf-8")     # body jab bhi request mei aati hai to encoded format mei aati hai so we are decoding it.
        data = json.loads(body_unicode)     # ab isme se body ka data nikalenge
        company = data['company']   # ab iss data mein se company ka data nikaal lenge

        job = Job.objects.filter(company=company).delete()
        return HttpResponse({"company Deleted Successfully"})
    