# Generated by Django 5.0.2 on 2024-05-02 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caraousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='carousel_images')),
            ],
        ),
    ]
