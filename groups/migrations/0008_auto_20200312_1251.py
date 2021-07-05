# Generated by Django 3.0.3 on 2020-03-12 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
        ('groups', '0007_auto_20200312_0849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groups',
            name='group_admin',
        ),
        migrations.AddField(
            model_name='groups',
            name='group_admin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='signup.signup'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='members',
            name='group_id',
        ),
        migrations.AddField(
            model_name='members',
            name='group_id',
            field=models.ManyToManyField(to='groups.Groups'),
        ),
    ]
