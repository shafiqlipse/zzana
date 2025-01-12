from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
# Create your views here.


def subjects(request):
    subjects = Subject.objects.all()
    if request.method == "POST":
        form = SubjectForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            return redirect('subjects')  # Redirect after save
        else:
            form_errors = form.errors  # Capture form errors
    else:
        form = SubjectForm()
    context = {
        "subjects": subjects,
        "form": form,

        # "form_errors": form_errors,
    }
    return render(request, "subjects/subjects.html", context)


@login_required(login_url="login")
def subject_delete(request, id):
    stud = Subject.objects.get(id=id)
    if request.method == "POST":
        stud.delete()
        return redirect("subjects")

    return render(request, "subjects/delete_subject.html", {"obj": stud})

# Create your views here.


def subject_details(request, id):
    subject = get_object_or_404(Subject, id=id)
    if request.method == "POST":
        form = PaperForm(request.POST, request.FILES)
        if form.is_valid():
            stream = form.save(commit=False)
            stream.subject = subject
            stream.save()
            return redirect('subject', id=subject.id)  # Redirect after save
        else:
            form_errors = form.errors  # Capture form errors
    else:
        form = PaperForm()
    context = {
        "subject": subject,
        "form": form,
        "streams": subject.stream_set.all(),
        # "form_errors": form_errors,
    }
    return render(request, "subjects/subject.html", context)


def classes(request):
    classes = Class.objects.all()
    if request.method == "POST":
        form = ClassForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            return redirect('classes')  # Redirect after save
        else:
            form_errors = form.errors  # Capture form errors
    else:
        form = ClassForm()
    context = {
        "classes": classes,
        "form": form,

        # "form_errors": form_errors,
    }
    return render(request, "classes/classes.html", context)


@login_required(login_url="login")
def class_delete(request, id):
    stud = Class.objects.get(id=id)
    if request.method == "POST":
        stud.delete()
        return redirect("classs")

    return render(request, "classes/delete_class.html", {"obj": stud})

# Create your views here.


def class_details(request, id):
    classroom = get_object_or_404(Class, id=id)
    if request.method == "POST":
        form = StreamForm(request.POST, request.FILES)
        if form.is_valid():
            stream = form.save(commit=False)
            stream.classroom = classroom
            stream.save()
            # Redirect after save
            return redirect('classroom', id=classroom.id)
        else:
            form_errors = form.errors  # Capture form errors
    else:
        form = StreamForm()
    context = {
        "classroom": classroom,
        "form": form,
        "streams": classroom.stream_set.all(),
        # "form_errors": form_errors,
    }
    return render(request, "classes/class.html", context)


def timetable_create(request):
    if request.method == 'POST':
        data = request.POST
        day_of_week = data.get('day_of_week')
        class_name_id = data.get('class_name')
        subject_id = data.get('subject')
        teacher_id = data.get('teacher')
        start_time = data.get('start_time')
        end_time = data.get('end_time')
        period = data.get('period')

        timetable = Timetable(
            class_name_id=class_name_id,
            subject_id=subject_id,
            teacher_id=teacher_id,
            day_of_week=day_of_week,
            start_time=start_time,
            end_time=end_time,
            period=period,
        )
        timetable.save()
        return redirect('timetable_list')

    subjects = Subject.objects.all()
    teachers = Teacher.objects.all()
    class_name = Class.objects.all()
    return render(request, 'timetable/timetable_create.html', {'subjects': subjects, 'teachers': teachers, 'class_name': class_name})


def timetable_view(request):
    # Fetch all timetable entries ordered by day and period
    timetable_data = Timetable.objects.all().order_by('day_of_week', 'start_time')
    
    # Group timetable data by day of the week
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    timetable_by_day = {day: timetable_data.filter(day_of_week=day) for day in days}
    
    context = {
        'timetable_by_day': timetable_by_day,
    }
    return render(request, 'timetable/timetable.html', context)