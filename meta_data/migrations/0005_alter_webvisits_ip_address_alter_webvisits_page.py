# Generated by Django 4.2.1 on 2023-06-09 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meta_data', '0004_alter_webvisits_ip_address_alter_webvisits_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webvisits',
            name='ip_address',
            field=models.GenericIPAddressField(),
        ),
        migrations.AlterField(
            model_name='webvisits',
            name='page',
            field=models.URLField(blank=True, null=True),
        ),
    ]