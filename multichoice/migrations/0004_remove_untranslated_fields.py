# Generated by Django 2.2.24 on 2022-01-06 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("multichoice", "0003_migrate_translatable_fields")]

    operations = [migrations.RemoveField(model_name="answer", name="_content")]
