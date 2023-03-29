# Generated by Django 4.1.7 on 2023-03-26 13:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0023_alter_notes_ndetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='buy',
            field=models.ManyToManyField(related_name='buy_notes', to=settings.AUTH_USER_MODEL),
        ),
    ]