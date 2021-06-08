# Generated by Django 3.2.4 on 2021-06-07 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_blogpost_typeof'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='typeof',
            field=models.CharField(choices=[('tech', 'termux'), ('code', 'coding'), ('termux', 'Technology')], default='code', max_length=30),
        ),
    ]
