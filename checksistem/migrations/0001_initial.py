# Generated by Django 2.2.5 on 2019-11-25 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='WorkGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=20, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employe_name', models.CharField(blank=True, max_length=50, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('card_employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checksistem.Cards')),
                ('group_employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checksistem.WorkGroups')),
            ],
        ),
    ]