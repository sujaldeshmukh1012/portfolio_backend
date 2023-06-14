# Generated by Django 4.2.1 on 2023-06-06 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_courseintrest'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='image_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='courses',
            name='video_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='courses-poster'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='courses-videos'),
        ),
    ]