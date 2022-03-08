# Generated by Django 4.0.3 on 2022-03-08 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkedQRCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qruid', models.CharField(editable=False, max_length=8, verbose_name='UID')),
                ('qrcode', models.ImageField(blank=True, editable=False, null=True, upload_to='qrcode')),
                ('qrcode_data', models.CharField(default='', help_text='Track qrcode data field', max_length=500, verbose_name='qrcode data')),
                ('linked_object_id', models.IntegerField(help_text='Linked instance primary key.')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('linked_object_type', models.ForeignKey(help_text='Linked object type', on_delete=django.db.models.deletion.CASCADE, related_name='qrcodes', to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'Linked QR Code',
                'verbose_name_plural': 'Linked QR Codes',
            },
        ),
    ]
