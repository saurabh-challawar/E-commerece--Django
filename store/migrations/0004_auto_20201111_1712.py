# Generated by Django 3.1.2 on 2020-11-11 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20201111_1647'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='transaction',
            new_name='transaction_id',
        ),
    ]
