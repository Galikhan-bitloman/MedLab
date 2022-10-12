# Generated by Django 4.1.2 on 2022-10-11 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_alter_api_analyses_link_alter_api_news_img_news'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='api_analyses',
            name='banner_img',
        ),
        migrations.CreateModel(
            name='API_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_image', models.ImageField(upload_to='imgAnalyse')),
                ('analyse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.api_analyses')),
            ],
            options={
                'verbose_name': 'Картинка',
                'verbose_name_plural': 'Картинки',
                'db_table': 'API_Image',
            },
        ),
    ]
