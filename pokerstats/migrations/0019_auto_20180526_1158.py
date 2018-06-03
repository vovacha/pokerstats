# Generated by Django 2.0.5 on 2018-05-26 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokerstats', '0018_auto_20180526_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameresult',
            name='total',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='roundresult',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]