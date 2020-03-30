# Generated by Django 3.0.2 on 2020-03-30 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eicapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.TextField()),
                ('url', models.TextField()),
            ],
            options={
                'db_table': 'slides',
                'managed': True,
            },
        ),
    ]