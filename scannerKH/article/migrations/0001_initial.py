# Generated by Django 3.0.5 on 2020-04-17 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wholesaler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('artikelNr', models.CharField(max_length=14, primary_key=True, serialize=False, verbose_name='ArtikelNr')),
                ('wholesaler', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='wholesaler.Wholesaler')),
            ],
        ),
    ]