# Generated by Django 4.2.1 on 2023-06-02 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_portfolio_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='category',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
