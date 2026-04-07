from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_alter_usuario_tipo_administrador_delete_especialista'),
    ]

    operations = [
        migrations.AddField(
            model_name='criador',
            name='Nombre_Refugio',
            field=models.CharField(blank=True, max_length=200, default=''),
            preserve_default=False,
        ),
    ]
