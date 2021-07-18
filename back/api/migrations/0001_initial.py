# Generated by Django 2.2.24 on 2021-07-16 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='INaturalistSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('-1', 'Inactivo'), ('1', 'Activo')], default='1', max_length=10)),
                ('last_modified', models.DateTimeField(auto_now=True, null=True)),
                ('auth_code', models.TextField()),
                ('token', models.TextField()),
                ('created', models.BooleanField(default=False)),
                ('expired', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]