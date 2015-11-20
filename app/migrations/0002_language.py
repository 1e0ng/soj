
from django.db import migrations

def add_language(apps, schema_editor):
    Language = apps.get_model('app', 'Language')
    languages = ('G++', 'GCC', 'Java', 'Pascal', 'Basic', 'Python',)
    for name in languages:
        language = Language(name=name,supported=True)
        language.save()
        print(language.name)

class Migration(migrations.Migration):
    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_language),
    ]
