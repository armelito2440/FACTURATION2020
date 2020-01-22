# Generated by Django 2.1.7 on 2019-10-10 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facture', '0002_auto_20190929_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facture',
            name='type_facture',
            field=models.CharField(choices=[('ANNU', 'Annuelle'), ('MENS', 'Mensuelle'), ('PONC', 'Ponctuelle')], default='PONC', max_length=4, verbose_name='Type facture'),
        ),
    ]
