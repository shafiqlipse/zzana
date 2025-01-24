import base64
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.db import IntegrityError
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url="login")
def Departments(request):
    departments = Department.objects.all()
    form_errors = None  # To capture errors if the form is invalid

    if request.method == "POST":
        form = DepartmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            form_errors = form.errors  # Capture form errors
    else:
        form = DepartmentForm()

    context = {
        "form": form,
        "departments": departments,
        "form_errors": form_errors,
    }
    return render(request, "departments/departments.html", context)


@login_required(login_url="login")
def department_delete(request, id):
    stud = Department.objects.get(id=id)
    if request.method == "POST":
        stud.delete()
        return redirect("departments")

    return render(request, "departments/delete_department.html", {"obj": stud})

# Create your views here.


@login_required(login_url="login")
def Designations(request):
    designations = Designation.objects.all()
    form_errors = None  # To capture errors if the form is invalid

    if request.method == "POST":
        form = DesignationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            form_errors = form.errors  # Capture form errors
    else:
        form = DesignationForm()

    context = {
        "form": form,
        "designations": designations,
        "form_errors": form_errors,
    }
    return render(request, "designations/designations.html", context)


@login_required(login_url="login")
def designation_delete(request, id):
    stud = Designation.objects.get(id=id)
    if request.method == "POST":
        stud.delete()
        return redirect("designations")

    return render(request, "designations/delete_designation.html", {"obj": stud})

# Create your views here.


@login_required(login_url="login")
def Roles(request):
    roles = Role.objects.all()
    form_errors = None  # To capture errors if the form is invalid

    if request.method == "POST":
        form = RoleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            form_errors = form.errors  # Capture form errors
    else:
        form = RoleForm()

    context = {
        "form": form,
        "roles": roles,
        "form_errors": form_errors,
    }
    return render(request, "roles/roles.html", context)


@login_required(login_url="login")
def role_delete(request, id):
    stud = Role.objects.get(id=id)
    if request.method == "POST":
        stud.delete()
        return redirect("roles")

    return render(request, "roles/delete_role.html", {"obj": stud})


@login_required(login_url="login")
def employees(request):
    form_errors = None  # To capture errors if the form is invalid

    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            employee = form.save(commit=False)  # Create an instance to modify
            cropped_data = request.POST.get("photo_cropped")
            employee.added_by = request.user  # Set added_by to the current user

            if cropped_data:
                try:
                    # Extract and decode the base64 image data
                    format, imgstr = cropped_data.split(";base64,")
                    ext = format.split("/")[-1]
                    data = ContentFile(base64.b64decode(
                        imgstr), name=f"photo.{ext}")
                    employee.photo = data  # Assign cropped image
                except (ValueError, TypeError) as e:
                    messages.error(request, "Invalid image data.")
                    return render(request, "enrollments/enrollment_new.html", {"form": form})

            employee.save()  # Save the employee object
            messages.success(request, "Employee added successfully!")
            return redirect("employees")  # Replace with actual success URL
        else:
            form_errors = form.errors  # Capture form errors
    else:
        form = EmployeeForm()

    context = {
        "form": form,
        "form_errors": form_errors,  # Pass form errors to the template if needed
    }
    return render(request, "Staff/add_staff.html", context)


@login_required(login_url="login")
def staff_details(request, id):
    employee = get_object_or_404(Employee, id=id)
    context = {
        "employee": employee
    }
    return render(request, "Staff/staff.html", context)


@login_required(login_url="login")
def staff_delete(request, id):
    stud = Role.objects.get(id=id)
    if request.method == "POST":
        stud.delete()
        return redirect("employees")

    return render(request, "Staff/delete_staff.html", {"obj": stud})


@login_required(login_url="login")
def all_employees(request):
    allemployees = Employee.objects.all()
    context = {"allemployees": allemployees}
    return render(request, 'Staff/all_employees.html', context)

# =====================================Teacher views===================================

@login_required(login_url="login")
def teachers(request):
    form_errors = None  # To capture errors if the form is invalid
    allteachers = Teacher.objects.all()
    if request.method == "POST":
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            teacher = form.save(commit=False)  # Create an instance to modify
            cropped_data = request.POST.get("photo_cropped")
            teacher.added_by = request.user  # Set added_by to the current user

            if cropped_data:
                try:
                    # Extract and decode the base64 image data
                    format, imgstr = cropped_data.split(";base64,")
                    ext = format.split("/")[-1]
                    data = ContentFile(base64.b64decode(
                        imgstr), name=f"photo.{ext}")
                    teacher.photo = data  # Assign cropped image
                except (ValueError, TypeError) as e:
                    messages.error(request, "Invalid image data.")
                    return render(request, "enrollments/enrollment_new.html", {"form": form})

            teacher.save()  # Save the teacher object
            messages.success(request, "Teacher added successfully!")
            return redirect("teachers")  # Replace with actual success URL
        else:
            form_errors = form.errors  # Capture form errors
    else:
        form = TeacherForm()

    context = {
        "form": form,
        "allteachers": allteachers,
        "form_errors": form_errors,  # Pass form errors to the template if needed
    }
    return render(request, "Teacher/add_teacher.html", context)


@login_required(login_url="login")
def teacher_details(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    context = {
        "teacher": teacher
    }
    return render(request, "Teacher/teacher.html", context)


@login_required(login_url="login")
def teacher_delete(request, id):
    stud = Teacher.objects.get(id=id)
    if request.method == "POST":
        stud.delete()
        return redirect("teachers")

    return render(request, "Teacher/delete_teacher.html", {"obj": stud})


@login_required(login_url="login")
def all_teachers(request):
    allteachers = Teacher.objects.all()
    context = {"allteachers": allteachers}
    return render(request, 'Teacher/all_teachers.html', context)



# =====================================Leave views===================================
@login_required
def apply_leave(request):
    leaves = Leave.objects.filter(employee=request.user).order_by('-applied_on')
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.employee = request.user
            leave.save()
            messages.success(request, 'Your leave request has been submitted.')
            return redirect('leave_list')
    else:
        form = LeaveForm()
        
    context={'form': form,'leaves': leaves}
    return render(request, 'leave/leave_list.html', context)


from django.utils.timezone import now

@login_required
def review_leave(request, id):
    if not request.user.is_staff:  # Only admins or HR staff can review
        return redirect('leave_list')

    leave = Leave.objects.get(id=id)
    if request.method == 'POST':
        status = request.POST.get('status')
        if status in ['APPROVED', 'REJECTED']:
            leave.status = status
            leave.reviewed_on = now()
            leave.reviewed_by = request.user
            leave.save()
            messages.success(request, f'Leave request has been {status.lower()}.')
            return redirect('leave/leave_review_list')
    
    return render(request, 'leave/review_leave.html', {'leave': leave})


@login_required
def leave_review_list(request):
    if not request.user.is_staff:
        return redirect('leave_list')
    
    leaves = Leave.objects.all().order_by('-applied_on')
    return render(request, 'leave/leave_review_list.html', {'leaves': leaves})


# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from .models import Request, Staff
from .utils import get_next_approver  # utility function

    

@login_required
def create_request(request):
    if request.method == 'POST':
        description = request.POST['description']
        employee = Employee.objects.get(user=request.user)
        next_approver = get_next_approver(employee)
        Request.objects.create(
            requester=employee,
            description=description,
            current_approver=next_approver
        )
        return redirect('dashboard')
    return render(request, 'create_request.html')

from django.contrib.auth.decorators import user_passes_test

def is_approver(user):
    employee = Employee.objects.get(user=user)
    return employee.role.level <= 2  # Example: Only Headteachers and HODs can approve

@user_passes_test(is_approver)
def approve_request(request, request_id):
    req = get_object_or_404(Request, id=request_id)
    if request.method == 'POST':
        action = request.POST['action']
        if action == 'approve':
            req.status = 'Approved' if not req.next_approver else 'Pending'
            req.current_approver = req.next_approver
            req.next_approver = get_next_approver(req.current_approver)
        elif action == 'reject':
            req.status = 'Rejected'
        req.save()
        return redirect('approvals')
    return render(request, 'requests/approve_request.html', {'request': req})


def request_list_view(request):

    employee = get_object_or_404(Employee, user=request.user)

    if employee.role.level == 1:  # Headteacher can view all requests
            requests = Request.objects.all().order_by('-timestamp')
    else:
            # Requesters see their own requests; approvers see requests assigned to them
            requests = Request.objects.filter(
                models.Q(requester=employee) | models.Q(current_approver=employee)
            ).order_by('-timestamp')

    return render(request, 'requests/request_list.html', {'requests': requests})


# from django.core.mail import send_mail
from django.core.mail import send_mail
from django.http import JsonResponse
def create_user_from_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if employee.user:
        return JsonResponse({'status': 'error', 'message': 'User already exists for this employee.'}, status=400)

    # Create the User instance
    user = User.objects.create_user(
        username=employee.email.split('@')[0],
        email=employee.email,
        first_name=employee.fname,
        last_name=employee.lname,
        password='defaultpassword123'  # Default password; recommend prompting a change
    )

    # Associate the User with the Employee
    employee.user = user
    employee.save()

    # Send an email notification
    subject = 'Your Account Has Been Created'
    message = f"""
    Dear {employee.fname},

    Your account has been successfully created. 
    Please log in using the following credentials:

    Username: {user.username}
    Password: defaultpassword123 (please change your password immediately)

    Regards,
    Admin Team
    """
    send_mail(subject, message, 'admin@example.com', [employee.email])

    # Return a success alert as JSON response
    return JsonResponse({'status': 'success', 'message': f"User created successfully for {employee.fname} {employee.lname}."})