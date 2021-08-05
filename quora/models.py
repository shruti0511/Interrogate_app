from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField

# Create your models here.
class quoraTopic(models.Model):
    topic_id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'quora/topicImg/')

    def __str__(self):
        return self.topic
    

class Question(models.Model):
    sno = models.AutoField(primary_key=True)
    question = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=0)
    queTopics = models.ManyToManyField(quoraTopic)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.question[0:30] + '... by ' +self.user.username

class Answer(models.Model):
    sno = models.AutoField(primary_key=True)
    answer= RichTextField(blank=True, null= True)
    # answer=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    # parent = models.ForeignKey('self', on_delete=models.CASCADE,null=True)
    timeStamp=models.DateTimeField(default=now)

    def __str__(self):
        return self.answer[0:10] + '... by ' +self.user.username


    
