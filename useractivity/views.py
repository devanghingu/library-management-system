from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Profile
from .forms import ProfileForm,Change_passwordForm
# Create your views here.
class profileCBView(View):
    @method_decorator(login_required, name="dispatch")
    def get(self,request,*args, **kwargs):
        context = {"form": ProfileForm(instance=request.user.profile)}
        context["passwordform"] = Change_passwordForm(request.user)
        return render(request, "useractivity/myprofile.html", context)
    @method_decorator(login_required, name="dispatch")
    def post(self,request):
        profile_form = ProfileForm(request.POST or None,instance=request.user.profile)
        if profile_form.is_valid():
            user = profile_form.save(commit=False)
            user.user = request.user
            user.save()
            messages.success(request, "Profile Information Updated..!!")
            return redirect("profile")

        return render(request, "useractivity/myprofile.html",
                      {"form": profile_form})
@method_decorator(login_required, name="dispatch")
class ChangePasswordCBView(View):
    """ change_password url view """

    def post(self, request):
        """ change password when post req"""
        pass_chng_form = Change_passwordForm(request.user, request.POST)
        if pass_chng_form.is_valid():
            user = pass_chng_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password Was Successfully Updated..!!")
            return redirect("profile")
        else:
            messages.error(request, "Please Correct the error below.")
            context = {"form": ProfileForm(instance=request.user.profile)}
            context["passwordform"] = pass_chng_form
            context["passwordtab"] = "passwordtab"
        return render(request, "useractivity/myprofile.html", context)

