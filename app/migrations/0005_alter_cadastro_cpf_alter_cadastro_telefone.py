# Generated by Django 4.0.2 on 2022-03-24 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_cadastro_cpf_alter_cadastro_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='cpf',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='telefone',
            field=models.CharField(max_length=10),
        ),
    ]
