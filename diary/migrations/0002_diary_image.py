# Generated by Django 2.1.8 on 2019-06-26 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
