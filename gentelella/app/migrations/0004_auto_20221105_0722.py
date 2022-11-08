# Generated by Django 2.1 on 2022-11-05 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20221105_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='control',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='control',
            name='desc',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='control',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
