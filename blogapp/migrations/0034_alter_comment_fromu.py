# Generated by Django 4.1.7 on 2023-03-31 20:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0033_alter_cmntreply_cmtrply_alter_cmntreply_frr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='fromU',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fromCmnt', to=settings.AUTH_USER_MODEL),
        ),
    ]