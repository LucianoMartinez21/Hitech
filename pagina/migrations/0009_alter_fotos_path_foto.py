# Generated by Django 5.0 on 2023-12-23 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0008_rename_contraseñas_contrasenas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotos',
            name='path_foto',
            field=models.ImageField(upload_to='./static/img'),
        ),
    ]
