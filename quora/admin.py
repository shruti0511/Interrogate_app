from quora.models import Answer,Question, quoraTopic
from django.contrib import admin

# Register your models here.
admin.site.register((Question,Answer,quoraTopic))

