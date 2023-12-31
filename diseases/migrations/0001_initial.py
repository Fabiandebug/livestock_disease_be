# Generated by Django 4.2.3 on 2023-07-14 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=100)),
                ('language', models.CharField(choices=[('en', 'English'), ('sw', 'Kiswahili')], max_length=2)),
                ('name', models.CharField(max_length=100)),
                ('local_names', models.TextField()),
                ('other_livestock_affected', models.TextField()),
                ('transmission', models.TextField()),
                ('number_affected_in_herd', models.TextField()),
                ('death_rate', models.TextField()),
                ('predisposing_factors', models.TextField()),
                ('key_signs', models.TextField()),
                ('other_signs', models.TextField()),
                ('prevention', models.TextField()),
            ],
            options={
                'unique_together': {('identifier', 'language')},
            },
        ),
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('description', models.TextField()),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='diseases.disease')),
            ],
        ),
    ]
