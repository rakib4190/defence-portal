# Generated by Django 4.0.4 on 2022-06-01 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_defenceproposal_assigned_status_and_more'),
        ('admins', '0005_remove_assignedstudent_proposal_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignedstudent',
            name='student_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='student.defenceproposal'),
        ),
    ]
