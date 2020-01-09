
from django.shortcuts import render, redirect,HttpResponseRedirect,render_to_response

from django.db.models import Q
from django.http import  JsonResponse, request
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from  django.http import HttpResponse 
from . import models
import sqlite3,json

import pandas as pd
from django.db.models import Count
from Tools.scripts.objgraph import flat
from django.http.request import QueryDict, HttpRequest


from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.core.exceptions import ObjectDoesNotExist



from django.http.response import HttpResponseRedirect
from rest_framework.request import Request
from django.template import  RequestContext


def nkang(request):
    return render(request,'vasuapp/nkang.html')
def Home(request):
    return render(request,'vasuapp/Home.html')

def tlogin(request):
    print("in LOGGGGGGGGGGGGGGGG")
    if request.method == "POST":
       usr = request.POST['username'] 
       pwd = request.POST['password']
       user =auth.authenticate(username=usr,password=pwd)
       if user is not None:
           auth.login(request, user)
           return redirect('/main')
       else:
           messages.error(request,"User Name or Password Does not Match")
       return render(request,"Home.html")    
       
       
def ibmcs90Home(request):
    dmname=models.StaffingMaster.objects.values('DMName').distinct()
#    print(dmname)
    
    return render(request,'vasuapp/ibmcs90home.html',{'dmn':dmname})
    #return render(request,'vasuapp/.html',{'dmn':dmname})
def Hellow(request):
    return render(request,'vasuapp/hallow.html')

def Empview(request):
    employees=models.Employee.objects.all()
    return render(request,'vasuapp/empview.html',{'employees':employees})


def ICS90Empview(request):
    #query1= request.POST["ddsel"]
    #print("Query one is : ",query1)
    employees=models.StaffingMaster.objects.all().order_by('DMName')
    ba=models.StaffingMaster.objects.values('BudgetArea').annotate(cnt=Count('BudgetArea'))
    data = list(employees)
    myowndict = {
        'employees':employees,
        'ba':ba
    }
    print("From ICS90EMPView :::: ")
    print(data)
    x=request.POST.get('idmn') 
    print("in ICS90 View ::::: Murali : ",x)    
   
    return render(request,'vasuapp/cs90Staff.html',myowndict)
  
def nkredirect():
    print ("Murali I am here")
    
def CS90Empview(request):
    print ("Murali I am here")        
    #print("Murali : ",kwargs.Get("slug"))
    if request.method == 'POST':
        print("POST")
        #pd=request.POST["Nkoption"]
        st= request.POST.get("Dnm")
    else:
        print("GET")    
        st=request.session.get('dname')
    print("989898 ::::",st)
    if st == "allData":
       return redirect('/cs90')
     
    employees=models.StaffingMaster.objects.order_by("BudgetArea").filter(DMName=st)
    print("MNMNNMMMMM",list(employees))
    ba=models.StaffingMaster.objects.values('BudgetArea').annotate(cnt=Count('BudgetArea')).filter(DMName=st)
    print (ba)  
    myowndict = {
        "employees":employees,
        "dm":1,
        "dm_name":st,
        'ba':ba
        }
    print("Print Dictionary Now Be ready")
    print (type(myowndict))
    print("Printeddddddddddd Dictionary Now Be ready")
    #return HttpResponse(json.dumps(myowndict), content_type='application/json')
    #return JsonResponse(json.dumps(list(myowndict)))
    #return redirect('http://127.0.0.1:8000/myredirect')
    #return redirect('myredirect/',permanent=True)
    #return HttpResponseRedirect('myredirect/')
    #return render_to_response('vasuapp/cs90Staff.html',myowndict,context_instance=RequestContext(request))
    return render(request,'vasuapp/cs90Staff.html',myowndict)

def myredirect(request):
    print('in Mydict')
    return render(request,'vasuapp/Home.html')
 
def CS90EmpviewBack(request,st):
           
    #print("Murali : ",kwargs.Get("slug"))
    print("Fetching in CS90 View for ::::: Murali : ",st)   
    employees=models.StaffingMaster.objects.order_by("BudgetArea").filter(DMName=st)
    print("MNMNNMMMMM",list(employees))
    ba=models.StaffingMaster.objects.values('BudgetArea').annotate(cnt=Count('BudgetArea')).filter(DMName=st)
    print (ba)  
    myowndict = {
        "employees":employees,
        "dm":1,
        "dm_name":st,
        'ba':ba
        }
    print (myowndict)
    return render(request,'vasuapp/cs90Staff.html',myowndict)

def AngCS90Empview(request):
        
    #print("Murali : ",kwargs.Get("slug"))
    st=request.POST['dmn'] 
    print("in CS90 View ::::: Murali : ",st)   
    employees=models.StaffingMaster.objects.order_by("BudgetArea").filter(DMName=st)
    
    dmname=models.StaffingMaster.objects.values('DMName').distinct()
    ba=models.StaffingMaster.objects.values('BudgetArea').annotate(cnt=Count('BudgetArea')).filter(DMName=st)
    print (ba)  
    myowndict = {
        "employees":employees,
        "dm":1,
        "dm_name":st,
        'dmn':dmname,
        'ba':ba
        }
    #print (myowndict)
    #return render(request,'vasuapp/cs90Staff.html',myowndict)    
    return HttpResponse(json.dumps(list(myowndict)), content_type='application/json')
    
def index(request):
    for i in request.POST.keys():
            print('murali','key: {0} value: {1}'.format(i, request.POST[i]))
    if "GET" == request.method:
        return render(request, 'vasuapp/index.html', {})
    else:
        excel_file = request.FILES["excel_file"]
        wb = pd.read_excel(excel_file,'WorkSheet')
         
        df= pd.DataFrame(wb)
        df=df[(df['SECTION']=='Active')]
        #df=df.drop([df.columns[9],df.columns[10],df.columns[11],df.columns[12]],axis=1)
        #6-Employee number, 2->Section, 11
        cols = [6,2,11,9,17,18,19,23]
        df = df[df.columns[cols]]
        exdd=df.to_dict('records')
#        print(exdd)
        stfmtx=df.values
        fs=0
        fs=Add2MasterStaff(stfmtx,fs)
        print("Sccess Files..................",fs)
        if fs==1:
            print("Sccess Files..................")
            msg={"msg":"Successfully Uploaded Data"}
        else:
            msg={"msg":"Problem with File"} 

        return render(request, 'vasuapp/index.html', msg)
def Add2MasterStaff(stfmtx,fs):    
    conn =sqlite3.connect('StaffingMaster.db')
    c=conn.cursor()
    dsql="delete from vasuapp_staffingmaster"
    c.execute(dsql)
    conn.commit
    print("The Data to be uploaded")
    print(stfmtx)
    insqry='INSERT INTO vasuapp_staffingmaster(Eno,Ename,DMName,BudgetArea,IBMMailID,OfficeNumber,MobileNumber,ClientMailID) values (?,?,?,?,?,?,?,?)'
    try:
        c.executemany(insqry,stfmtx)
        fs=1
        print("Loaded data")
    except:
        print("Problem with Data")
        pass    
    conn.commit()
    conn.close()
    return(fs)
    
def SrchView(request):
    query1= request.POST["srchinput"]
    query= request.GET.get("srchinput","murali")
    print("Murali in SRCH ::: ",query,"Query 2",query1)
    lookups= Q(Eno__icontains=query1) | Q(Ename__icontains=query1) | Q(IBMMailID__icontains=query1) | Q(ClientMailID__icontains=query1) 
    employees= models.StaffingMaster.objects.filter(lookups).distinct()
    return render(request,'vasuapp/hallow.html',{"employees":employees})

def getdmnames(request):
    x=request.POST.get('x') 
    print("::::::::::I am in getdmnames:::::::::::::::",x)
    dmname=models.StaffingMaster.objects.values('DMName').distinct()
    dmbudget=models.StaffingMaster.objects.order_by('DMName').values_list('DMName','BudgetArea')
    x=dmbudget.values('DMName','BudgetArea')
    dbdf=pd.DataFrame.from_records(x)
    dbdf=dbdf.drop_duplicates();
    #print("eeeeeeeeeeeeeeeeeeekkkkkkkkkkkk: ",dbdf)
    dbf=list(dbdf.groupby(['DMName']))
    dbdd=dict(dbf)
    dmdict=dbdf.groupby('DMName')['BudgetArea'].apply(lambda g:g.values.tolist()).to_dict()
           
    
    
    data = json.dumps(list(dmname))
    print('dmname::::',data)
    #data = json.dumps(dmname)
    #print("k88888888kkkkkkkkkkk: ",data)
    #json_data=serialize('json', [dmname,])
    #print("kkkkkkkkkkkk--kkkk: ",json_data)
    return HttpResponse(data, content_type='application/json')
   
def getAppNames(request):

    #ap=request.POST.get('ap') 
    print("::::::::::I am in Get APP Name :::::::::::::::")
    #ba=models.StaffingMaster.objects.values('BudgetArea').distinct()
    ba=models.StaffingMaster.objects.values('BudgetArea','DMName').distinct()
    #data = json.dumps(ba)
    m1={}
    data = list(ba)
    print('lklk---------------',data)
    for e in data:
        v=e['BudgetArea']
        k=e['DMName']
        m1.setdefault(k,[]).append(v)

    #print("Loop Starting...........")             
    #for k,vl in m1.items():
    #    for v in vl:
    #        print(k,"----",v) 
    return HttpResponse(json.dumps(m1), content_type='application/json')
    #return JsonResponse(data, content_type='application/json')



def getEmpAppwise(request):
    
    st= request.POST.get("barea")
    st1= request.POST.get("dnm")
    print("Fetching in CS90 View for ::::: Murali : ",st,"===",st1)
    if st1 is not None:
       request.session['dname']=st1  
       return redirect('/cs90a')
       
    if st == 'allData':
       return redirect('/cs90')
    else:    
       employees=models.StaffingMaster.objects.order_by("BudgetArea").filter(BudgetArea=st)
       ba=models.StaffingMaster.objects.values('BudgetArea').annotate(cnt=Count('BudgetArea')).filter(BudgetArea=st)
    print (ba)  
    myowndict = {
        "employees":employees,
        "dm":1,
        "dm_name":st,
        'ba':ba
        }
    print (myowndict)
    return render(request,'vasuapp/cs90Staff.html',myowndict)
    


def EnoEname(request):
    cs90data=models.StaffingMaster.objects.values("Eno","Ename")
#    print(cs90data)
    #data = json.dumps(list(cs90data))
    #return JsonResponse(data, safe=False) 
    return HttpResponse(json.dumps(list(cs90data)), content_type='application/json')  