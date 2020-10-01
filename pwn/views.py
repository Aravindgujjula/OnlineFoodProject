from django.contrib import messages
from django.shortcuts import render,redirect
from pwn.models import AdminLoginModel, StateModel, CityModel , CuisineModel
from vendor.models import VendorRegistrationModel
from pwn.otpsending import sendASMS

def showIndex(request):
    return render(request,"pwn/login.html")

def pwn_login_check(request):
    if request.method == "POST":
        try:
            admin = AdminLoginModel.objects.get(username=request.POST.get("pwn_username"),
                                                password=request.POST.get('pwn_password'))
            request.session["admin_status"] = True
            return redirect('welcome')
        except:
            return render(request, "pwn/login.html", {"error": "Invalid User"})

    else:
        request.session['admin_status'] = False
        return render(request, "pwn/login.html", {"error": "Admin logged out"})


def welcome(request):
    return render(request,"pwn/home.html")


def openstate(request):
    sm = StateModel.objects.all()
    return render(request, "pwn/openstate.html", {'data': sm})

def savestate(request):
    StateModel(name=request.POST.get('t1'),photo=request.FILES['t2']).save()
    messages.success(request,'state is saved')
    return openstate(request)


def updatestate(request):
    sid = request.GET.get('id')
    print(sid)
    sm = StateModel.objects.get(id=sid)
    sm_all = StateModel.objects.all()
    return render(request,'pwn/openstate.html',{'udata':sm, 'data': sm_all})


def updatestateid(request):
    StateModel.objects.filter(id=request.GET.get('sid')).update(name=request.POST.get('t1'),photo=request.FILES.get('t2'))
    return redirect('state')


def sdelete(request):
    StateModel.objects.filter(id=request.GET.get('sid')).delete()
    messages.success(request,'state deleted')
    return redirect('state')



def opencity(request):
    return render(request, "pwn/opencity.html", {"s_data": StateModel.objects.all(), "c_data": CityModel.objects.all()})

def savecity(request):
    CityModel(name=request.POST.get("c1"),photo=request.FILES['c2'],city_state_id=request.POST.get("c3")).save()
    return opencity(request)


def opencusine(request):
    return render(request,'pwn/opencusine.html',{"c_data":CuisineModel.objects.all()})


def savecusine(request):
    CuisineModel(type=request.POST.get("c1"),photo=request.FILES['c2']).save()
    return opencusine(request)


def openvendor(request):
    return render(request,'pwn/openvendor.html',{"pending":VendorRegistrationModel.objects.filter(status="pending"),"approved":VendorRegistrationModel.objects.filter(status="approved"),"cancelled":VendorRegistrationModel.objects.filter(status="cancelled")})


def pwn_vendor_approve(request):
    res = VendorRegistrationModel.objects.get(id=request.GET.get("idno"))
    sname = res.stall_name
    cno=res.contact_1
    res.status = 'approved'
    res.save()
    sendASMS(str(cno),"Hello "+sname+"! \n We are happy to inform that your registration is approved")
    return openvendor(request)


def pwn_vendor_cancel(request):
    result = VendorRegistrationModel.objects.get(id=request.GET.get("idno"))
    sname = result.stall_name
    cno = result.contact_1
    result.status = 'cancelled'
    result.save()
    sendASMS(str(cno), "Hello " + sname + "! \n We are sorry to inform that your registration is Cancelled")
    return openvendor(request)


def openreports(request):
    return render(request,'pwn/openreports.html')

