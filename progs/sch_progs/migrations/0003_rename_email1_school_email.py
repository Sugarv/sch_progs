# Generated by Django 4.0.3 on 2022-03-10 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sch_progs', '0002_alter_program_arxeio_alter_program_diaxysh_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='email1',
            new_name='email',
        ),
    ]