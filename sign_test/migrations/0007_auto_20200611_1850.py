# Generated by Django 3.0.7 on 2020-06-11 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_test', '0006_auto_20200611_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='likes',
            name='LikeId',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='likes',
            name='like',
            field=models.IntegerField(default=1),
        ),
    ]
