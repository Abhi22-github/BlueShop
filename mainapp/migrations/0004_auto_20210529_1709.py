# Generated by Django 3.1.7 on 2021-05-29 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20210529_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobiles',
            name='price',
            field=models.IntegerField(),
        ),
    ]
