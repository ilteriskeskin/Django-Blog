# Generated by Django 2.2.1 on 2019-07-01 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['id'], 'verbose_name_plural': 'Gönderiler'},
        ),
    ]
