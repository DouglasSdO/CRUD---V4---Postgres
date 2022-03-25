# Generated by Django 4.0.2 on 2022-03-25 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_cadastro_cpf_alter_cadastro_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='cpf',
            field=models.DecimalField(decimal_places=1, max_digits=10),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='telefone',
            field=models.DecimalField(decimal_places=1, max_digits=10),
        ),
    ]
