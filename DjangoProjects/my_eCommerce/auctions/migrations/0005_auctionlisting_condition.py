# Generated by Django 3.0.8 on 2020-08-29 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20200829_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='condition',
            field=models.CharField(default='', max_length=12),
        ),
    ]
