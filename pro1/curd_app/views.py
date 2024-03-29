from django.shortcuts import render, redirect
from .forms import SchoolForm
from .models import School
from django.http import HttpResponse


def create_view(request):
    template_name = "curd_app/create.html"
    form = SchoolForm()
    if request.method == "POST":
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("order successfully!!!")
    context = {"form": form}
    return render(request, template_name, context)


def show_view(request):
    template_name = "curd_app/show.html"
    obj = School.objects.all()
    context = {"obj": obj}
    return render(request, template_name, context)


def updated_view(request, pk):
    template_name = "curd_app/create.html"
    obj = School.objects.get(id=pk)
    form = SchoolForm()
    if request.method == "POST":
        form = SchoolForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {"form": form}
    return render(request, template_name, context)


def cancel_view(request, pk):
    template_name = "curd_app/confirm.html"
    obj = School.objects.get(id=pk)
    form = SchoolForm(instance=obj)
    if request.method == "POST":
        obj.delete()
        return redirect("show_url")
    return render(request, template_name)



