#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Joel'
SITENAME = "WarHouse"
SITEURL = ''
THEME = './brutalist'

PATH = 'content'
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


## used for OG tags and Twitter Card data on index page
SITEIMAGE = 'logo.jpg'
## used for OG tags and Twitter Card data of index page
SITEDESCRIPTION = 'Personal Blog Made Using Pelican'
## path to favicon
FAVICON = 'logo.jpg'
## path to logo for nav menu (optional)
LOGO = 'logo.jpg'
## first name for nav menu if logo isn't provided
FIRST_NAME = 'Home'
## google analytics (fake code commented out)
# GOOGLE_ANALYTICS = 'UA-0011001-1'
## Twitter username for Twitter Card data

## Toggle display of theme attribution in the footer (scroll down and see)
## Attribution is appreciated but totally fine to turn off!
ATTRIBUTION = True
## Add a link to the tags page to the menu
## Other links can be added following the same tuple pattern 
MENUITEMS = [('Tags', '/tags'),('Archives', '/archives')]
## Social icons for footer
## Set these to whatever your unique public URL is for that platform
## I've left mine here as a example







# PLUGINS
PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap']

## SITEMAP PLUGIN
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': .99,
        'pages': .75,
        'indexes': .5
    },
    'changefreqs': {
        'articles': 'daily',
        'pages': 'daily',
        'indexes': 'daily'
    },
}
