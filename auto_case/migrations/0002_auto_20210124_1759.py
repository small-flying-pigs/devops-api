# Generated by Django 3.1.1 on 2021-01-24 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_case', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='browser',
            field=models.CharField(max_length=32, verbose_name='浏览器'),
        ),
    ]
