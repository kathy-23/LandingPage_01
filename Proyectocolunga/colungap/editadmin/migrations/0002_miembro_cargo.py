# Generated by Django 3.2 on 2021-06-03 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editadmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='miembro',
            name='cargo',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
    ]
