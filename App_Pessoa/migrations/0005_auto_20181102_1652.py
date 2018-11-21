# Generated by Django 2.1.2 on 2018-11-02 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_Pessoa', '0004_auto_20181102_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa_pessoa_tipo',
            name='fk_pessoa_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='App_Pessoa.Pessoa'),
        ),
        migrations.AlterField(
            model_name='pessoa_pessoa_tipo',
            name='fk_pessoa_tipo_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='App_Pessoa.Pessoa_Tipo'),
        ),
    ]
