# Generated by Django 4.2.4 on 2023-08-29 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='rating',
            field=models.IntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Start'), (5, '5 Start')], default='1'),
            preserve_default=False,
        ),
    ]
