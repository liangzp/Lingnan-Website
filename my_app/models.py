from django.db import models

# Create your models here.
class User(models.Model):
    uname = models.CharField(max_length=200)
    pwd = models.CharField(max_length=200)
    intro=models.CharField(max_length=200)
    role=models.CharField(max_length=200,default="administrator")#另一种身份是学生student
    def __str__(self):
        text=self.uname+'的记录:'+self.intro
        return text
    
class Application(models.Model):#申请课室的数据类
    name = models.CharField(max_length=10)
    activity=models.CharField(max_length=100,default=str(None))
    phonenumber = models.CharField(max_length=11)#电话号码最多只有11位，在输入的时候要检测输入是否全为数字，是否刚好11位
    date=models.CharField(max_length=10)
    begintime=models.IntegerField(default=1)
    endtime=models.IntegerField(default=1)
    maxnum=models.IntegerField()#活动最大人数是多少
    status=models.CharField(max_length=10,default=u"待审核")
    submittime=models.CharField(max_length=10,default=str(None))
    feedback=models.CharField(max_length=100,default=str(None))
    classroom=models.CharField(max_length=20,default=str(None))
    mailbox=models.CharField(max_length=40,default=str(None))#发邮件
    def __str__(self):
        text=self.name+u'想在'+self.date+u'申请一个课室，人数为'+str(self.maxnum)+u',要做的事：'+self.activity
        return text
    
class Classroom(models.Model):#申请课室的数据类
    building=models.CharField(max_length=10)#课室在哪个建筑物,叶葆定，林护堂，岭南堂，黄传经,MBA,EDP
    dayofweek=models.IntegerField(default=4)#周一到周日,即1-7
    date=models.CharField(max_length=20,default="2018-12-13")#表示哪个日期例如2018-12-13
    room=models.CharField(max_length=20)#在建筑物的哪个房间
    status=models.CharField(max_length=200,default=u"[1,1,1,1,1,1,1,1,1,1,1,1]")#1闲置，
    maxnum=models.IntegerField()#课室容量是多少
    #存储在某一天的某一个课室哪些时段是能被申请的,默认一天10个时段都能申请
    def __str__(self):
        text=self.building+u'的'+self.room+u'课室在星期'+str(self.date)+u'的状态是'+self.status
        return text