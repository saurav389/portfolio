from django.shortcuts import render
from django.http import HttpResponse
from .models import contact,homeDetail,experience,service,portfolio,about,contactDetails
from .form import ContactForm

# Create your views here.
def index_view(request):


    exper = experience.objects.all()
    serv = service.objects.all()
    abt = about.objects.all()
    count = homeDetail.objects.all().count()
    counter = contactDetails.objects.all().count()
    if counter is 1:
        details = contactDetails.objects.all()


    if count is 1:
        home_detail = homeDetail.objects.all()

    
    context = {"home_detail":home_detail,
                "experience":exper,
                "service":serv,
                "details":details,
                "about":abt
                }

    return render(request,"index.html",context)

def about_view(request):

    cont = about.objects.all().count()
    if cont is 1:
        data = about.objects.all()


    context = {"about":data
    }
    return render(request,"about.html",context)

def portfolio_view(request):
    data = portfolio.objects.all()
    context = {"portfolio":data
    }
    return render(request,"portfolio.html",context)

def contact_view(request):
    cont = contactDetails.objects.all().count()
    msg = ''
    if request.method == 'POST':
        name = request.POST.get('name')
        company = request.POST.get('company')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(request.POST)
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            msg = form.errors
        

    if cont is 1:
        data = contactDetails.objects.all()

    context = {"contactDetails":data,
                "message":msg
                }
    return render(request,"contact.html",context)