# Generated by Django 3.2.8 on 2021-10-13 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='cat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.categories'),
        ),
        migrations.AlterField(
            model_name='products',
            name='prod_datetime_ingress',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='prov',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.provider'),
        ),
    ]
