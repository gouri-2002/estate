# Generated by Django 5.1.3 on 2024-11-09 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('property_type', models.CharField(choices=[('apartment', 'apartment'), ('house', 'house'), ('land', 'land')], default='land', max_length=100)),
                ('number_of_bedrooms', models.PositiveIntegerField()),
                ('square_footage', models.PositiveIntegerField()),
                ('location', models.CharField(max_length=100)),
                ('property_image', models.ImageField(blank=True, null=True, upload_to='estate_img')),
                ('contact_details', models.CharField(max_length=100)),
            ],
        ),
    ]
