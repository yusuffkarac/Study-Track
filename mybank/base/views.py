from email.policy import default
import imp
from multiprocessing import context
from time import sleep
from django.shortcuts import render
from base.models import Products, Days,Activity,Lectures,Grades,Studies,TransferCodes
from django.shortcuts import redirect
from django.db.models import Sum
from datetime import date, datetime   
from django.db.models.functions import (ExtractDay)
## import http response redirect
from django.http import HttpResponseRedirect


def calendar(request):
    
    return render(request, 'base/calendar.html')

def harcamalarım(request):
    if request.user.is_authenticated:


        context = {
            "products": Products.objects.filter(created_by = request.user),
            "total": Products.objects.filter(created_by = request.user).aggregate(Sum('price')),
            "total_market": Products.objects.filter(created_by = request.user).filter(type="Market").aggregate(Sum('price')),
            "total_okul": Products.objects.filter(created_by = request.user).filter(type="Okul").aggregate(Sum('price')),
            "total_diger": Products.objects.filter(created_by = request.user).filter(type="Diğer").aggregate(Sum('price')),


        }
        
        return render(request, 'base/main.html',context)
    else:
        return redirect("login")

def lectures(request):
    if request.user.is_authenticated:

        context={
            'is_home':True,
            'lectures': Lectures.objects.filter(created_by = request.user),
            'days': Days.objects.filter(created_by = request.user),
            'activities': Activity.objects.filter(created_by = request.user).order_by('-is_high_priority','is_done')[:8],
            'not_done_activities': Activity.objects.filter(created_by = request.user).filter(is_done=False),
            'studies' : Studies.objects.filter(created_by = request.user)[:5],
        }
        return render(request, 'base/lectures.html',context)
    else:
        return redirect("login")
def add_activity(request):
    if request.user.is_authenticated:

        context={
            'lectures': Lectures.objects.filter(created_by = request.user).all(),
            'user': request.user,
            }
        return render(request, 'base/addactivity.html',context)
    else:
        return redirect("login")

def add_activity_def(request):
    if request.user.is_authenticated:

        context={
            'lectures': Lectures.objects.filter(created_by = request.user).all(),
            }
        if request.method == "POST":
            title = request.POST['act_title']
            description = request.POST['act_description']
            lecture = request.POST['act_lecture']
            is_grade = request.POST.get("act_is_grade",False)
            date = request.POST['startDate']
            created_by =   request.user 
            is_high_priority=request.POST.get("act_is_high_priority",False)


            if is_grade:
                weight = request.POST.get("act_weight",1)
            else:
                weight = 0
            


        new_act = Activity(title=title,description=description,weight=weight,date=date,lecture=Lectures.objects.get(id=lecture),is_grade=is_grade,created_by=created_by,is_high_priority=is_high_priority)
        new_act.save()
        return redirect("/")

    else:
        return redirect("login")



def edit_activity(request,id):
    if request.user.is_authenticated:
        context={
            'lectures': Lectures.objects.filter(created_by = request.user).all(),
            'title' : Activity.objects.get(id=id).title,
            'description' : Activity.objects.get(id=id).description,
            'lecture_selected' : Activity.objects.get(id=id).lecture,
            'is_grade' : Activity.objects.get(id=id).is_grade,
            'weight' : Activity.objects.get(id=id).weight,
            'date' : (Activity.objects.get(id=id).date),
            'id' : id,
            }
        if request.method == "POST":
            title = request.POST['act_title']
            description = request.POST['act_description']
            lecture = request.POST['act_lecture']
            is_grade = request.POST.get("act_is_grade",False)
            date = request.POST['startDate']
            created_by =   request.user 
            is_high_priority=request.POST.get("act_is_high_priority",False)
        
            if is_grade:
                weight = request.POST.get("act_weight",1)
            else:
                weight = 0
            Activity.objects.filter(id=id).update(title=title,description=description,weight=weight,date=date,lecture=Lectures.objects.get(id=lecture),is_grade=is_grade,created_by=created_by,is_high_priority=is_high_priority)
            return redirect("/")

       
        return render(request, 'base/editactivity.html',context)
     
def delete_activity(request,id):
    if request.user.is_authenticated:

        Activity.objects.filter(id=id).delete()
        return redirect("/")
    else:
        return redirect("login")

def add_lecture(request):
    if request.user.is_authenticated:
 
        context={
            'days': Days.objects.all(),
            }
        
        return render(request, 'base/addlecture.html',context)
    
    else:
        return redirect("login")

def add_lecture_def(request):
    if request.user.is_authenticated:

        context={
            'days': Days.objects.all(),
            }
        if request.method == "POST":
            title = request.POST['lecture_title']
            description = request.POST['lecture_description']
            days = request.POST.getlist('lecture_days')
            created_by =   request.user 

        new_lec = Lectures(title=title,description=description,created_by=created_by)
        new_lec.save()
        for day in days:
            new_lec.days_of_lec.add(Days.objects.get(id=day))
        
        return  (HttpResponseRedirect('/'))
    else:
        return redirect("login")


def add_study(request):
    if request.user.is_authenticated:

        context={
            'lectures': Lectures.objects.filter(created_by = request.user).all(),
            }

        return render (request, 'base/addstudy.html',context)
    else:
        return redirect("login")
def add_study_def(request):
    if request.user.is_authenticated:

        context={
            'lectures': Lectures.objects.filter(created_by = request.user).all(),
            }
        if request.method == "POST":
            title = request.POST['std_title']
            lecture = request.POST['std_lecture']
            minute = request.POST['std_minute']
            created_by =   request.user 

            new_study = Studies(title=title,lecture=Lectures.objects.get(id=lecture),how_many_minutes=minute,created_by=created_by)
            new_study.save()
        return  (HttpResponseRedirect('/get_details/'+str(lecture)))
    else:
        return redirect("login")


def add_transfercode(request):
    if request.user.is_authenticated:
        halls_list = [
            {
                "id": 1,
                "name": "Öğrenci Yemekhanesi 1 (Rekreasyon alanı yanı)"
            },
            {
                "id": 2,
                "name": "Öğrenci Yemekhanesi 3 (FEN EDEBİYAT)"
            },
            {
                "id": 3,
                "name": "Sağlık Bilimleri Fakültesi Yemekhanesi"
            },
            {
                "id": 4,
                "name": "Spor Bilimleri Fakültesi Yemekhanesi"
            },
            {
                "id": 5,
                "name": "Yabancı Diller Yüksekokulu"
            },
            {
                "id": 6,
                "name": "Glutensiz Yemekhane"
            },
            {
                "id": 7,
                "name": "MYO Soma"
            },
            {
                "id": 8,
                "name": "MYO Kırkağaç"
            },
            {
                "id": 9,
                "name": "MYO Akhisar"
            },
            {
                "id": 10,
                "name": "Hasan Ferdi Turgutlu Teknoloji Fakültesi"
            },
            {
                "id": 11,
                "name": "MYO Turgutlu"
            },
            {
                "id": 12,
                "name": "MYO Ahmetli"
            },
            {
                "id": 13,
                "name": "MYO Salihli"
            },
            {
                "id": 14,
                "name": "MYO Saruhanlı"
            },
            {
                "id": 15,
                "name": "MYO Köprübaşı"
            },
            {
                "id": 16,
                "name": "Demirci Eğitim Fakültesi"
            }
        ]

        # tarihi geçenleri kaldır

        transfer_codes = TransferCodes.objects.filter(created_at__gte= datetime.now().date())
        context = {
            'halls': halls_list,
            'transfer_codes': transfer_codes,
        }

        return render(request, 'base/addtransfercode.html', context)
    else:
        return redirect("login")

def add_transfercode_def(request):    
    if request.user.is_authenticated:

        context={
            'lectures': Lectures.objects.filter(created_by = request.user).all(),
            }
        if request.method == "POST":
            hall = request.POST['trf_hall']
            meal = request.POST['trf_meal']
            code = request.POST['trf_code']
            
            created_by =   request.user 

            new_code = TransferCodes(code=code,hall=hall,meal=meal,created_by=created_by)
            new_code.save()
        

        # run the function as render
        return redirect("/add_transfercode")
    else:
        return redirect("login")

def pomodoro(request):
    if request.user.is_authenticated:

        context={
            'lectures': Lectures.objects.filter(created_by = request.user).all(),
            }
        return render(request, 'base/pomodoro.html',context)
    else:
        return redirect("login")

def add_product(request):
    if request.user.is_authenticated:

        context={
            'products': Products.objects.filter(created_by = request.user).all(),
        }

        name = request.GET.get('prname')
        price = request.GET.get('prprice')
        type = request.GET.get('prtype')
        created_by =   request.user
        new_pr = Products(name=name,price=price,type=type,created_by=created_by)
        new_pr.save()
        return redirect("/harcamalarım")

    else:
        return redirect("login")


def delete_item(request,id):
    if request.user.is_authenticated:

        Products.objects.filter(id=id).delete()
        return redirect("/harcamalarım")
    else:
        return redirect("login")
def update_item(request,id):
    if request.user.is_authenticated:

        name = request.GET.get('prname')
        price = request.GET.get('prprice')
        type = request.GET.get('prtype')

        Products.objects.filter(id=id).update(name=name,price=12,type=type)
        return redirect("/harcamalarım")
    else:
        return redirect("login")

def add_like(request,id):

    Products.objects.filter(id=id).update(gifLink="https://mir-s3-cdn-cf.behance.net/project_modules/disp/e4299734559659.56d57de04bda4.gif")
    return redirect("/harcamalarım")


def add_heart(request,id):

    Products.objects.filter(id=id).update(gifLink="https://mir-s3-cdn-cf.behance.net/project_modules/disp/65ea2034559659.56d57de06cea2.gif")
    return redirect("/harcamalarım")


def add_haha(request,id):

    Products.objects.filter(id=id).update(gifLink="https://mir-s3-cdn-cf.behance.net/project_modules/disp/35c9bf34559659.56d57de0eb467.gif")
    return redirect("/harcamalarım")

def add_wow(request,id):

    Products.objects.filter(id=id).update(gifLink="https://mir-s3-cdn-cf.behance.net/project_modules/disp/6105c734559659.56d59c54f0d05.gif")
    return redirect("/harcamalarım")

def add_cry(request,id):

    Products.objects.filter(id=id).update(gifLink="https://mir-s3-cdn-cf.behance.net/project_modules/disp/3eee1d34559659.56d59de621daa.gif")
    return redirect("/harcamalarım")


def add_angry(request,id):
    Products.objects.filter(id=id).update(gifLink="https://mir-s3-cdn-cf.behance.net/project_modules/disp/e66e6e34559659.56d57de095aee.gif")
    return redirect("/harcamalarım")


def get_details(request,id):
    if request.user.is_authenticated:
        if Studies.objects.filter(lecture_id=id).aggregate(Sum('how_many_minutes'))['how_many_minutes__sum']:
            print('alo1')
            context={
                'lectures': Lectures.objects.filter(created_by = request.user).all(),
                'lecture': Lectures.objects.filter(created_by = request.user).filter(id=id),
                'days': Days.objects.filter(),
                'days_of_lec': Lectures.objects.filter(created_by = request.user).filter(id=id).values_list('days_of_lec__name',flat=True),
                'activities': Lectures.objects.filter(created_by = request.user).get(id=id).activities.all().order_by('-is_high_priority','is_done'),
                'datetime_now': datetime.now(),
                'kalanzaman':  Activity.objects.values_list('date'),
                'grades': Grades.objects.filter(created_by = request.user).all(),
                'not_done_activities': Activity.objects.filter(created_by = request.user).filter(is_done=False),
                'range_earned':  range(Lectures.objects.filter(created_by = request.user).get(id=id).earned_point),
                'range_notearned': range(100 - Lectures.objects.get(id=id).earned_point),
                'studies' : Studies.objects.filter(lecture_id=id),
                "total_study": Studies.objects.filter(lecture_id=id).aggregate(Sum('how_many_minutes')),
                'water_height' : Studies.objects.filter(lecture_id=id).aggregate(Sum('how_many_minutes'))['how_many_minutes__sum']/1200*14,
                'water_top' : 14.3 - Studies.objects.filter(lecture_id=id).aggregate(Sum('how_many_minutes'))['how_many_minutes__sum']/1200*14-1,
                'effect_top' : 14.3 - Studies.objects.filter(lecture_id=id).aggregate(Sum('how_many_minutes'))['how_many_minutes__sum']/1200*14-0.9,

                
            }
        else:
            print('alo2')
            context={
                'lectures': Lectures.objects.filter(created_by = request.user).all(),
                'lecture': Lectures.objects.filter(created_by = request.user).filter(id=id),
                'days': Days.objects.filter(),
                'days_of_lec': Lectures.objects.filter(created_by = request.user).filter(id=id).values_list('days_of_lec__name',flat=True),
                'activities': Lectures.objects.filter(created_by = request.user).get(id=id).activities.all().order_by('-is_high_priority','is_done'),
                'datetime_now': datetime.now(),
                'kalanzaman':  Activity.objects.values_list('date'),
                'grades': Grades.objects.filter(created_by = request.user).all(),
                'not_done_activities': Activity.objects.filter(created_by = request.user).filter(is_done=False),
                'range_earned':  range(Lectures.objects.filter(created_by = request.user).get(id=id).earned_point),
                'range_notearned': range(100 - Lectures.objects.get(id=id).earned_point),
                'studies' : Studies.objects.filter(lecture_id=id),
                "total_study": Studies.objects.filter(lecture_id=id).aggregate(Sum('how_many_minutes')),
                'water_height' :0,
                'water_top' :0,
                'effect_top' : -10000,
            }
            print(context['activities'],'aloo')

        
        return render(request, 'base/lectures.html',context)
    else:
        return redirect("login")

def get_lectures_byday(request,id):

    context={
        'lectures': Lectures.objects.filter(days_of_lec__id=id,created_by = request.user).all(),
    }
    
    return render(request, 'base/lectures.html',context)


def set_done(request,id):
    if request.user.is_authenticated:

        Activity.objects.filter(id=id).update(is_done = not Activity.objects.get(id=id).is_done)
        grade = request.GET.get('grade_act',0)
        
        new_grade = Grades(grade=grade,activity_id=id)
        new_grade.save()

        Lectures.objects.filter(id=Activity.objects.get(id=id).lecture_id).update(earned_point= Lectures.objects.get(id=Activity.objects.get(id=id).lecture_id).earned_point+((int(grade)*int(Activity.objects.get(id=id).weight))/100))
        
        if grade != 0:
            sleep(7)
            return  (HttpResponseRedirect('/get_details/'+str(Activity.objects.get(id=id).lecture_id)))
        else:
            return  (HttpResponseRedirect('/get_details/'+str(Activity.objects.get(id=id).lecture_id)))

    else:
        return redirect("login")



