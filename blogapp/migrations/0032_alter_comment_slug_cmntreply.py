# Generated by Django 4.1.7 on 2023-03-31 20:08

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0031_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='fromU', unique=True),
        ),
        migrations.CreateModel(
            name='CmntReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmntR', models.TextField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='cmntR', unique=True)),
                ('cmtRply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.comment')),
                ('frR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]