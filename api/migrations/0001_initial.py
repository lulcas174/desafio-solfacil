# Generated by Django 4.2 on 2023-04-10 19:09

from django.db import migrations, models

from api.utils import populate_partners_csv


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parceiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=100)),
                ('razao_social', models.CharField(max_length=100)),
                ('nome_fantasia', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RunPython(populate_partners_csv),
    ]
