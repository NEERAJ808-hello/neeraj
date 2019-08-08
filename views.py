from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import UpdateView

from .models import users, MyNotes
# from django.views.generic import CreateView

# Create your views here.
def index(request):
    return render(request, 'index.html', {'no': 'no'})

def login(request):
    return render(request, 'index.html', {'login':"login_try"})


def signUp(request):
    return render(request, 'index.html', {'userRegistration': "start_user_registration"})


def checkLogin(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        data = users.objects.filter(name=un, password=up)
        print(data)
        if data:
            return render(request, 'index.html', {'login_yes': un})
        else:
            return render(request, 'index.html', {'login_no': "Error while Logging...!!!"})

        # if data:
        #     return render(request, 'index.html', {'username:' })

    #     try:
    #         users.objects.get(name=un, password=up)
    #         # carry = request.session.__setitem__('user', un)
    #         return render(request, 'index.html', {'login_yes': un})
    #     except:
    #         return render(request, 'index.html', {'login_no': 'unsuccessful loggin'})
    # return render(request, 'index.html')


def addNote(request):
    user = request.session.__getitem__('user')
    return render(request, 'index.html', {'user': user, 'noteentrypage': 'entrypage'})


def saveNote(request):
    n = request.POST.get("notes")
    print(n)
    MyNotes(note=n).save()
    mynotes = MyNotes.objects.all()
    return render(request, 'index.html', {'havenotes': "yes", 'mynotes': mynotes})

def showAllNotes(request):
    query = MyNotes.objects.all()
    return render(request, 'index.html', {'query': query})

def userResigration(request):
    un = request.POST.get("uname")
    mn = request.POST.get("mobile")
    up = request.POST.get("upass")
    users(name=un, mobile=mn, password=up).save()
    return render(request, 'index.html', {'u_reg_success': "User Registration Successfull"})

def addUser(request):
    return render(request, 'index.html', {'adduser':True})


def logOut(request):
    return render(request, 'index.html', {'no': 'no'})




def update(request, id):
    update = MyNotes.objects.get(id=id)
    id = update.id
    return render(request, 'index.html', {'updatenow': id})


def updatenow(request, id):
    val = request.POST.get("notes")
    MyNotes(id=id, note=val).save()

    return render(request, 'index.html', {'query': MyNotes.objects.all()})


def deletenow(request, id):
    MyNotes(id=id).delete()
    return render(request, 'index.html', {'query': MyNotes.objects.all()})


def searchUser(request):
    return render(request, 'index.html', {'search': MyNotes.objects.all()})


def search(request):
    get = request.POST.get("search")
    data = MyNotes.objects.filter(name=get)
    if data:
        return render(request, 'index.html', {'data': data.all()})
    return render(request, 'index.html')


def searchByName(request):
    get = request.POST.get("search")
    data = MyNotes.objects.filter(name=get)
    if data:
        return render(request, 'index.html', {'data': "User is available"})
    else:
        return render(request, 'index.html', {'data': "User is not available"})


def searchByMobile(request):
    get = request.POST.get("search")
    data = MyNotes.objects.filter(id=get)
    if data:
        return render(request, 'index.html', {'data': "User is available"})
    else:
        return render(request, 'index.html', {'data': "User is not available"})
