# Generated by Django 4.2.1 on 2023-06-06 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_alter_portfolio_git_hub_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='git_hub_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
