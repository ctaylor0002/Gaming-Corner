# Generated by Django 4.1.4 on 2023-05-23 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0013_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='../images/base_profile_picture.jpg', upload_to='images/'),
        ),
    ]
