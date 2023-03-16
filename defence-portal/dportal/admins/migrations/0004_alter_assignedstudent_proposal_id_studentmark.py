# Generated by Django 4.0.4 on 2022-06-01 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_teacher_phone_number_teacher_teacher_initial'),
        ('student', '0002_defenceproposal_assigned_status_and_more'),
        ('admins', '0003_remove_assignedstudent_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignedstudent',
            name='proposal_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='student.defenceproposal'),
        ),
        migrations.CreateModel(
            name='StudentMark',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mid_status', models.IntegerField(default=0)),
                ('final_status', models.IntegerField(default=0)),
                ('student_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='login.student')),
            ],
        ),
    ]