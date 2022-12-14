# Generated by Django 4.1.3 on 2022-11-09 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('repo', models.CharField(max_length=124)),
                ('deploy', models.CharField(max_length=124)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(max_length=255, upload_to='project/', verbose_name='Project')),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(max_length=255, upload_to='technology/', verbose_name='Technology')),
            ],
        ),
        migrations.CreateModel(
            name='TechnologiesProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.project')),
                ('technology', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.technology')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(through='work.TechnologiesProject', to='work.technology'),
        ),
    ]
