# Generated by Django 4.2.10 on 2024-02-08 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='picture', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
