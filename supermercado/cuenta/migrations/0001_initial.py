# Generated by Django 3.1.2 on 2020-10-18 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('edad', models.PositiveIntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('genero', models.CharField(max_length=15)),
            ],
        ),
    ]
