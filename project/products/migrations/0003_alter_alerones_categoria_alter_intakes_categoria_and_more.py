# Generated by Django 5.0.4 on 2024-05-06 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alerones_categoria_intakes_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alerones',
            name='categoria',
            field=models.CharField(choices=[('llantas', 'Llantas'), ('alerones', 'Alerones'), ('spoilers', 'Spoilers'), ('intakes', 'Intakes'), ('widebody', 'Widebody')], default='Seleccionar', max_length=30),
        ),
        migrations.AlterField(
            model_name='intakes',
            name='categoria',
            field=models.CharField(choices=[('llantas', 'Llantas'), ('alerones', 'Alerones'), ('spoilers', 'Spoilers'), ('intakes', 'Intakes'), ('widebody', 'Widebody')], default='Seleccionar', max_length=30),
        ),
        migrations.AlterField(
            model_name='llantas',
            name='categoria',
            field=models.CharField(choices=[('llantas', 'Llantas'), ('alerones', 'Alerones'), ('spoilers', 'Spoilers'), ('intakes', 'Intakes'), ('widebody', 'Widebody')], default='Seleccionar', max_length=30),
        ),
        migrations.AlterField(
            model_name='spoilers',
            name='categoria',
            field=models.CharField(choices=[('llantas', 'Llantas'), ('alerones', 'Alerones'), ('spoilers', 'Spoilers'), ('intakes', 'Intakes'), ('widebody', 'Widebody')], default='Seleccionar', max_length=30),
        ),
        migrations.AlterField(
            model_name='widebody',
            name='categoria',
            field=models.CharField(choices=[('llantas', 'Llantas'), ('alerones', 'Alerones'), ('spoilers', 'Spoilers'), ('intakes', 'Intakes'), ('widebody', 'Widebody')], default='Seleccionar', max_length=30),
        ),
    ]
