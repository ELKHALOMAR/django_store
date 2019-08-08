# Generated by Django 2.2.4 on 2019-08-05 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('financial', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='images/catalog/categories')),
                ('tags', models.CharField(blank=True, help_text='Comma-delimited set of SEO keywords for meta tag', max_length=100, null=True)),
                ('display_order', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('is_expended', models.BooleanField(default=False, help_text='Catergory will always shown expended')),
                ('updated_by', models.CharField(max_length=100)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='catalog.Category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ('display_order', 'id'),
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('updated_by', models.CharField(max_length=100)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('part_number', models.CharField(blank=True, help_text='Manufacturer part number', max_length=50, null=True)),
                ('sku', models.CharField(blank=True, max_length=50, null=True, verbose_name='SKU')),
                ('gtin', models.CharField(blank=True, help_text='Global Trade Item Number (GTIN)', max_length=50, null=True, verbose_name='GTIN')),
                ('gist', models.CharField(blank=True, help_text='Short description of the product', max_length=500, null=True)),
                ('description', models.TextField(blank=True, help_text='Full description displayed on the product page', null=True)),
                ('price', models.DecimalField(decimal_places=2, help_text='Per unit price', max_digits=9)),
                ('old_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('cost', models.DecimalField(decimal_places=2, default=0.0, help_text='Per unit cost', max_digits=9)),
                ('shipping_cost', models.DecimalField(decimal_places=2, default=0.0, help_text='Shipping cost per unit', max_digits=9)),
                ('quantity', models.IntegerField(help_text='Stock quantity')),
                ('is_active', models.BooleanField(default=True, help_text='Product is available for listing and sale')),
                ('is_bestseller', models.BooleanField(default=False, help_text='It has been best seller')),
                ('is_featured', models.BooleanField(default=False, help_text='Promote this product on main pages')),
                ('is_free_shipping', models.BooleanField(default=False, help_text='No shipping charges')),
                ('tags', models.CharField(blank=True, help_text='Comma-delimited set of SEO keywords for meta tag', max_length=250, null=True)),
                ('weight', models.FloatField(default=0)),
                ('length', models.FloatField(default=0)),
                ('width', models.FloatField(default=0)),
                ('height', models.FloatField(default=0)),
                ('updated_by', models.CharField(max_length=100)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=100)),
                ('brand', models.ForeignKey(help_text='Manufacturer', on_delete=django.db.models.deletion.CASCADE, to='catalog.Manufacturer')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Category')),
                ('tax', models.ForeignKey(blank=True, help_text='Tax applied on this product, if tax exempt select none', null=True, on_delete=django.db.models.deletion.CASCADE, to='financial.Tax')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='ProductPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(upload_to='images/catalog/products')),
                ('display_order', models.IntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pics', to='catalog.Product')),
            ],
            options={
                'verbose_name_plural': 'Product Pics',
                'db_table': 'catalog_product_pic',
                'ordering': ('display_order', 'id'),
            },
        ),
        migrations.CreateModel(
            name='ProductSpec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=250)),
                ('display_order', models.IntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specs', to='catalog.Product')),
            ],
            options={
                'verbose_name_plural': 'Product Specs',
                'db_table': 'catalog_product_spec',
                'ordering': ('display_order', 'id'),
                'unique_together': {('product', 'name')},
            },
        ),
    ]