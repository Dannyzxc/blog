# Generated by Django 4.1.4 on 2023-01-16 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ablog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='', max_length=50),
        ),
    ]
