# Generated by Django 4.1.4 on 2022-12-23 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Categorias',
            },
        ),
    ]
