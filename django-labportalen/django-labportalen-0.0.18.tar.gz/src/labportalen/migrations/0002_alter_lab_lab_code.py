# Generated by Django 3.2.9 on 2022-03-03 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labportalen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='lab_code',
            field=models.CharField(db_column='lab_code', max_length=250, unique=True, verbose_name='Lab code'),
        ),
    ]
