# Generated by Django 3.0.3 on 2020-08-11 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feeding', '0003_pet'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeding_entry',
            name='pet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='feeding.Pet'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pet',
            name='profile_pic',
            field=models.ImageField(upload_to='pet_profile_pics/'),
        ),
    ]