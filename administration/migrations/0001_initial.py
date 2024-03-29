# Generated by Django 2.2.1 on 2019-08-02 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('virtualmachine', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('tel_contact', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=255)),
                ('admin', models.BooleanField(default=False)),
                ('developper', models.BooleanField(default=False)),
                ('guest', models.BooleanField(default=True)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='virtualmachine.Site')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
