# Generated by Django 4.1.2 on 2022-11-03 09:48

import accounts.services
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Direktor',
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.user',),
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.FileField(default=1, help_text='Maximum file size allowed is 2Mb', upload_to=accounts.services.location_image, validators=[accounts.services.validate_image, accounts.services.custom_validator]),
            preserve_default=False,
        ),
    ]
