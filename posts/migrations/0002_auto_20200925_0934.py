# Generated by Django 3.1.1 on 2020-09-25 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author_id',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=999, on_delete=django.db.models.deletion.CASCADE, to='posts.author'),
        ),
    ]