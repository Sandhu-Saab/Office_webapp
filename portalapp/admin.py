from django.contrib import admin
from .models import *


# Register your models here.

class Learning_PathAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
admin.site.register(Learning_Path, Learning_PathAdmin)


class TrainerAdmin(admin.ModelAdmin):
    list_display = ('trainer_id', 'trainer_name')
admin.site.register(Trainer, TrainerAdmin)

