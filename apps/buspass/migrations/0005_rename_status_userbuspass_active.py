# Generated by Django 3.2.19 on 2023-06-15 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buspass', '0004_userbuspass_fare'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userbuspass',
            old_name='status',
            new_name='active',
        ),
    ]
