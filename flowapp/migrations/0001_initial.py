# Generated by Django 4.1.3 on 2024-02-06 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('faixa', models.CharField(max_length=50)),
                ('data', models.DateField()),
            ],
        ),
    ]