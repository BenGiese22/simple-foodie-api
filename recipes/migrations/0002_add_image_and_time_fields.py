from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [('migrations', '0001_initial')]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.CharField(max_length=5000, blank=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='total_prep_time',
            field=models.IntegerField(blank=True, null=True),
        )
    ]