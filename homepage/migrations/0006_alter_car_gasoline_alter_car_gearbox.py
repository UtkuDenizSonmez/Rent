# Generated by Django 4.0.3 on 2022-03-23 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_car_gasoline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='gasoline',
            field=models.CharField(choices=[('D', 'Dizel'), ('B', 'Benzin')], default='D', max_length=25, verbose_name='Benzin / Dizel'),
        ),
        migrations.AlterField(
            model_name='car',
            name='gearbox',
            field=models.CharField(choices=[('M', 'Manuel'), ('O', 'Otomatik')], default='M', max_length=25, verbose_name='Vites'),
        ),
    ]
