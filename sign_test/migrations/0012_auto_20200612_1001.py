# Generated by Django 3.0.7 on 2020-06-12 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_test', '0011_auto_20200611_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follows',
            name='follow_check',
            field=models.IntegerField(default=1),
        ),
    ]