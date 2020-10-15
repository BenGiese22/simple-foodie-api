from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [('migrations', '0001_initial')]

    operations = [
        # migrations.DeleteModel('Tribble'),
        # migrations.AddField('image', 'rating', models.IntegerField(default=0)),
        migrations.AddField('image', models.CharField(max_length=5000, blank=True),
        migrations.AddField('total_prep_time', models.IntegerField(blank=True, null=True),
    ]
