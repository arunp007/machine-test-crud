# Generated by Django 4.0.1 on 2022-06-16 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0005_delete_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=25)),
                ('contact', models.TextField(max_length=25)),
                ('email', models.EmailField(max_length=25)),
                ('username', models.TextField(max_length=25)),
                ('password', models.TextField(max_length=25)),
                ('cpassword', models.TextField(max_length=25)),
            ],
            options={
                'db_table': 'registration',
            },
        ),
    ]
