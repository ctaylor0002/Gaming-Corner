# Generated by Django 4.1.4 on 2022-12-19 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_userprofile_rename_user_collection_usercollection_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='follewers',
            new_name='user_follewers',
        ),
    ]