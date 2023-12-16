# Generated by Django 4.2.8 on 2023-12-14 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acknowledgment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acknowledgment_date', models.DateTimeField(blank=True, null=True)),
                ('purchase_order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='acknowledgment', to='orders.purchaseorder')),
            ],
        ),
    ]
