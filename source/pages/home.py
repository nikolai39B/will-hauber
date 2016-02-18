"""
FILE:
    home.py
 
DIRECTORY:
    will-hauber/source/pages

DESCRIPTION:
    This file manages requests to '/' (the home page).
"""

# Python
import logging
import os
import sys

# GAE
import webapp2

# Application
import requestHandler as rh
import source.utilities.jinjaTemplateRenderer as jtr
	
# Page Template
pathToContent = os.path.join(rh.rootDir, 'html/content')
contentFilename = 'home.html'
contentTemplateValues = {
    'photos': [
        'images/monster_bath_time.jpg',
        'images/monster_bath_time.jpg'
    ]
}
pageTemplateValues = { 
    'page_title': 'Will Hauber',
    'content_title': 'Home',
}

class Home(webapp2.RequestHandler):
    def get(self):
        # Render the page
        jtr.renderContentAndPage(self, pathToContent, contentFilename, contentTemplateValues, pageTemplateValues)
