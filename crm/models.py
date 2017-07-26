from django.db import models

# Create your models here.


class Customer(models.Model):
    '''客户信息表'''
    name = models.CharField(max_length=32,blank=True,null=True)
    qq = models.CharField(max_length=64,unique=True)
    qq_name = models.CharField(max_length=64,blank=True,null=True)
    phone = models.IntegerField(blank=True,null=True)
    sourse_choice = (
        (0,'转介绍'),
        (1,'QQ群'),
        (2,'官网'),
        (3,'百度推广'),
        (4,'51CTO'),
        (5,'知乎'),
        (6,'市场推广'),
    )
    source = models.SmallIntegerField(choices=sourse_choice)
    referral_from = models.CharField(max_length=64,verbose_name='转介绍人qq',blank=True,null=True)
    consult_course = models.ForeignKey('Course',verbose_name='咨询课程')
    content = models.TextField(verbose_name='咨询详情')
    consultant = models.ForeignKey('UserProfile')
    date = models.DateTimeField(auto_now_add=True)
    memo = models.TextField(verbose_name='备注',blank=True,null=True)
    tag = models.ManyToManyField('Tag',blank=True,null=True)

    def __str__(self):
        return self.qq

class Tag(models.Model):
    '''标签'''
    name = models.CharField(max_length=64,unique=True)

    def __str__(self):
        return self.name


class CustomerFollowUp(models.Model):
    '''客户跟进表'''
    pass


class UserProfile(models.Model):
    '''账号表'''
    pass


class Role(models.Model):
    '''角色表'''
    pass

class Course(models.Model):
    '''课程表'''
    pass

class ClassList(models.Model):
    '''班级列表'''
    pass


class Enrollment(models.Model):
    '''报名表'''
    pass


class CourseRecord(models.Model):
    '''上课记录'''
    pass

class StudyRecord(models.Model):
    '''学习记录'''
    pass

