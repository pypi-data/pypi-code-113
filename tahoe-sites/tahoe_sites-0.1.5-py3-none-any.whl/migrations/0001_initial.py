# Generated by Django 2.2.26 on 2022-01-14 08:28

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

from tahoe_sites import zd_helpers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0011_historicalorganization_edx_uuid'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    # Usage of zd_helpers was edited manually since django migrator sets the value directly
    # instead of linking to zd_helpers functions
    operations = [
        migrations.CreateModel(
            name='UserOrganizationMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(db_column=zd_helpers.get_replacement_name('is_amc_admin'), default=False)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='organizations.Organization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': zd_helpers.get_replacement_name('organizations_userorganizationmapping'),
                'managed': zd_helpers.get_meta_managed(),
            },
        ),
        migrations.CreateModel(
            name='TahoeSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('organization', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='organizations.Organization')),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
        ),
    ]
