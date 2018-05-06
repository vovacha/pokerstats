# Generated by Django 2.0.5 on 2018-05-06 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokerstats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='current_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_team', to='pokerstats.Team'),
        ),
    ]
