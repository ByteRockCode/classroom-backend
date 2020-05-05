# Generated by Django 2.1.7 on 2019-03-12 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20190307_0325'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('creation_timestamp',)},
        ),
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(verbose_name='mensaje'),
        ),
        migrations.AlterField(
            model_name='post',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='asunto'),
        ),
    ]