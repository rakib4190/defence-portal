# Generated by Django 4.0.4 on 2022-06-03 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0010_assignedstudent_message_body_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignedstudent',
            name='final_document',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AddField(
            model_name='assignedstudent',
            name='final_video',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AddField(
            model_name='assignedstudent',
            name='github_link',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AddField(
            model_name='assignedstudent',
            name='mid_document',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AddField(
            model_name='assignedstudent',
            name='mid_video',
            field=models.CharField(default=0, max_length=500),
        ),
    ]
