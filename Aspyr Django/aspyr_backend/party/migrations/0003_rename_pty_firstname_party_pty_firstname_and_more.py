# Generated by Django 5.1.2 on 2024-10-09 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0002_alter_party_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='party',
            old_name='PTY_FirstName',
            new_name='pty_firstname',
        ),
        migrations.RenameField(
            model_name='party',
            old_name='PTY_ID',
            new_name='pty_id',
        ),
        migrations.RenameField(
            model_name='party',
            old_name='PTY_LastName',
            new_name='pty_lastname',
        ),
        migrations.RemoveField(
            model_name='party',
            name='PTY_Age',
        ),
        migrations.RemoveField(
            model_name='party',
            name='PTY_Gender',
        ),
        migrations.RemoveField(
            model_name='party',
            name='PTY_Phone',
        ),
        migrations.RemoveField(
            model_name='party',
            name='PTY_SSN',
        ),
        migrations.AlterModelTable(
            name='party',
            table='opt_party',
        ),
        migrations.AddField(
            model_name='party',
            name='pty_age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='party',
            name='pty_gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='party',
            name='pty_phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='party',
            name='pty_ssn',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
