# Generated by Django 4.1.3 on 2022-11-19 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_rename_district_district_district_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='districts', to='apis.state'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='apis.user'),
        ),
    ]