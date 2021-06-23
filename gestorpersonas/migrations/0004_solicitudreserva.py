# Generated by Django 3.2.3 on 2021-06-23 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestorpersonas', '0003_telefonocontacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitudReserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refugio', models.CharField(max_length=20)),
                ('noches', models.IntegerField()),
                ('fecha', models.DateField()),
            ],
        ),
    ]