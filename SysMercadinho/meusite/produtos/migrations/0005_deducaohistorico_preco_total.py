# Generated by Django 5.0 on 2023-12-21 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_deducaohistorico'),
    ]

    operations = [
        migrations.AddField(
            model_name='deducaohistorico',
            name='preco_total',
            field=models.DecimalField(decimal_places=2, default=9, max_digits=10),
            preserve_default=False,
        ),
    ]
