# Generated by Django 2.1.7 on 2019-08-15 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=256)),
            ],
        ),
        migrations.DeleteModel(
            name='Greeting',
        ),
    ]
