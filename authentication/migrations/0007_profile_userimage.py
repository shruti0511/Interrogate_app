# Generated by Django 3.2.3 on 2021-06-22 19:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_profile_topics'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='userImage',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='auth/userImg/'),
            preserve_default=False,
        ),
    ]