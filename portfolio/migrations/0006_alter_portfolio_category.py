# Generated by Django 4.2.1 on 2023-06-04 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_alter_portfolio_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='category',
            field=models.CharField(blank=True, choices=[('cat', 'jobs'), ('cat2', 'achievements')], max_length=20),
        ),
    ]