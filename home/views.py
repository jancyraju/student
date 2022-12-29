# Create your views here.
from django.shortcuts import render,redirect
from django.views import View
from account.models import Contact,Staff
from home.models import Students
from .forms import StudentForm
from django.contrib import messages

class Home(View):
    def get(self,request):
        return render(request,'home.html')
    

class Form(View):
    def get(self,request):
        std1=StudentForm()
        return render(request,'form.html',{'form':std1})
    def post(self,request):
        if request.method == "POST":
            std1=StudentForm(request.POST)
            if std1.is_valid():
                std1.save()
                student=Students.objects.all()
                return render (request,'show.html',{'form':student})
            else:
                print("Form not valid") 
            return redirect("show")   


class Show(View):
    def get(self,request):
        student=Students.objects.all()
        return render (request,'show.html',{'form':student})

 
class Edit(View):
    def get(self,request):
        return render(request,'edit.html')
    
    
class Delete(View):
    def get(self,request):
        delete=request.GET['delete']
        #print(delete)
        Students.objects.filter(stud_id=delete).delete()
        student=Students.objects.all()
        return render(request,'show.html',{'form':student})

    
class Enquery(View):
    def get(self,request):
        customer=Contact.objects.all()
        return render(request,'enquery.html',{'form':customer})
    
    
class Profile(View):
    def get(self,request):
        if request.session['email'] is not None:
            customer=Staff.objects.filter(email=request.session['email'])
        return render(request,'profile.html',{'form':customer})
    
    
class Editprofile(View):
    def get(self,request):
        edit1=request.session['email']
        edit=Staff.objects.filter(email=edit1)
        return render (request,'editprofile.html',{'customer':edit})
    def post(self,request):
        # print(request.GET['edit'])
        edit1=request.session['name']
        if request.method == 'POST':
            if Staff.objects.filter(email=edit1).exists():
                if request.POST['password']:
                    Staff.objects.filter(email=edit1).update(password=request.POST['password'])
                if request.POST['name']:
                    Staff.objects.filter(email=edit1).update(name=request.POST['name'])
            # To check email is unique in staff table
                if request.POST['email']:
                    if Staff.objects.filter(email=edit1).exist():
                        edit=Staff.objects.filter(email=edit1)
                        messages.error(request,"email id already exist")
                        return render(request,'editprofile.html',{'form':edit})
                    else:
                        Staff.objects.filter(email=edit1).update(name=request.POST['email'])
                        request.session['email']=request.POST['email']
                if request.POST['phno']:
                    Staff.objects.filter(email=edit1).update(phno=request.POST['phno'])               
        customer=Staff.objects.filter(name=request.session['name'])
        return render(request,'profile.html',{'customer':customer}) 
            

class Staffs(View):
    def get(self,request):
        customer=Staff.objects.all()
        return render(request,'staff.html',{'form':customer})
    

class Edit(View):
    def get(self,request):
        edit1=request.GET['edit']
        edit=Students.objects.filter(stud_id=edit1)
        return render(request,'edit.html',{'form':edit})
    def post(self,request):
        edit1=request.GET['edit']
        if request.method == 'POST':
            if Students.objects.filter(stud_id=edit1).exists():
                if request.POST['stud_address']:
                    Students.objects.filter(stud_id=edit1).update(stud_address=request.POST['stud_address'])
                if request.POST['stud_place']:   
                    Students.objects.filter(stud_id=edit1).update(stud_place=request.POST['stud_place'])
                if request.POST['stud_name']:   
                    Students.objects.filter(stud_id=edit1).update(stud_name=request.POST['stud_name'])
                if request.POST['stud_email']:   
                    Students.objects.filter(stud_id=edit1).update(stud_email=request.POST['stud_email'])
                if request.POST['stud_phno']:   
                    Students.objects.filter(stud_id=edit1).update(stud_phno=request.POST['stud_phno'])
                student=Students.objects.all()   
                return render(request,'show.html',{'form':student})
    
    
    
          

