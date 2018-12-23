from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from django.utils.timezone import now
from my_app.models import User
from rewardu.models import Tasku
from rewardu.models import Materialu
from rewardu.models import Opinionu 
from rewardu.models import Resultu 
from django.core.files import File
import io
import os
import datetime
# Create your views here.
def materialpage(request):
    if "username" in request.COOKIES:
        savepath=os.path.join(os.path.dirname(__file__), 'pic\\'+request.COOKIES['username']).replace('\\','/')
        if os.path.exists(savepath) ==False:
            os.makedirs(savepath)
        with io.open(os.path.dirname(__file__)+"\\result.txt","r") as f:
            signal=f.readline()
        num_addscore=len(os.listdir(savepath))
        user=User.objects.filter(uname=request.COOKIES['username'])[0]
        task=Tasku.objects.filter(user=user).filter(description="校级奖学金")[0]
        status=eval(task.checkorder)[task.status-1]
        if status!="self":
            changematerial="True"
        else:
            changematerial="False"
        #changematerial="False" 
        response=render(request, 'materialpageu.HTML',locals())        
        return HttpResponse(response)
    else:
        return HttpResponseRedirect('/my_app/login')

def submitnewmaterialscore(request):
    if "username" in request.COOKIES:
        if iseditable(request.COOKIES['username'])==False:
            return HttpResponseRedirect('/rewardu/materialpage/')
        savepath=os.path.join(os.path.dirname(__file__), 'pic\\'+request.COOKIES['username']).replace('\\','/')
        if os.path.exists(savepath) ==False:
            os.makedirs(savepath)
        response=render(request, 'submitnewmaterialuscore.HTML')        
        return HttpResponse(response)
    else:
        return HttpResponseRedirect('/my_app/login')
    
def submitnewmaterialpublic(request):
    if "username" in request.COOKIES:
        if iseditable(request.COOKIES['username'])==False:
            return HttpResponseRedirect('/rewardu/materialpage/')
        savepath=os.path.join(os.path.dirname(__file__), 'pic\\'+request.COOKIES['username']).replace('\\','/')
        if os.path.exists(savepath) ==False:
            os.makedirs(savepath)
        #savepath的路径是创建了每一个人的总文件夹，这个文件夹下只有文件夹下只有文件夹，没有文件
        #os.listdir是获得文件夹下文件夹+文件的数目
        response=render(request, 'submitnewmaterialupublic.HTML')        
        return HttpResponse(response)
    else:
        return HttpResponseRedirect('/my_app/login')
    
def editmaterialscore(request):
    if "username" in request.COOKIES:
        if iseditable(request.COOKIES['username'])==False:
            return HttpResponseRedirect('/rewardu/materialpage/')
        user=User.objects.filter(uname=request.COOKIES['username'])[0]
        task=Tasku.objects.filter(user=user).filter(description="校级奖学金")[0]
        materiallist=Materialu.objects.filter(task=task).filter(destype="绩点")
        
        response=render(request, 'editmaterialuscore.HTML',locals())        
        return HttpResponse(response)
    else:
        return HttpResponseRedirect('/my_app/login')
    
def editmaterialpublic(request):
    if "username" in request.COOKIES:
        if iseditable(request.COOKIES['username'])==False:
            return HttpResponseRedirect('/rewardu/materialpage/')
        user=User.objects.filter(uname=request.COOKIES['username'])[0]
        task=Tasku.objects.filter(user=user).filter(description="校级奖学金")[0]
        materiallist=Materialu.objects.filter(task=task).filter(destype="公益时")
        response=render(request, 'editmaterialupublic.HTML',locals())        
        return HttpResponse(response)
    else:
        return HttpResponseRedirect('/my_app/login')
    
def deletematerial(request):
    #deletematerial
    if "username" in request.COOKIES:
        if iseditable(request.COOKIES['username'])==False:
            return HttpResponseRedirect('/rewardu/materialpage/')
        user=User.objects.filter(uname=request.COOKIES['username'])[0]
        task=Tasku.objects.filter(user=user).filter(description="校级奖学金")[0]
        materiallist=Materialu.objects.filter(task=task)
        response=render(request, 'deletematerialu.HTML',locals())        
        return HttpResponse(response)
    else:
        return HttpResponseRedirect('/my_app/login')

def savematerialscore(request):
    if "username" in request.COOKIES:
        if request.method != 'POST':
            return HttpResponseRedirect('/rewardu/materialpage/')
        description=request.POST.get("description","")
        score=request.POST.get("score","")
        public=request.POST.get("public","")
        
        level=request.POST.get("level","")
        fromtime=request.POST.get("fromtime","")
        totime=request.POST.get("totime","")
        kind=request.POST.get("kind","")
        
        user=User.objects.filter(uname=request.COOKIES['username'])[0]
        task=Tasku.objects.filter(user=user).filter(description="校级奖学金")[0]
        
        savepath=os.path.join(os.path.dirname(__file__), 'pic\\'+request.COOKIES['username']).replace('\\','/')
        foldnum=task.material_num
        savepath=savepath+"/"+str(foldnum+1)
        os.makedirs(savepath)
        i=0
        for key in request.FILES.keys():
            i=i+1
            file=request.FILES[key]
            file_suffix=file.name.split(".")[-1]
            with open(savepath+"/"+str(i)+"."+file_suffix,'wb') as fp:
                for part in file.chunks():
                    fp.write(part)
                       
        material=Materialu(task=task,extrascore=float(score),initscore=float(score),\
                          extrapublic=float(public),initpublic=float(public),description=description,\
                          materialid=foldnum+1,num_pic=i,level=level,fromtime=fromtime,\
                          totime=totime,kind=kind,destype="绩点")
        task.material_num=task.material_num+1
        task.total_material=task.total_material+1
        material.save()
        task.save()
        return HttpResponseRedirect('/rewardu/materialpage/')
    else:
        return HttpResponseRedirect('/my_app/login/')
    
def savematerialpublic(request):
    if "username" in request.COOKIES:
        if request.method != 'POST':
            return HttpResponseRedirect('/rewardu/materialpage/')
        description=request.POST.get("description","")
        score=request.POST.get("score","")
        public=request.POST.get("public","")
        
        level=request.POST.get("level","")
        fromtime=request.POST.get("fromtime","")
        totime=request.POST.get("totime","")
        kind=request.POST.get("kind","")
        
        user=User.objects.filter(uname=request.COOKIES['username'])[0]
        task=Tasku.objects.filter(user=user).filter(description="校级奖学金")[0]
        
        savepath=os.path.join(os.path.dirname(__file__), 'pic\\'+request.COOKIES['username']).replace('\\','/')
        foldnum=task.material_num
        savepath=savepath+"/"+str(foldnum+1)
        os.makedirs(savepath)
        i=0
        for key in request.FILES.keys():
            i=i+1
            file=request.FILES[key]
            file_suffix=file.name.split(".")[-1]
            with open(savepath+"/"+str(i)+"."+file_suffix,'wb') as fp:
                for part in file.chunks():
                    fp.write(part)
                       
        material=Materialu(task=task,extrascore=float(score),initscore=float(score),\
                          extrapublic=float(public),initpublic=float(public),description=description,\
                          materialid=foldnum+1,num_pic=i,level=level,fromtime=fromtime,\
                          totime=totime,kind=kind,destype="公益时")
        task.material_num=task.material_num+1
        task.total_material=task.total_material+1
        material.save()
        task.save()
        return HttpResponseRedirect('/rewardu/materialpage/')
    else:
        return HttpResponseRedirect('/my_app/login/')
    
def rewardmain(request):
    if "username" in request.COOKIES:
        response=render(request,"rewardmainu.html")
        return response
    else:
        return HttpResponseRedirect('/my_app/login/')
    
def editspecificmaterialpublic(request):
    if "username" in request.COOKIES:
        if "material_id" not in request.GET:
            return HttpResponseRedirect('/rewardu/materialpage/')
        if iseditable(request.COOKIES['username'])==False:
            return HttpResponseRedirect('/rewardu/materialpage/')
        materialid=int(request.GET.get("material_id","0"))
        user=User.objects.filter(uname=request.COOKIES['username'])[0]
        task=Tasku.objects.filter(user=user).filter(description="校级奖学金")[0]
        material=Materialu.objects.filter(task=task).filter(materialid=materialid)[0]
        picpath=os.path.join(os.path.dirname(__file__), 'pic\\'+request.COOKIES['username']+"\\"+request.GET.get("material_id","0")).replace('\\','/')
        piclist=os.listdir(picpath)
        #for i in range(len(piclist)):#把获得文件名的后缀去掉
        #    piclist[i]=piclist[i].split(".")[0]
        response=render(request,"editspecificmaterialupublic.html",locals())
        return HttpResponse(response)
    else:
        return HttpResponseRedirect('/my_app/login/')

def editspecificmaterialscore(request):
    if "username" in request.COOKIES:
        if "material_id" not in request.GET:
            return HttpResponseRedirect('/rewardu/materialpage/')
        if iseditable(request.COOKIES['username'])==False:
            return HttpResponseRedirect('/rewardu/materialpage/')
        materialid=int(request.GET.get("material_id","0"))
        user=User.objects.filter(uname=request.COOKIES['username'])[0]
        task=Tasku.objects.filter(user=user).filter(description="校级奖学金")[0]
        material=Materialu.objects.filter(task=task).filter(materialid=materialid)[0]
        picpath=os.path.join(os.path.dirname(__file__), 'pic\\'+request.COOKIES['username']+"\\"+request.GET.get("material_id","0")).replace('\\','/')
        piclist=os.listdir(picpath)
        #for i in range(len(piclist)):#把获得文件名的后缀去掉
        #    piclist[i]=piclist[i].split(".")[0]
        response=render(request,"editspecificmaterialuscore.html",locals())
        return HttpResponse(response)
    else:
        return HttpResponseRedirect('/my_app/login/')

def saveedition(request):
    if "username" in request.COOKIES:
        if "materialid" not in request.POST:
            return HttpResponseRedirect('/my_app/login/')
        user=User.objects.filter(uname=request.COOKIES["username"])[0]
        task=Tasku.objects.filter(user=user).filter(description="校级奖学金")[0]
        materialid=request.POST['materialid']
        material=Materialu.objects.filter(task=task).filter(materialid=materialid)[0]
        #先处理加分是否有变化       
        material.extrascore=float(request.POST['score'])
        material.initscore=material.extrascore
        material.extrapublic=float(request.POST['public'])
        material.initpublic=material.extrapublic
        material.description=request.POST['description']
        
        material.level=request.POST.get("level","")
        material.fromtime=request.POST.get("fromtime","")
        material.totime=request.POST.get("totime","")
        material.kind=request.POST.get("kind","")
        #处理是否有删除已经存好的图片
        picpath=os.path.join(os.path.dirname(__file__), 'pic\\'+request.COOKIES['username']+"\\"+materialid).replace('\\','/')
        piclist=os.listdir(picpath)
        for pic in piclist:
            if ("text"+pic) not in request.POST:
                os.remove(picpath+'/'+pic)
        
        #处理新加入的图片
        i=material.num_pic
        #response=HttpResponse()
        for key in request.FILES.keys():
            #response.write(request.FILES[key])
            i=i+1
            file=request.FILES[key]
            file_suffix=file.name.split(".")[-1]
            with open(picpath+"/"+str(i)+"."+file_suffix,'wb') as fp:
                for part in file.chunks():
                    fp.write(part)
            
        material.num_pic=i
        material.save()
        #return HttpResponseRedirect('/rewardu/materialpage/editspecificmaterial/?material_id='+materialid)
        return HttpResponseRedirect('/rewardu/materialpage/')
        #response=HttpResponse()
        #response.write(request.META[])
        #return response
        
    else:
        return HttpResponseRedirect('/my_app/login/')
    
def submitdeletematerial(request):
    if "username" in request.COOKIES:
        if "targetmaterial" not in request.GET:
            return HttpResponseRedirect("/rewardu/materialpage/deletematerial/")
        if iseditable(request.COOKIES['username'])==False:
            return HttpResponseRedirect('/rewardu/materialpage/')
        user=User.objects.filter(uname=request.COOKIES['username'])[0]
        task=Tasku.objects.filter(user=user).filter(description="校级奖学金")[0]
        materialpath=os.path.join(os.path.dirname(__file__), 'pic\\'+request.COOKIES['username']+"\\"+request.GET['targetmaterial']).replace('\\','/')
        if not os.path.exists(materialpath):
            return HttpResponseRedirect("/rewardu/materialpage/deletematerial/")
        for file in os.listdir(materialpath):
            os.remove(materialpath+"/"+file)
        os.rmdir(materialpath)
        #user=User.objects.filter(uname=request.COOKIES["username"])[0]
        #task=Tasku.objects.filter(user=user).filter(description="校级奖学金")[0]
        materialid=request.GET["targetmaterial"]
        material=Materialu.objects.filter(task=task).filter(materialid=int(materialid))[0]
        material.delete()
        task.total_material=task.total_material-1
        task.save()
        #response=HttpResponse()
        #response.write(path)
        #return response
        return HttpResponseRedirect("/rewardu/materialpage/deletematerial/")
    else:
        return HttpResponseRedirect('/my_app/login/')
    
def viewmaterial(request):
    if "username" in request.COOKIES:
        user=User.objects.filter(uname=request.COOKIES['username'])[0]
        task=Tasku.objects.filter(user=user).filter(description="校级奖学金")[0]
        status=eval(task.checkorder)[task.status-1]
        if status=="self":
            return HttpResponseRedirect('/rewardu/materialpage/')
        with io.open(os.path.dirname(__file__)+"\\result.txt","r") as f:
            signal=f.readline()
        if signal=="1":
            return HttpResponseRedirect('/rewardu/materialpage/')
        materiallist=Materialu.objects.filter(task=task)
        checker=eval(task.checkorder)[task.status-1]
        order=eval(task.checkorder_char)[task.status-1]
        response=render(request, 'viewmaterialu.HTML',locals())        
        return HttpResponse(response)
    else:
        return HttpResponseRedirect('/my_app/login')

def viewspecificmaterial(request):
    if "username" in request.COOKIES:
        if "material_id" not in request.GET:
            return HttpResponseRedirect('/rewardu/materialpage/')
        materialid=int(request.GET.get("material_id","0"))
        user=User.objects.filter(uname=request.COOKIES['username'])[0]
        task=Tasku.objects.filter(user=user).filter(description="校级奖学金")[0]
        status=eval(task.checkorder)[task.status-1]
        if status=="self":
            return HttpResponseRedirect('/rewardu/materialpage/')
        with io.open(os.path.dirname(__file__)+"\\result.txt","r") as f:
            signal=f.readline()
        if signal=="1":
            return HttpResponseRedirect('/rewardu/materialpage/')
        material=Materialu.objects.filter(task=task).filter(materialid=materialid)[0]
        opinionlist=Opinionu.objects.filter(material=material)
        picpath=os.path.join(os.path.dirname(__file__), 'pic\\'+request.COOKIES['username']+"\\"+request.GET.get("material_id","0")).replace('\\','/')
        piclist=os.listdir(picpath)
        response=render(request,"viewspecificmaterialu.html",locals())
        return HttpResponse(response)
    else:
        return HttpResponseRedirect('/my_app/login/')
    
def checktask(request):
    if "username" in request.COOKIES:
        materialid=int(request.GET.get("material_id","0"))
        user=User.objects.filter(uname=request.COOKIES['username'])[0]
        tasklist=Tasku.objects.filter(now_checker=request.COOKIES['username'])
        with io.open(os.path.dirname(__file__)+"\\result.txt","r") as f:
            signal=f.readline()
        if signal=="1":
            return HttpResponseRedirect('/rewardu/materialpage/')
        '''
        material=Materialu.objects.filter(task=task).filter(materialid=materialid)[0]
        opinionlist=Opinionu.objects.filter(material=material)
        picpath=os.path.join(os.path.dirname(__file__), 'pic\\'+request.COOKIES['username']+"\\"+request.GET.get("material_id","0")).replace('\\','/')
        piclist=os.listdir(picpath)
        '''
        response=render(request,"checktasku.html",locals())
        return HttpResponse(response)
    else:
        return HttpResponseRedirect('/my_app/login/')
    
def checkspecifictask(request):
    if "username" in request.COOKIES:
        if "username" not in request.GET:
            return HttpResponseRedirect('/rewardu/materialpage/')
        with io.open(os.path.dirname(__file__)+"\\result.txt","r") as f:
            signal=f.readline()
        if signal=="1":
            return HttpResponseRedirect('/rewardu/materialpage/')
        #materialid=int(request.GET.get("material_id","0"))
        user=User.objects.filter(uname=request.GET['username'])[0]
        task=Tasku.objects.filter(user=user).filter(description="校级奖学金")[0]
        if task.now_checker!=request.COOKIES["username"]:
            return HttpResponseRedirect('/rewardu/materialpage/')
        materiallist=Materialu.objects.filter(task=task)
        response=render(request,"checkspecifictasku.html",locals())
        return HttpResponse(response)
    else:
        return HttpResponseRedirect('/my_app/login/')
    
def checkspecificmaterial(request):
    if "username" in request.COOKIES:
        if "material_id" not in request.GET:
            return HttpResponseRedirect('/rewardu/materialpage/')
        if "user" not in request.GET:
            return HttpResponseRedirect('/rewardu/materialpage/')
        with io.open(os.path.dirname(__file__)+"\\result.txt","r") as f:
            signal=f.readline()
        if signal=="1":
            return HttpResponseRedirect('/rewardu/materialpage/')
        materialid=int(request.GET.get("material_id","0"))
        user=User.objects.filter(uname=request.GET['user'])[0]
        task=Tasku.objects.filter(user=user).filter(description="校级奖学金")[0]
        if task.now_checker!=request.COOKIES["username"]:
            return HttpResponseRedirect('/rewardu/materialpage/')
        material=Materialu.objects.filter(task=task).filter(materialid=materialid)[0]
        #opinionlist=Opinionu.objects.filter(material=material).filter(name=request.COOKIES["username"])
        opinionlist=Opinionu.objects.filter(material=material)
        opinioncontent=""
        if len(opinionlist)>0:
            for opinion in opinionlist:
                if str(opinion)!="":
                    opinioncontent=opinioncontent+str(opinion)+"\n"
        else:
            opinioncontent=u"无"
        picpath=os.path.join(os.path.dirname(__file__), 'pic\\'+user.uname+"\\"+request.GET.get("material_id","0")).replace('\\','/')
        piclist=os.listdir(picpath)
        response=render(request,"checkspecificmaterialu.html",locals())
        return HttpResponse(response)
    else:
        return HttpResponseRedirect('/my_app/login/')
    
def savecheck(request):
    if "username" in request.COOKIES:
        if "materialid" not in request.POST:
            return HttpResponseRedirect('/rewardu/materialpage/')
        if "name" not in request.POST:
            return HttpResponseRedirect('/rewardu/materialpage/')
        if "score" not in request.POST:
            return HttpResponseRedirect('/rewardu/materialpage/')
        if "public" not in request.POST:
            return HttpResponseRedirect('/rewardu/materialpage/')
        if "myopinion" not in request.POST:
            return HttpResponseRedirect('/reward/materialpage/')
        materialid=int(request.POST.get("materialid","0"))
        user=User.objects.filter(uname=request.POST['name'])[0]
        task=Tasku.objects.filter(user=user).filter(description="校级奖学金")[0]
        material=Materialu.objects.filter(task=task).filter(materialid=materialid)[0]
        rightnow=now().strftime('%Y-%m-%d %H:%M:%S')
        opinioncontent=request.POST['myopinion']
        opinion=Opinionu(material=material,opinioncontent=opinioncontent,name=request.COOKIES["username"],\
                        submitdate=rightnow)
        opinion.save()
        material.extrascore=float(request.POST["score"])
        material.extrapublic=float(request.POST["public"])
        material.save()
        return HttpResponseRedirect('/rewardu/materialpage/checkspecificmaterial/?material_id='+request.POST["materialid"]+'&user='+request.POST["name"])
    else:
        return HttpResponseRedirect('/my_app/login/')
    
def reuslt(request):
    if "username" in request.COOKIES:
        with io.open(os.path.dirname(__file__)+"\\result.txt","r") as f:
            signal=f.readline()
        if signal!="1":
            return HttpResponseRedirect('/my_app/managestu/')
        relist=Resultu.objects.all().order_by('uname')
        response=render(request,"resultu.html",locals())
        return HttpResponse(response)
    else:
        return HttpResponseRedirect('/my_app/login/')
    
def iseditable(uname):
    user=User.objects.filter(uname=uname)[0]
    task=Tasku.objects.filter(user=user).filter(description="校级奖学金")[0]
    status=eval(task.checkorder)[task.status-1]
    if status!="self":
        return False
    with io.open(os.path.dirname(__file__)+"\\result.txt","r") as f:
        signal=f.readline()
    if signal=="1":
        return False
    return True
'''
from django.core.files import File
user1=User(name='abc')
user1.pic.save('abc.png', File(open('/tmp/pic.png', 'rb')))
'''

# Create your views here.


# Create your views here.
