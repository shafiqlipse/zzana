from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login
from accounts.decorators import school_required, anonymous_required, staff_required
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.db import IntegrityError
@login_required
def edit_user(request, id=None):
    if id:
        # Fetch the user to edit by their ID
        user = get_object_or_404(User, id=id)
    else:
        # Default to the logged-in user if no ID is provided
        user = request.user

    if request.method == "POST":
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "The profile was updated successfully.")
            return redirect("edit_user", user_id=user.id)
    else:
        form = UserEditForm(instance=user)

    return render(request, "accounts/edit_user.html", {"form": form, "id": user.id})



# Create your views here.
@anonymous_required
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if user.is_school:
                messages.success(request, "School login successful.")
                return redirect("schooldash")
            elif user.is_admin:
                messages.success(request, "Officer login successful.")
                return redirect("dashboard")
            else:
                messages.success(request, "Login successful.")
                return redirect(
                    "dashboard"
                )  # Adjust the URL name for your dashboard view
        else:
            messages.error(request, "Error in login. Please check your credentials.")
    else:
        form = AuthenticationForm()
    return render(request, "auth/login.html", {"form": form})


def user_logout(request):
    # if user.is_authenticated:
    logout(request)
    return redirect("login")


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Update the session to maintain the user's login status
            update_session_auth_hash(request, user)
            messages.success(request, "Your password was successfully updated!")
            return redirect("success")
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "auth/change_password.html", {"form": form})


def Confirm(request):

    return render(request, "accounts/confirm.html")


def custom_404(request, exception):
    return render(request, "auth/custom404.html", {}, status=404)




class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = "auth/password_reset.html"
    email_template_name = "auth/password_reset_email.html"
    subject_template_name = "auth/password_reset_subject.txt"
    success_message = (
        "We've emailed you instructions for setting your password, "
        "if an account exists with the email you entered. You should receive them shortly."
        " If you don't receive an email, "
        "please make sure you've entered the address you registered with, and check your spam folder."
    )
    success_url = reverse_lazy("home")


def success(request):
    return render(request, "accounts/success.html")


#+++++++++++++++++++++++++++++_________)))))))))))))(((((((((*************&&&&&&&&&^^^^^^^^^^^^^%)))))))))
#-------------------------------------------Visitors views------------------------------------------------

#+++++++++++++++++++++++++++++_________)))))))))))))(((((((((*************&&&&&&&&&^^^^^^^^^^^^^%)))))))))
def Notices(request):
    notices = Notice.objects.all()
    if request.user.is_authenticated:
        # Annotate notices with read status for the current user
        notices = notices.annotate(
            is_read=models.Exists(
                NoticeReadStatus.objects.filter(user=request.user, notice=models.OuterRef('id'), is_read=True)
            )
        )
    form = NoticesForm(request.POST or None, request.FILES or None)
    
    if request.method == "POST" and form.is_valid():
        try:
            new_notice = form.save(commit=False)
            # Assign values to `new_enrollment` before saving
            new_notice.author = request.user
            # For example: new_enrollment.user = request.user
            new_notice.save()
            messages.success(request, "Notice added successfully!")
            return redirect("notices")
        except IntegrityError:
            messages.error(request, "There was an error saving the enrollment.")
    context={"form": form,"notices":notices}
    return render(request, "notices/notices.html", context)

#+++++++++++++++++++++++++++++_________)))))))))))))(((((((((*************&&&&&&&&&^^^^^^^^^^^^^%)))))))))
from django.utils.timezone import now
def Notice_detail(request, id):
    notice = get_object_or_404(Notice, id=id)

    # Update or create read status for the current user
    if request.user.is_authenticated:
        read_status, created = NoticeReadStatus.objects.get_or_create(user=request.user, notice=notice)
        if not read_status.is_read:
            read_status.is_read = True
            read_status.read_at = now()
            read_status.save()
    return render(request, 'notices/notice.html', {'notice': notice})



#+++++++++++++++++++++++++++++_________)))))))))))))(((((((((*************&&&&&&&&&^^^^^^^^^^^^^%)))))))))
#-------------------------------------------Visitors views------------------------------------------------

#+++++++++++++++++++++++++++++_________)))))))))))))(((((((((*************&&&&&&&&&^^^^^^^^^^^^^%)))))))))
def Visitors(request):
    visitors = Visitor.objects.all()
    form = VisitorsForm(request.POST or None, request.FILES or None)
    
    if request.method == "POST" and form.is_valid():
        try:
            new_visitor = form.save(commit=False)
            # Assign values to `new_enrollment` before saving
            new_visitor.recorder = request.user
            # For example: new_enrollment.user = request.user
            new_visitor.save()
            messages.success(request, "visitor added successfully!")
            return redirect("visitors")
        except IntegrityError:
            messages.error(request, "There was an error saving the enrollment.")
    context={"form": form,"visitors":visitors}
    return render(request, "visitors/visitors.html", context)








#+++++++++++++++++++++++++++++_________)))))))))))))(((((((((*************&&&&&&&&&^^^^^^^^^^^^^%)))))))))
#-------------------------------------------Complaints views------------------------------------------------
#+++++++++++++++++++++++++++++_________)))))))))))))(((((((((*************&&&&&&&&&^^^^^^^^^^^^^%)))))))))
def Complaints(request):
    complaints = Complaint.objects.all()
    form = ComplaintsForm(request.POST or None, request.FILES or None)
    
    if request.method == "POST" and form.is_valid():
        try:
            new_complaint = form.save(commit=False)
            # Assign values to `new_enrollment` before saving
            new_complaint.recorder = request.user
            # For example: new_enrollment.user = request.user
            new_complaint.save()
            messages.success(request, "Complained added successfully!")
            return redirect("complaints")
        except IntegrityError:
            messages.error(request, "There was an error saving the enrollment.")
    context={"form": form,"complaints":complaints}
    return render(request, "complaints/complaints.html", context)