# Generated by Django 3.1.6 on 2021-02-13 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0003_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacancy',
            options={'ordering': ['-timestamp'], 'verbose_name': 'Вакансия', 'verbose_name_plural': 'Вакансии'},
        ),
    ]