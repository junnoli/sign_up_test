# Generated by Django 3.0.7 on 2020-06-11 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sign_test', '0008_follows'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follows',
            old_name='Follow_check',
            new_name='follow_check',
        ),
        migrations.RenameField(
            model_name='follows',
            old_name='FollowId',
            new_name='follow_id',
        ),
        migrations.RenameField(
            model_name='follows',
            old_name='UserId',
            new_name='user_id',
        ),
    ]
