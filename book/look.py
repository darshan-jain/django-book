from django.shortcuts import render ,HttpResponseRedirect
from .forms import BookRegistration
from .models import Book

# Create your views here.

# This function would  add and display the Book
def add_show(request):
    if request.method == 'POST':
        fm = BookRegistration(request.POST)
        if fm.is_valid():
            nm =fm.cleaned_data['bookname']
            em =fm.cleaned_data['author']
            pw =fm.cleaned_data['price']
            reg = Book(bookname=nm,author=em,price=pw)
            reg.save()
            fm = BookRegistration()
           
    else:
          fm = BookRegistration()
    stud = Book.objects.all()
    return render(request,'book/addandshow.html',{'form':fm,'stu':stud})


    # This function would delete the Book
def delete_data(request,id):
    if request.method =='POST':
        pi = Book.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/book/')

 #this function will update and edit
 #    
def update_data(request,id):
    if request.method == 'POST':
        pi = Book.objects.get(pk=id)
        fm=BookRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi =  Book.objects.get(pk=id)
        fm=BookRegistration(instance=pi)
    return render(request,'book/updateBook.html',{'form':fm})

