# Generated by Django 3.2.10 on 2023-11-13 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0002_rename_authoer_book_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='decription',
            new_name='description',
        ),
    ]
