# Generated by Django 4.0.4 on 2022-05-28 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_student_id_alter_teacher_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.CharField(default=1, max_length=200),
        ),
    ]
