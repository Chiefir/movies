# Generated by Django 2.1.7 on 2019-03-28 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_api', '0008_auto_20190327_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='runtime',
            field=models.DurationField(null=True),
        ),
    ]
