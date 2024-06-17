# Generated by Django 5.0.6 on 2024-05-18 09:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('library', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='barrowing',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activitylog',
            name='barrowing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.barrowing'),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='barrowing',
            name='coupons',
            field=models.ManyToManyField(blank=True, to='library.coupon'),
        ),
        migrations.AddField(
            model_name='couponusers',
            name='barrowing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.barrowing'),
        ),
        migrations.AddField(
            model_name='couponusers',
            name='coupon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.coupon'),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='library',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.library'),
        ),
        migrations.AddField(
            model_name='barrowing',
            name='library',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.library'),
        ),
        migrations.AddField(
            model_name='libraryfaqs',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.library'),
        ),
        migrations.AddField(
            model_name='libraryfeatures',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.library'),
        ),
        migrations.AddField(
            model_name='librarygallery',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.library'),
        ),
        migrations.AddField(
            model_name='notification',
            name='barrowing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.barrowing'),
        ),
        migrations.AddField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='helpful',
            field=models.ManyToManyField(blank=True, related_name='helpful', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='library',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='library.library'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='room',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.library'),
        ),
        migrations.AddField(
            model_name='barrowing',
            name='room',
            field=models.ManyToManyField(to='library.room'),
        ),
        migrations.AddField(
            model_name='roomservices',
            name='barrowing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.barrowing'),
        ),
        migrations.AddField(
            model_name='roomservices',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.room'),
        ),
        migrations.AddField(
            model_name='roomtype',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.library'),
        ),
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.roomtype'),
        ),
        migrations.AddField(
            model_name='barrowing',
            name='room_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.roomtype'),
        ),
        migrations.AddField(
            model_name='staffonduty',
            name='barrowing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.barrowing'),
        ),
    ]