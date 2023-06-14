# Generated by Django 4.2.1 on 2023-06-07 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceEnquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField()),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('organization', models.CharField(max_length=200)),
                ('phone_no', models.IntegerField(null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('work_description', models.TextField()),
                ('for_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.services')),
            ],
        ),
    ]