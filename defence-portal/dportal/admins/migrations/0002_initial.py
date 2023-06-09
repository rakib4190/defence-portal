# Generated by Django 4.0.4 on 2022-05-27 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('admins', '0001_initial'),
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignedstudent',
            name='proposal_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.defenceproposal'),
        ),
        migrations.AddField(
            model_name='assignedstudent',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.student'),
        ),
        migrations.AddField(
            model_name='assignedstudent',
            name='teacher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.teacher'),
        ),
    ]
