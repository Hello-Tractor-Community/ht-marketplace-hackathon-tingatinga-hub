# Generated by Django 3.0.5 on 2024-11-25 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_inappmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inappmessage',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to='store.Product'),
        ),
    ]