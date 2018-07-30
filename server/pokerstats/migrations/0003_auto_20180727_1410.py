# Generated by Django 2.0.5 on 2018-07-27 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokerstats', '0002_player_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gameresult',
            options={'ordering': ['player__name']},
        ),
        migrations.AddField(
            model_name='game',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='game_creator', to='pokerstats.Player'),
            preserve_default=False,
        ),
    ]
