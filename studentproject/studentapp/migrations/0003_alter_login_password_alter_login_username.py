# Generated by Django 4.0.1 on 2022-06-16 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0002_alter_login_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.TextField(max_length=25),
        ),
        migrations.AlterField(
            model_name='login',
            name='username',
            field=models.EmailField(max_length=25),
        ),
    ]
