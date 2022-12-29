from django.contrib import auth
from django.contrib import messages
from .models import Contact,Course,Staff
from django.contrib import messages
from django.shortcuts import redirect,render
# from django.views import View


# Create your views here.

def mainhome(request):
    return render(request,'mainhome.html')


def signin(request):
    if request.method == "POST":
        email =request.POST['email']
        password=request.POST['password']
        try:
            check_user = Staff.objects.get(email=email,password=password)
            request.session['email']=check_user.email
            request.session['name']=check_user.name
            request.session['phno']=check_user.phno
            return redirect('home')
        except Staff.DoesNotExist:
            messages.error(request,'invalid username and password')
            return redirect('signin')
    return render(request,'signin.html')

def signup(request):
    if request.method == "POST" :
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        phno=request.POST['ph']
        password2=request.POST['password2']
        if password == password2 :
            if Staff.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('signup')
            else:
                customer = Staff.objects.create(email = email, name= name, password=password, phno=phno)
                customer.save()
                messages.info(request,'user created')
                return redirect('signin')
        else:
          messages.info(request,'password is not match')
          return redirect('signup')
    else:
        return render(request,'signup.html')

def forgot(request):
    if request.method == 'POST':
        emails = request.POST['email']
        passwords = request.POST['password']
        if Staff.objects.filter(email=emails).exists():
            Staff.objects.filter(email=emails).update(password=passwords)
            return redirect('signin')
        else:
            messages.error(request,'invalid email')
            return redirect('forgot')
    return render(request,'forgot.html')

# class Forgot(View):
#     def get(self,request):
#         return render(request,'forgot.html')
#     def post(self,request):
#         if request.method=="POST":
#             emails=request.POST['email']
#             passwords=request.POST['password']
#             if Staff.objects.filter(email=emails).exists():
#                 Staff.objects.filter(email=emails).update(password=passwords)
#                 return render(request,"signin.html")
#             else:
#                 messages.error(request,"invalid mail")
#                 return render(request,"forgot.html")

def course(request):
    courses={
        'course':Course.objects.all()
    }
    return render(request,'course.html',courses)



def gallery(request):
    return render(request,'gallery.html')



def contact(request):
    if request.method=="POST":
        if request.POST['name']is not None:
            enq=Contact.objects.create(name=request.POST['name'],email=request.POST['email'],phno=request.POST['phno'])
            enq.save()
            # message.success(request,'contact-soon')
            dicts={'out':1,'name':request.POST['name']}
            return render(request,'contact.html',dicts)
    return render(request,'contact.html')
