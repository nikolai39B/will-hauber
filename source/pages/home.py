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
}
pageTemplateValues = { 
    'buttons_side': [
        ('', 'Home'),
        ('contact_me', 'Contact Me'),
        ('resume', 'Resume')
    ],
    'content_title': 'Home',
    'page_title': 'Will Hauber'
}

class Home(webapp2.RequestHandler):
    def get(self):
        # Render the page
        jtr.renderContentAndPage(self, pathToContent, contentFilename, contentTemplateValues, pageTemplateValues)
