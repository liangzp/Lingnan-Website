from django.db import models
from my_app.models import User

#here is reward.models
# Create your models here.
class Task(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    description=models.CharField(max_length=200)
    checkorder=models.CharField(max_length=200,default=str(None))#该任务分别给谁审核，值为User的uname，还是先把列表以字符串方式储存
    checkorder_char=models.CharField(max_length=200,default=str(None))#该任务分别给谁审核，文字说明，先把列表以字符串方式储存
    status=models.IntegerField(default=0)#数字方式表明目前到了哪一个状态，0表示没开始，1表示第一个阶段
    material_num=models.IntegerField(default=0)#记录该任务的材料数量。这个值只会增加，不会减少，以方便命名
    now_checker=models.CharField(max_length=20,default=str(None))#表明当前轮到谁审核
    total_material=models.IntegerField(default=0)#这个用来记录材料总数，会增加也会减少
    def __str__(self):
        return self.description

class Material(models.Model):#一个加分项对应多张图片
    task=models.ForeignKey(Task, on_delete=models.CASCADE)
    extrascore=models.FloatField(default=0.0)#该加分项的最终数值
    initscore=models.FloatField(default=0.0)#该加分项的最初数值
    extrapublic=models.FloatField(default=0.0)#该公益时项的最终数值
    initpublic=models.FloatField(default=0.0)#该公益时项的最初数值
    description=models.CharField(max_length=200,default=str(None))#该加分项的描述
    materialid=models.IntegerField(default=0)#这个变量实际上是用来记录对应的文件夹名字的
    num_pic=models.IntegerField(default=0)#记录该加分项下有多少张图片
    
    level=models.CharField(max_length=20,default=str("其他"))#该加分项的级别
    fromtime=models.CharField(max_length=20,default=str(None))#该活动的开始时间，只需月份即可
    totime=models.CharField(max_length=20,default=str(None))#该活动的结束时间，只需月份即可
    kind=models.CharField(max_length=20,default=str(None))#该活动的结束时间，只需月份即可
    def __str__(self):
        return self.description+"加分是"

class Opinion(models.Model):
    material=models.ForeignKey(Material, on_delete=models.CASCADE)
    opinioncontent=models.CharField(max_length=100,default=str(None))#留下审核意见
    name=models.CharField(max_length=10,default=str(None))#谁留下这条Opinion，值为user的uname
    submitdate=models.CharField(max_length=100,default=str(None))#意见提交时间
    def __str__(self):
        return self.opinioncontent+"——"+self.name+" "+self.submitdate

# Create your models here.
