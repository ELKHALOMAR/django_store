
import os



STORE_APPS = [
    'store',
    'store.catalog',
    'store.financial',
    'store.accounts',
    'store.pages',
]


STORE_APPS += [
    'sorl.thumbnail',
]

THUMBNAIL_DEBUG = True

STORE_APPS += [
    'pipeline',
]

AUTH_USER_MODEL = 'accounts.User'
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'


from django.conf.global_settings import STATICFILES_FINDERS
STATICFILES_FINDERS += (
    'pipeline.finders.PipelineFinder',
)
from store.utils.finders import get_static_paths
STATIC_PATHS = os.pathsep.join(get_static_paths(STORE_APPS))
PIPELINE_LESS_ARGUMENTS = '--include-path="%s"' % STATIC_PATHS

PIPELINE = {
    'COMPILERS': (
        'pipeline.compilers.less.LessCompiler',
        ),
    'LESS_ARGUMENTS': '--include-path="%s"' % STATIC_PATHS,

    # CSS configurations for django-pipeline
    # All LESS styles configured for store defined
    # You can append your LESS configurations here.
    'STYLESHEETS': {
        # store app LESS styles
        'base': {
            'source_filenames': (
                'store/css/base.less',
            ),
            'output_filename': 'store/css/base.css'
        },
        # store.catalog LESS styles for products catalog
        'catalog': {
            'source_filenames': (
                'catalog/css/catalog.less',
            ),
            'output_filename': 'catalog/css/catalog.css'
        },
        # store.sales LESS styles for checkout pages
        'sales': {
            'source_filenames': (
                'sales/css/sales.less',
            ),
            'output_filename': 'sales/css/sales.css'
        },
        # store.pages LESS styles for flat pages
        'pages': {
            'source_filenames': (
                'pages/css/pages.less',
            ),
            'output_filename': 'pages/css/pages.css'
        }
    },

    'DISABLE_WRAPPER': True,
    # Javascript configuration for django-pipeline
    # store app's Javascript compressed & versioned before deployment
    # Simply add your project or apps Javascript here
    'JAVASCRIPT': {
        # store: Base javascript include in every page
        'jquery_ajax': {
            'source_filenames': (
                'store/scripts/jquery-ajax.js',
            ),
            'output_filename': 'store/scripts/jquery-ajax.js',
        },
        # store.catalog: Javascript for product catalog pages
        'catalog_base': {
            'source_filenames': (
                'catalog/scripts/jquery.catalog_base.js',
            ),
            'output_filename': 'catalog/scripts/catalog_base.js',
        },
        'search_products': {
            'source_filenames': (
                'catalog/scripts/jquery.search_products.js',
            ),
            'output_filename': 'catalog/scripts/search_products.js',
        },
        'product_detail': {
            'source_filenames': (
                'catalog/scripts/jquery.scrollTo.js',
                'catalog/scripts/jquery.serialScroll.js',
                'catalog/scripts/jquery.elevatezoom.js',
                'catalog/scripts/jquery.product_detail.js',
            ),
            'output_filename': 'catalog/scripts/product_detail.js',
        },
        'sales_checkout_order': {
            'source_filenames': (
                'sales/scripts/jquery.creditCardValidator.js',
                'sales/scripts/jquery.maskedinput.js',
                'sales/scripts/jquery.checkout_order.js',
            ),
            'output_filename': 'sales/scripts/sales_checkout_order.js',
        }
    }
}

# Views to render page from store.pages
PAGE_VIEWS = (('pages_base_page', 'Base View'),
              ('pages_catalog_page', 'Catalog View')
)