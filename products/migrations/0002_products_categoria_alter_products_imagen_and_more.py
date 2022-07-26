# Generated by Django 4.0.6 on 2022-07-16 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='categoria',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='imagen',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='products',
            name='numero_parte',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='products',
            name='precio',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='products',
            name='titulo',
            field=models.CharField(default='', max_length=300),
        ),
    ]
