from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, serialize=False, primary_key=True, verbose_name='ID'
                    )
                ),
                ('title', models.CharField(max_length=2000)),
                ('slug', models.SlugField(unique=True, max_length=2000)),
                ('summary', models.TextField(blank=True)),
                ('body', models.TextField(blank=True)),
                ('published_at', models.DateTimeField(null=True, blank=True))
            ],
            options={
                'db_table': 'blog_article'
            }
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, serialize=False, primary_key=True, verbose_name='ID'
                    )
                ),
                ('title', models.CharField(max_length=2000)),
                ('slug', models.SlugField(unique=True, max_length=2000))
            ],
            options={
                'db_table': 'blog_label'
            },
        ),
        migrations.AddField(
            model_name='article',
            name='labels',
            field=models.ManyToManyField(to='blog.Label')
        )
    ]
