from django.db import models

# Create your models here.



class Learning_Path(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=5000)

    def __str__(self):
        return str(self.name)


class Trainer(models.Model):
    trainer_id = models.AutoField(primary_key=True)
    trainer_name = models.CharField(max_length=20)
    adderes = models.CharField(max_length=500)
    phone_no = models.CharField(max_length=13, unique=True)
    phone_no_optional = models.CharField(max_length=13, null=True, blank=True)
    email = models.CharField(max_length=50)
    email_optional = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(choices=(('Male','Male'),('Female','Female')), max_length=30, blank=True, null=True)
    trainer_international = models.CharField(choices=(('Yes','Yes'),('No','No')), max_length=30, blank=True, null=True)
    trainer_pricing = models.CharField(max_length=1000)
    trainer_course_specialization = models.CharField(max_length=5000)
    trainer_skill_set = models.CharField(max_length=10000)
    trainer_enrolled_with = models.ForeignKey(Learning_Path, on_delete=models.PROTECT)
    trainer_tier =  models.CharField(choices=(('1','1'),('2','2'),('3','3'),('4','4')), max_length=10)
    trainer_attachment = models.FileField(upload_to ='portalapp/static/uploads/', blank=True, null=True)

    