# Generated by Django 3.0.7 on 2020-06-12 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sign_test', '0013_auto_20200612_1105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follows',
            old_name='follow_id',
            new_name='follow',
        ),
    ]