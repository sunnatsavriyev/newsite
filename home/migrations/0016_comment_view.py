# Generated by Django 4.2.3 on 2023-10-10 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_comment_user_profile_comment_user_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='view',
            field=models.IntegerField(default=0),
        ),
    ]