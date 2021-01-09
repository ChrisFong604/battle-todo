# Generated by Django 3.1.1 on 2021-01-09 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=200)),
                ('team_points', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=200)),
                ('player_points', models.IntegerField(default=0)),
                ('player_special_select', models.BooleanField(default=False)),
                ('physical_attack', models.IntegerField(default=0)),
                ('physical_defense', models.IntegerField(default=0)),
                ('special_attack', models.IntegerField(default=0)),
                ('special_defense', models.IntegerField(default=0)),
                ('speed', models.IntegerField(default=0)),
                ('player_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.team')),
            ],
        ),
    ]
