# Generated by Django 4.0.3 on 2022-03-08 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0004_rename_create_at_post_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id']},
        ),
    ]
