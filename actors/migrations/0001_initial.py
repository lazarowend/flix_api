# Generated by Django 5.0.4 on 2024-04-16 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(choices=[('US', 'Estados Unidos'), ('GB', 'Reino Unido'), ('FR', 'França'), ('IT', 'Itália'), ('AU', 'Austrália'), ('CA', 'Canadá'), ('DE', 'Alemanha'), ('JP', 'Japão'), ('IN', 'Índia'), ('BR', 'Brasil')], max_length=100)),
            ],
        ),
    ]