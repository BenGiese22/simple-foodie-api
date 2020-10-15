from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [('migrations', '0001_initial')]

    operations = [
        migrations.AddField('image', 'image', models.CharField(max_length=5000, blank=True),
        migrations.AddField('total_prep_time', 'total_prep_time', models.IntegerField(blank=True, null=True),
    ]
