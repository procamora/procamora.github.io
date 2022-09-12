#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import plumage

AUTHOR = u'procamora'
SITENAME = u'#> fireroot'
SITEURL = ''

BASEDIR = os.path.dirname(os.path.realpath('__file__'))
PATH = BASEDIR + 'content'

TIMEZONE = 'Europe/Madrid'
DEFAULT_LANG = u'es'
LOCALE = 'C'
MARKDOWN = {
    'extension_configs': {
        # https://pythonhosted.org/Markdown/extensions/index.html#officially-supported-extensions
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.meta': {},
        'markdown.extensions.sane_lists': {},
        'markdown.extensions.smarty': {},
        'markdown.extensions.toc': {'permalink': True},
        'mdx_video': {},
        # 'mdx_titlecase.mdx_titlecase:TitlecaseExtension': {}, # Pone el primer caracte de los titulos con mayuscales
        # https://facelessuser.github.io/pymdown-extensions/
        'pymdownx.extra': {},
        'pymdownx.caret': {'superscript': True},
        'pymdownx.magiclink': {},
        'pymdownx.smartsymbols': {},
    },
    'output_format': 'html5',
    # Allow numbered lists to not start with 1. Used in following article:
    # https://kevin.deldycke.com/2016/12/falsehoods-programmers-believe-about-falsehoods-lists/
    # See: https://pythonhosted.org/Markdown/reference.html#lazy_ol
    'lazy_ol': False,
}
TYPOGRIFY = True

# Do not publish articles set in the future
WITH_FUTURE_DATES = False

# Force Pelican to use the file name as the slug, instead of derivating it from
# the title.
SLUGIFY_SOURCE = 'basename'

# Force the same URL structure as WordPress
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'
# ARTICLE_PATHS = ['.']

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'
PAGE_PATHS = ['pages']

'''
TEMPLATE_PAGES = {
    'templates/videos.html': 'video/index.html',
    'templates/code.html': 'code/index.html',
    'templates/themes.html': 'themes/index.html',
    'search.html': 'search.html',
}
'''

DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'search']

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = TAG_URL + 'index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = CATEGORY_URL + 'index.html'

YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags, categories and archives are Direct Templates, so they don't have a
# <NAME>_URL option.
TAGS_SAVE_AS = 'tags/index.html'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_SAVE_AS = 'archives/index.html'

# Deactivate author URLs
AUTHOR_SAVE_AS = ''  # Antes era None
AUTHORS_SAVE_AS = ''  # Antes era None

# Deactivate localization
ARTICLE_LANG_SAVE_AS = None
DRAFT_LANG_SAVE_AS = None
PAGE_LANG_SAVE_AS = None

##############
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
##############

# FEED_RSS = 'feed/index.html'
# FEED_ATOM = 'feed/atom/index.html'
# FEED_ALL_RSS = None
# FEED_ALL_ATOM = None
# TRANSLATION_FEED_RSS = None
# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None

# https://kevin.deldycke.com/tag/openerp/feed/
# TAG_FEED_RSS = 'tag/%s/feed/index.html'
# TAG_FEED_ATOM = 'tag/%s/feed/atom/index.html'

# https://example.com/category/categoryname/feed
# CATEGORY_FEED_RSS = 'category/%s/feed/index.html'
# CATEGORY_FEED_ATOM = 'category/%s/feed/atom/index.html'

# FEED_MAX_ITEMS = 10
USE_FOLDER_AS_CATEGORY = True  # el lo tiene en false
DEFAULT_CATEGORY = 'English'
DEFAULT_DATE_FORMAT = '%b. %d, %Y'
REVERSE_ARCHIVE_ORDER = True
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Pagination
DEFAULT_ORPHANS = 2
DEFAULT_PAGINATION = 10
# TODO: set PAGINATION_PATTERNS to produce nice URLs like index/page/23/
# instead of indexXX.html

# THEME = "./theme/plumage"
THEME = plumage.get_path()

STATIC_PATHS = [
    'images',
    #    'feed',
    'downloads',  # borrar en un futuro
    'downloads',
    'extra',
    'code',
    'pdf',
    # '.git/',
]

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/humans.txt': {'path': 'humans.txt'},
    'extra/htaccess': {'path': '.htaccess'},
    'extra/googlec9cb9be279a3dd36.html': {'path': 'googlec9cb9be279a3dd36.html'},
    'extra/pushgit.sh': {'path': 'pushgit.sh'},
    # 'extra/htaccess-static': {'path': 'documents/.htaccess'},
}

'''
LEFT_SIDEBAR = """
    <!--<div data-spy="affix" data-offset-top="0">-->
    <!--<h4>Sponsors</h4>-->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
    <!-- Responsive Ad -->
    <ins class="adsbygoogle"
         style="display:block"
         data-ad-client="ca-pub-0142056597033291"
         data-ad-slot="9726265119"
         data-ad-format="auto"></ins>
    <script>
    (adsbygoogle = window.adsbygoogle || []).push({});
    </script>
    <!--</div>-->
    """
'''

ARTICLE_EDIT_LINK = 'https://github.com/procamora/Wiki-Personal/edit/master/content/%(category)s/%(slug)s.md'
ARTICLE_PDF_LINK = '/pdf/%(slug)s.pdf'
# ARTICLE_PDF_LINK = 'https://github.com/procamora/Wiki-Personal/master/content/pdf/%(slug)s.pdf'

SOCIAL_WIDGET_NAME = "Presencia online"
SOCIAL = (
    ('GitHub', 'https://github.com/procamora'),
    ('Gmail', 'mailto:pablojoserocamora@gmail.com'),
    ('LinkedIn', 'https://linkedin.com/in/pablo-rocamora/'),
    # ('feed', '/rss.xml'),
)

LINKS_WIDGET_NAME = "Links"
LINKS = (
    ('Contacto', '/contacto.html'),
    ('Stackoverflow', 'http://stackoverflow.com/search?q='),
)

COPYRIGHT = ""
DISCLAIMER = "Todas las opiniones expresadas en este sitio son mis propias opiniones personales"

DISQUS_SITENAME = 'procamora-github'

GOOGLE_ANALYTICS = "UA-70813636-1"

OUTPUT_RETENTION = [".git"]
READERS = {'html': None}  # PARA QUE NO DE FALLO POR LOS FICHEROS HTML
FILENAME_METADATA = '(?P<slug>.*)'
RELATED_POSTS_MAX = 3

IMAGE_PATH = "images"
# THUMBNAIL_DIR = ""
THUMBNAIL_SIZES = {
    'thumbnail': '462x?',
}
DEFAULT_TEMPLATE = """<a href="{url}" class="zoomable" title="{filename}">
<img src="{thumbnail}" alt="{filename}"></a>"""

### Theme-specific settings

SITE_THUMBNAIL = '/images/profile.png'
SITE_THUMBNAIL_TEXT = 'Me has visto :)'

SITESUBTITLE = "Wiki de procamora"

MENUITEMS = (
    ('Home', '/'),
    ('Code', '/tag/code/'),
    ('Archivo', '/archives/index.html'),
    ('Tags', '/tags/index.html'),
    ('About', '/about/'),
    ('Secret', '/tag/secret/'),
)

#############################################################################################################
### Plugin-specific settings
#############################################################################################################


PLUGIN_PATHS = ['./pelican-plugins', ]
PLUGINS = [
    'pelican_webassets',
    # #'deadlinks',
    # 'related_posts',
    # # 'thumbnailer',
    # 'tipue_search',
    # 'neighbors',
    # 'sitemap',
    # #'optimize_images',
    # 'just_table',
    # 'encrypt-content'
    #
    # #'pdf' # No es valido en Python 3
]

# Plugin deadlinks
DEADLINK_VALIDATION = True
DEADLINK_OPTS = {
    'archive': True,
    'classes': ['custom-class1', 'disabled'],
    'labels': True,
    'timeout_duration_ms': 2000,
    'timeout_is_error': False,
}

# Plugin tipue_search
TIPUE_SEARCH = True

# Plugin sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Plugin just_table
JTABLE_SEPARATOR = ','
JTABLE_TEMPLATE = """
<table class="uk-table uk-table-striped">
    {% if caption %}
    <caption> {{ caption }} </caption>
    {% endif %}
    {% if th != 0 %}
    <thead>
    <tr>
        {% if ai == 1 %}
        <th> No. </th>
        {% endif %}
        {% for head in heads %}
        <th>{{ head }}</th>
        {% endfor %}
    </tr>
    </thead>
    {% endif %}
    <tbody>
        {% for body in bodies %}
        <tr>
            {% if ai == 1 %}
            <td> {{ loop.index }} </td>
            {% endif %}
            {% for entry in body %}
            <td>{{ entry }}</td>
            {% endfor %}
        </tr>
        {% endfor %}
    </tbody>
</table>
"""

# Plugin encrypt_content
# Para usarlo solo hay que poner en la cabecera: Password: test
ENCRYPT_CONTENT = {
    'title_prefix': '[Encrypted]',
    'summary': 'Este post esta protegido.'
}
