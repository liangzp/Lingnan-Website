# Create your views here.
from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
from django.utils.timezone import now
from my_app.models import User
from my_app.models import Application
from my_app.models import Classroom
import datetime
import numpy as np
import io
# Create your views here.

def testtemplate(request):
    string=u"你好"
    rightnow=now()
    response=HttpResponse()
    response.write(rightnow)
    response.write(string)
    return response
    #return HttpResponseRedirect(u'/my_app/login')

def login(request):
    string=u"登陆测试界面"
    submit=request.GET.get("submit", None)
    if submit=="failed":
        submitagain=True
    #elif submit==None:
    #    submitagain=False
    else:
        submitagain=False
    response=render(request, 'login.html', {'string': string,'submitagain':submitagain})
    return HttpResponse(response)

def loginsuccess(request):
    #string=u"你妈死了"
    uname=request.GET.get("uname", None)
    pwd=request.GET.get("password", None)
    #return HttpResponseRedirect(u'/my_app/testtemplate')
    if len(User.objects.filter(uname=uname))>0:
        validate=User.objects.filter(uname=uname)[0]
        if validate.pwd==pwd:
            if validate.role=="student":
                url="/my_app/managestu/"
                response=HttpResponseRedirect(url)
                response.set_cookie('username',uname,max_age=600)
                return  response
            else:
                url="/my_app/managetea/"
                response=HttpResponseRedirect(url)
                response.set_cookie('username',uname,max_age=600)
                return  response
        else:
            return HttpResponseRedirect(u'/my_app/login/?submit=failed')
    else:
        return HttpResponseRedirect(u'/my_app/login/?submit=failed')
    
def manage(request):
    if "username" in request.COOKIES:
        user=request.COOKIES['username']
        intro=User.objects.filter(uname=user)[0].intro
        filepath='E:\\django-master\\django\\bin\\mysite\\my_app\\user\\'+user+'\\info.txt'
        with io.open(filepath,'r') as f:
            info=f.readline()
        return HttpResponse(render(request, 'manage.html',locals()))
    else:
        return HttpResponseRedirect('/my_app/login')
    
def managestu(request):
    if "username" in request.COOKIES:
        user=request.COOKIES['username']
        if User.objects.filter(uname=user)[0].role=="student":        
            intro=User.objects.filter(uname=user)[0].intro
            info=u"这里是学生界面"
            return HttpResponse(render(request, 'managestu.html',locals()))
        else:
            return HttpResponseRedirect('/my_app/login')
    else:
        return HttpResponseRedirect('/my_app/login')
    
def managetea(request):
    if "username" in request.COOKIES:
        user=request.COOKIES['username']
        if User.objects.filter(uname=user)[0].role=="administrator":
            intro=User.objects.filter(uname=user)[0].intro
            info="test"
            return HttpResponse(render(request, 'managetea.html',locals()))
        else:
            return HttpResponseRedirect('/my_app/login')
    else:
        return HttpResponseRedirect('/my_app/login')
    
def testurl(request,year):
    return HttpResponse("hahaha")

def applypage(request):
    if "username" in request.COOKIES:
        user=request.COOKIES['username']
        if User.objects.filter(uname=user)[0].role=="student":           
            phonenumber=request.GET.get("phonenumber", "")
            date=request.GET.get("date", "")
            maxnum=request.GET.get("maxnum", "")
            activity=request.GET.get('activity',"")
            begintime=request.GET.get('begintime',"")
            endtime=request.GET.get('endtime',"")
            applist=Application.objects.filter(name=request.COOKIES['username'])
            if len(applist)>10:
                applist=applist[:10]
            if date=="":
                date=(now()+datetime.timedelta(days=1)).strftime('%Y-%m-%d')
            '''
            if date=="":
                date=(now()+datetime.timedelta(days=1)).strftime('%Y-%m-%d')
            if date!="" and maxnum!="":
                classlistall=Classroom.objects.filter(maxnum__gte=int(maxnum)).filter(date=date)
                classlist=[]
                for i in range(len(classlistall)):
                    find=True
                    avaltime=eval(classlistall[i].status)
                    for j in range(int(begintime)-1,int(endtime),1):
                        if avaltime[j]==0:
                            find=False
                            break
                    if find==True:
                        classlist.append(classlistall[i])
            else:
                classlistall=[]
                classlist=[]
            '''        
            mindate=(now()+datetime.timedelta(days=1)).strftime('%Y-%m-%d')
            maxdate=(now()+datetime.timedelta(days=7)).strftime('%Y-%m-%d')
            response=render(request, 'applytemplate.html',locals())
            return HttpResponse(response)
        else:
            return HttpResponseRedirect('/my_app/login')
    else:
        return HttpResponseRedirect('/my_app/login')

def applysuccess(request):
    
    if "username" in request.COOKIES:
        user=request.COOKIES['username']
        if User.objects.filter(uname=user)[0].role=="student":
            phonenumber=request.GET.get("phonenumber", None)
            date=request.GET.get("date", None)
            maxnum=request.GET.get("maxnum", None)
            activity=request.GET.get('activity',None)
            begintime=request.GET.get('begintime',None)
            endtime=request.GET.get('endtime',None)
            cla=request.GET.get('cla',None)
            application=Application(name=user,phonenumber=phonenumber,date=date,maxnum=maxnum,\
                                    status="待审核",submittime=now().strftime('%Y-%m-%d %H:%M:%S'),\
                                    activity=activity,begintime=begintime,endtime=endtime,\
                                    classroom=cla)
            application.save()
            response=render(request, 'applysuccess.html')
            return response
        else:
            return HttpResponseRedirect('/my_app/login')
    else:
        return HttpResponseRedirect('/my_app/login')
    
    '''
    response=HttpResponse()
    for key in request.GET.keys():
        response.write(key+':')
        response.write(request.GET[key]+'<br>')
    return response
    '''
    
def checkapplication(request):
    if "username" in request.COOKIES:
        user=request.COOKIES['username']
        if User.objects.filter(uname=user)[0].role=="student":
            applist=Application.objects.filter(name=request.COOKIES['username'])
            response=render(request, 'checkapplication.html', {'applist': applist,'user':user})
            return response
        else:
            return HttpResponseRedirect('/my_app/login')
    else:
        return HttpResponseRedirect('/my_app/login')
    
def checkallapplication(request):#这个功能是给老师用的！！！！
    if "username" in request.COOKIES:
        user=request.COOKIES['username']
        if User.objects.filter(uname=user)[0].role=="administrator":
            appall=Application.objects.all()
            response=render(request,'checkallapplication.html',{'appall':appall})
            return HttpResponse(response)
        else:
            return HttpResponseRedirect('/my_app/login')
    else:
        return HttpResponseRedirect('/my_app/login')
    
def permitapplication(request):
    if "username" in request.COOKIES:
        user=request.COOKIES['username']
        if User.objects.filter(uname=user)[0].role=="administrator":
            targetday=request.GET.get("targetday",None)
            if targetday==None:
                targetday=(now()+datetime.timedelta(days=1)).strftime('%Y-%m-%d')
            else:
                #targetday=datetime.datetime.strptime(targetday,"%Y-%m-%d")
                pass
            classroomlist=Classroom.objects.filter(date=targetday)
            appall=Application.objects.filter(status=u'待审核')
            response=render(request,'permitapplication.html',{'appall':appall,'targetday':targetday,'classroomlist':classroomlist})
            return HttpResponse(response)
        else:
            return HttpResponseRedirect('/my_app/login')
    else:
        return HttpResponseRedirect('/my_app/login')

def logout(requeset):
    response=HttpResponseRedirect('/my_app/login')
    response.delete_cookie("username")
    return response
    
def updatestatus(request):#这里相当于是用未被审核列表里面传递的编号来完成的
    applist=Application.objects.filter(status=u'待审核')#数据库里app的status一旦被更改，applist内的元素数目也会减少
    #for index in range(len(applist)):
    for index in range(len(applist),0,-1):
        info=request.GET.get(str(index),None)
        app=applist[index-1]
        if info=="yes":
            app.status=u"通过"
            building,room=app.classroom.split("-")[0],app.classroom.split("-")[1]
            cla=Classroom.objects.filter(building=building).filter(room=room).filter(date=app.date)[0]
            aval=eval(cla.status)
            for j in range(app.begintime-1,app.endtime,1):
                aval[j]=0
            cla.status=str(aval)
            cla.save()
            app.save()
        elif info=="no":
            app.status=u"被拒绝"
            app.feedback=request.GET.get(str(index)+"opinion",None)
            app.save()
        else:
            continue            
    return HttpResponseRedirect('/my_app/permitapplication')

    
def applyselclassroom(request):
    if "username" in request.COOKIES:
        user=request.COOKIES['username']
        if User.objects.filter(uname=user)[0].role=="student":
            phonenumber=request.GET.get("phonenumber", None)
            date=request.GET.get("date", None)
            maxnum=int(request.GET.get("maxnum", None))
            activity=request.GET.get('activity',None)
            begintime=int(request.GET.get('begintime',None))
            endtime=int(request.GET.get('endtime',None))
            classlist=Classroom.objects.filter(maxnum__gte=maxnum).filter(date=date)
            #datetime.datetime.strptime(date,"%Y-%m-%d")
            #如果是星期日，会返回6，即-1     
            classroom=[]
            for i in range(len(classlist)):
                find=True
                avaltime=eval(classlist[i].status)
                for j in range(begintime-1,endtime,1):
                    if avaltime[j]==0:
                        find=False
                        break
                if find==True:
                    classroom.append(classlist[i])
            response=render(request,'applyselclassroom.HTML',locals())
            return response
        else:
            return HttpResponseRedirect('/my_app/login')
    else:
        return HttpResponseRedirect('/my_app/login')
    
    
    
    
