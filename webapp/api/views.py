from django.shortcuts import render
from django.http import HttpResponse
import json
import datetime
import random
import string
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from authentication.models import *
#from privateviews.decorators import login_not_required
#from django.contrib.auth.decorators import login_required , login_not_required
from django.contrib.auth import authenticate
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
from product.models import WalletMoney,ReferralEmployee,Product,DashboardDetails
# Create your views here.
BASE_URL = "http://13.233.193.139/"

def index(request):
    return HttpResponse("hello")

#@login_not_required
@csrf_exempt
def auth(request):
    if request.body:
        resp={}
        payload = json.loads(request.body)
        username=payload['username']
        password=payload['password']
        apk_version = payload.get('app_version')
        newuser =authenticate(username=username, password=password)
        if newuser is None:
            resp['success']= False
            resp['message']= 'Invalid User'
            return HttpResponse(json.dumps(resp),content_type="application/json")
        else:
            emp=EmployeeMaster.objects.filter(user=newuser)
            now = datetime.datetime.now() + datetime.timedelta(days=1)
            if emp:
                emp=emp[0]
                s = SessionStore()
                s['user_id'] = emp.user_id
                s['expiry_date'] = str(now)
                s.save()
                mobile=emp.mobile_no
                name=str(emp.firstname)
                resp['success']=True
                resp['message'] = 'Logged in successfully'
                resp['name']=name
                resp['username']=mobile
                resp['session_key'] = s.session_key
                return HttpResponse(json.dumps(resp),content_type="application/json")
            else:
                resp['success']= False
                resp['message'] = 'Login Failed'
                return HttpResponse(json.dumps(resp),content_type="application/json")

def logged_in_user(session_key):
    now = datetime.datetime.now()
    sessionObj = Session.objects.get(session_key=session_key)

    if not sessionObj:
        return {"success":False,"message":"Invalid Session"}

    user_id_obj = sessionObj.get_decoded()

    #if now >= user_id_obj["expiry_date"]:
     #   return {"success":False,"message":"Session Expired."}

    user_id = {}
    user_id["success"] = True
    user_id["message"] = user_id_obj["user_id"]
    return user_id

@csrf_exempt
def walletmoney_show(request):
    if not request.method == "POST":
        return {"success":False,"message":"Invalid Method in REQUEST HEADER."}
    if request.method == "POST":
        payload = request.body
        payload = payload.replace('\ "',"")
        if not payload:
            return {"success":False,"message":"Payload should be in JSON Format"}
    payload = json.loads(payload)

    if "session_key" not in payload:
        return {"success":False,"message":"Missing session_key in REQUEST."}

    session_key = payload["session_key"]

    user_id = logged_in_user(session_key)
    if user_id["success"] == False:
        return user_id

    emp = EmployeeMaster.objects.get(user_id=user_id["message"])
    walletmoney = emp.walletmoney.all()
    data = []
    total = 0
    for detail in walletmoney:
        dic = {}
        value = detail.value
        total = total + int(value)
        dic['money'] = value
        dic['date'] = str(detail.added_on.date())
        dic['status'] = detail.status
        data.append(dic)
    response = {}
    response["success"] = True
    response["message"] = "success"
    response["total_money"] = total
    response["data"] = data
    payload_data = json.dumps(response)
    return HttpResponse(payload_data)
 
    

@csrf_exempt
def user_registraion(request):
    if not request.method == "POST":
        return HttpResponse(json.dumps({"success":False,"message":"Invalid Method in REQUEST HEADER."}))
    if request.method == "POST":
        payload = request.body
        payload = payload.replace('\ "',"")
        if not payload:
            return HttpResponse(json.dumps({"success":False,"message":"Payload should be in JSON Format"}))
    payload = json.loads(payload)
    if "firstname" not in payload:
        return HttpResponse(json.dumps({"success":False,"message":"Missing firstname in REQUEST."}))
    if "mobile" not in payload:
        return HttpResponse(json.dumps({"success":False,"message":"Missing mobile in REQUEST."}))
    if "password" not in payload:
        return HttpResponse(json.dumps({"success":False,"message":"Missing password in REQUEST."}))
   
    firstname = payload['firstname']
    lastname = payload.get('lastname')
    mobile = payload['mobile']
    password = payload['password']
    referral_code = payload.get('referral_code')

    try:
        mobile = int(mobile)
    except:
        return HttpResponse(json.dumps({"success":False,"message":"Invalid Mobile number"}))

    if not password:
        return HttpResponse(json.dumps({"success":False,"message":"Please Enter Password"}))
    emp_check = EmployeeMaster.objects.filter(user__username = mobile)
    if emp_check:
        return HttpResponse(json.dumps({"success":False,"message":"Already Exist"}))
    referral_flag = 0
    if referral_code:
        referral_emp_check = EmployeeMaster.objects.filter(refferal_code = str(referral_code))
        if not referral_emp_check:
            return HttpResponse(json.dumps({"success":False,"message":"Invalid Referral Code"}))
        else:
            referral_flag = 1
            referral_user = referral_emp_check[0]

    total_emp = EmployeeMaster.objects.filter().order_by("-id")[:1]
    emp_code = str(int(total_emp[0].id) + 1)
    employee_code = str(emp_code) + ("".join([random.choice(string.digits) for x in range(1, 6 - int(len(emp_code)))]))

    user_ch = User.objects.filter(username=mobile)
    if user_ch:
        user = user_ch[0]
    else:
        user = User.objects.create_user(username=mobile,first_name=firstname)

    referral_code = str(employee_code)
    dep = Department.objects.get(name="Operations")
    emp = EmployeeMaster.objects.create(user=user, employee_code=employee_code, firstname=firstname,lastname=lastname, email="", address1="", address2="",mobile_no=mobile,refferal_code=referral_code,user_type="User",department=dep)
    user.set_password(str(password))
    user.save()
    now = datetime.datetime.now() + datetime.timedelta(days=1)
    s = SessionStore()
    s['user_id'] = emp.user_id
    s['expiry_date'] = str(now)
    s.save()

    user_wallet_money = random.randint(150,200)
    if referral_flag == 1:
        exist_name = referral_user.firstname
        exist_code = referral_user.employee_code
        referralemp = ReferralEmployee.objects.create(name_referral_by = exist_name ,name_referral_to = firstname ,code_referral_by = exist_code ,code_referral_to = employee_code)
        WalletMoney.objects.create(employee_code = emp ,referralemployee = referralemp , value = user_wallet_money)
        WalletMoney.objects.create(employee_code = emp ,referralemployee = referralemp , value = 100)
        WalletMoney.objects.create(employee_code = referral_user ,referralemployee = referralemp , value = 100)
    else:
        WalletMoney.objects.create(employee_code = emp , value = user_wallet_money)
    resp = {}
    resp['success']=True
    resp['message'] = 'Logged in successfully'
    resp['name'] = firstname
    resp['username'] = mobile
    resp['session_key'] = s.session_key
    return HttpResponse(json.dumps(resp),content_type="application/json")
    #return HttpResponse(json.dumps({"success":True,"message":"Successfully Registered"}))

@csrf_exempt
def product_list(request):
    if not request.method == "POST":
        return {"success":False,"message":"Invalid Method in REQUEST HEADER."}
    if request.method == "POST":
        payload = request.body
        payload = payload.replace('\ "',"")
        if not payload:
            return {"success":False,"message":"Payload should be in JSON Format"}
    payload = json.loads(payload)

    if "session_key" not in payload:
        return {"success":False,"message":"Missing session_key in REQUEST."}

    session_key = payload["session_key"]
    product_type = payload.get("product_type")
    ideal_for = payload.get("ideal_for")
    brand_name = payload.get("brand_name")

    user_id = logged_in_user(session_key)
    if user_id["success"] == False:
        return user_id

    emp = EmployeeMaster.objects.get(user_id=user_id["message"])
    data = []
    total = 0
    q = Q()
    if ideal_for:
        q = Q(ideal_for = ideal_for)
    elif product_type:
        q = Q(product_type = product_type)
    elif brand_name:
        q = Q(brand_name__name = brand_name)
    else:
        pass 
    product = Product.objects.filter(q)
    for p in product:
        dic = {}
        dic['id'] = p.id
        dic['product_size'] = {}
        dic['name'] = p.name
        dic['model_name'] = str(p.model_name)
        dic['warranty'] = p.warranty
        dic['description'] = p.description
        dic['orignal_price'] = p.orignal_price
        if p.offer_discount.status==0:
            dic['actual_price'] = p.actual_price
            dic['discount'] = p.discount
        else:
            discount = p.offer_discount.discount
            dis_amount = int(p.orignal_price) * int(discount)
            discount_amount = dis_amount/100
            actual_amount = int(p.orignal_price) - int(discount_amount)
            dic['actual_price'] = int(actual_amount)
            dic['discount'] = int(p.offer_discount.discount)
        dic['brand_name'] = p.brand_name.name
        dic['product_size']['size_from'] = p.product_size.size_from
        dic['product_size']['size_to'] = p.product_size.size_to
        dic['product_size']['size_name'] = p.product_size.name
        colors_name = p.color.all()
        color_list = []
        for i in colors_name:
            color_list.append(str(i.name))
        dic['color_availeble'] = color_list
        dic['ideal_for'] = str(p.ideal_for)
        dic['product_type'] = str(p.product_type)
        dic['image'] = str(BASE_URL+"static"+str(p.image.url))
        data.append(dic)
    response = {}
    response["success"] = True
    response["message"] = "success"
    response["data"] = data
    payload_data = json.dumps(response)
    return HttpResponse(payload_data)

@csrf_exempt
def dashboard_details(request):
    if not request.method == "POST":
        return {"success":False,"message":"Invalid Method in REQUEST HEADER."}
    if request.method == "POST":
        payload = request.body
        payload = payload.replace('\ "',"")
        if not payload:
            return {"success":False,"message":"Payload should be in JSON Format"}
    payload = json.loads(payload)

    if "session_key" not in payload:
        return {"success":False,"message":"Missing session_key in REQUEST."}

    session_key = payload["session_key"]
    product_type = payload.get("product_type")
    ideal_for = payload.get("ideal_for")
    brand_name = payload.get("brand_name")

    user_id = logged_in_user(session_key)
    if user_id["success"] == False:
        return user_id

    emp = EmployeeMaster.objects.get(user_id=user_id["message"])
    details = DashboardDetails.objects.all()[0]
    
    dic = {}
    if details.dashboard_image1:
        dic['dashboard_img1'] = str(BASE_URL+"static"+str(details.dashboard_image1.url))
    else:
        dic['dashboard_img1'] = ""
    if details.dashboard_image2:
        dic['dashboard_img2'] = str(BASE_URL+"static"+str(details.dashboard_image2.url))
    else:
        dic['dashboard_img2'] = ""
    if details.dashboard_image3:
        dic['dashboard_img3'] = str(BASE_URL+"static"+str(details.dashboard_image3.url))
    else:
        dic['dashboard_img3'] = ""
    if details.dashboard_image4:
        dic['dashboard_img4'] = str(BASE_URL+"static"+str(details.dashboard_image4.url))
    else:
        dic['dashboard_img4'] = ""
    dic['dashboard_img5'] = ""
    if details.referral_image:
        dic['referral_img'] = str(BASE_URL+"static"+str(details.referral_image.url))
    else:
        dic['referral_img'] = ""
    prod_details = details.producttype_set.all()
    prod_data = []
    if prod_details:
        for i in prod_details:
            dic2 = {}
            dic2['name'] = i.name
            dic2['id'] = i.id
            dic2['image'] = str(BASE_URL+"static"+str(i.image.url))
            prod_data.append(dic2)
    dic['product_category'] = prod_data
    brand = details.brandname_set.all()
    brand_data = []
    if brand:
        for i in brand:
            dic3 = {}
            dic3['name'] = i.name
            dic3['id'] = i.id
            dic3['image'] = str(BASE_URL+"static"+str(i.image.url))
            brand_data.append(dic3)

    dic['brand_category'] = brand_data

    response = {}
    response["success"] = True
    response["message"] = "success"
    response["data"] = dic
    payload_data = json.dumps(response)
    return HttpResponse(payload_data)
    

