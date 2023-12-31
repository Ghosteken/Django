# Generated by Django 4.2.3 on 2023-07-27 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=122)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='0.2')),
            ],
        ),
    ]
