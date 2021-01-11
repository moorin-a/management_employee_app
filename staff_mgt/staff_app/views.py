from django.shortcuts import render, redirect
from .forms import StaffForm
from .models import Staff


# Create your views here.
def index(request):
	data = Staff.objects.all()
	params = {
		'title': '社員管理',
		'data': data,
	}
	return render(request, 'staff_app/index.html', params)

# create mode
def create(request):
	params = {
		'title': '社員管理',
		'form' : StaffForm()
	}
	if (request.method=='POST'):
		obj = Staff()
		person = StaffForm(request.POST, obj)
		person.save()
		return redirect(to='/staff')
	return render(request, 'staff_app/create.html', params)

# edit mode
def edit(request, num):
	obj = Staff.objects.get(id=num)
	if (request.method=='POST'):
		person = StaffForm(request.POST, instance=obj)
		person.save()
		return redirect(to='/staff')
	params = {
		'title': '社員管理',
		'id': num,
		'form': StaffForm(instance=obj)
	}
	return render(request, 'staff_app/edit.html', params)

def delete(request, num):
	person = Staff.objects.get(id=num)
	if (request.method=='POST'):
		person.delete()
		return redirect(to='/staff')
	params = {
		'title': '社員管理',
		'id': num,
		'obj': person
	}
	return render(request, 'staff_app/delete.html', params)