# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('delivery', models.CharField(help_text=b'Estimated remaining delivery time.', max_length=125)),
                ('free_porto', models.BooleanField(default=False, help_text=b'Is product sold porto free?')),
                ('img_url', models.CharField(help_text=b'The relative url on the static url for a product image.', max_length=255)),
                ('name', models.CharField(help_text=b'The user displayed name/description of the product. Not used internally.', max_length=255)),
                ('sizes', models.TextField(help_text=b"List of available sizes. Elements seperated by '/'.")),
                ('url', models.CharField(help_text=b'The relative url for indepth informationon the product.', max_length=255)),
                ('kids', models.IntegerField(default=0, help_text=b'Is this product only available for kids?', choices=[(0, b'Default Demographic'), (1, b'Only for kids')])),
                ('kids_adult', models.IntegerField(default=0, help_text=b'Is this product available for both kids and adults?', choices=[(0, b'Default Demographic'), (1, b'For Kids and Adults')])),
                ('package', models.IntegerField(default=0, help_text=b'Is this product sold in package?', choices=[(0, b'Sold as a seperate product'), (1, b'Sold as part of a package')])),
                ('price', models.DecimalField(default=0, help_text=b'What this product cost. Denominated in DKK.', max_digits=9, decimal_places=2)),
                ('price_old', models.DecimalField(default=0, help_text=b'The previous price of this product. Used to evaluated benefits of price changes.', max_digits=9, decimal_places=2)),
                ('women', models.IntegerField(default=0, help_text=b'Is this product only availablefor women?', choices=[(0, b'Default Demographic'), (1, b'For women only')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
