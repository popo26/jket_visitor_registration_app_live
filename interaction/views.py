import datetime
from django.shortcuts import get_object_or_404, render, redirect
from interaction.forms import CheckOutForm, UserForm
from interaction.models import Member, ClassRoom
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

YEAR = datetime.datetime.now().year

def index(request):
    return render(request, 'interaction/index.html', {'year': YEAR})


def classroom_list(request):
    class_room_list = ClassRoom.objects.all()
    context = {
        'class_room_list': class_room_list,
        'year': YEAR
        }
    return render(request, 'interaction/classroom_list.html', context=context)


def student_list(request, classroom_pk):
    classroom = get_object_or_404(ClassRoom, pk=classroom_pk)
    students = classroom.member_set.filter(class_room=classroom_pk)
    s_list = []
    for s in students:
        s = User.objects.get(username=s)
        s_list.append(s)
    context = {
        'classroom': classroom,
        's_list': s_list,
        'year': YEAR,
        }
    return render(request, 'interaction/student_list.html', context=context)
    

def checkout(request, student_pk):
    current_time = datetime.datetime.now()
    student = get_object_or_404(User, id=student_pk)
    s = Member.objects.get(user=student.id)
    classroom_name = s.class_room
    
    if request.method == 'POST':
        checkout_form = CheckOutForm(request.POST)
        password_form = UserForm(request.POST)
        if checkout_form.is_valid() and password_form.is_valid():
            new_form = checkout_form.save(commit=False)
            new_form.student = User.objects.get(pk=student_pk)
            new_form.class_room = classroom_name

            password = request.POST["password"]

            if student.check_password(password) != True :
                print("Incorrec Password")
                message = "Your PIN must be exactly 6 digits."    

                context = {
                    'checkout_form': checkout_form,
                    'student': student,
                    'current_time': current_time,
                    "classroom_name": classroom_name,
                    'password_form': password_form,
                    'year': YEAR,
                    'message': message,
                    }
                return render(request, "interaction/checkout.html", context=context)
            else:
                new_form.save()
                return redirect('success_checkout')            
  
        else:
            print("not valid form")
            print(checkout_form.errors.as_data())
             
    else:   
        checkout_form = CheckOutForm(initial={'checkout_choice': '1'})
        c = ClassRoom.objects.get(pk=classroom_name.pk)
        current_time = datetime.datetime.now()
        class_start_time = c.start_time
        class_end_time = c.end_time
        two_hour_class_swap_time = datetime.timedelta(0, 3600)
        one_hour_class_swap_time = datetime.timedelta(0, 1800)
        thirty_min_delta = datetime.timedelta(0,1800)
        today_start_time_with_date = datetime.datetime.combine(datetime.date.today(), class_start_time)
        today_end_time_with_date = datetime.datetime.combine(datetime.date.today(), class_end_time)  
        today_end_time_with_date_plus_30min = today_end_time_with_date + thirty_min_delta 
        ''' e.g.Default pickup choice is "Dropoff". 
            Also first half displays Dropoff. Next half + 30 min shows Pickup. '''
        if c.duration() == datetime.timedelta(seconds=7200):
            checkout_option_swap_time_with_date = today_start_time_with_date + two_hour_class_swap_time
            if today_end_time_with_date_plus_30min > current_time > checkout_option_swap_time_with_date:
                checkout_form = CheckOutForm(initial={'checkout_choice': '2'}) 
        else:
            checkout_option_swap_time_with_date = today_start_time_with_date + one_hour_class_swap_time
            if today_end_time_with_date_plus_30min > current_time > checkout_option_swap_time_with_date:
                checkout_form = CheckOutForm(initial={'checkout_choice': '2'})
         
        password_form = UserForm()
        
        context = {
            'checkout_form': checkout_form,
            'student': student,
            'current_time': current_time,
            "classroom_name": classroom_name,
            "password_form": password_form,
            'year': YEAR,
            }
        return render(request, "interaction/checkout.html", context=context)


def success_checkout(request):
    return render(request, 'interaction/success_checkout.html', {'year': YEAR})


