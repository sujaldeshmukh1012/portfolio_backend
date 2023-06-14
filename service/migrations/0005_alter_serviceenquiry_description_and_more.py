# Generated by Django 4.2.1 on 2023-06-09 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_alter_serviceenquiry_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceenquiry',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='serviceenquiry',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='serviceenquiry',
            name='for_service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.services'),
        ),
        migrations.AlterField(
            model_name='serviceenquiry',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='serviceenquiry',
            name='organization',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='serviceenquiry',
            name='phone_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='serviceenquiry',
            name='work_description',
            field=models.TextField(),
        ),
    ]
