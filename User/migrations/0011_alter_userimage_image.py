# Generated by Django 4.1.2 on 2023-03-30 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0010_alter_userimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='image',
            field=models.ImageField(default='abc.jpg', upload_to='User.user/User.email'),
        ),
    ]
