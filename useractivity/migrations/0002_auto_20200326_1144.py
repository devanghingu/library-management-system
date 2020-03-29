# Generated by Django 3.0.4 on 2020-03-26 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useractivity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='total_book_issued',
            field=models.PositiveIntegerField(default=0),
        ),
    ]