# Generated by Django 4.2.3 on 2023-09-14 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_profilemodel_tel_nomer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectmodel',
            name='project_image',
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='gitHub_link',
            field=models.CharField(default='defult link', max_length=100),
        ),
    ]