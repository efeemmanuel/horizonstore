# Generated by Django 4.2.2 on 2023-07-09 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appusers', '0006_delete_anonymouscart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='session_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
