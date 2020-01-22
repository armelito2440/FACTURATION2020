# Generated by Django 2.2.5 on 2020-01-20 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facture', '0011_auto_20200120_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facture',
            name='prestToFact',
        ),
        migrations.AddField(
            model_name='facture',
            name='prestToFact',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='facture.PrestToFact'),
            preserve_default=False,
        ),
    ]