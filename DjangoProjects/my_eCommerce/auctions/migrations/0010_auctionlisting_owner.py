# Generated by Django 3.0.8 on 2020-09-02 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20200902_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='owner',
            field=models.CharField(default=True, max_length=64),
        ),
    ]
