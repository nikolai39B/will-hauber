"""
FILE:
    notFound.py
 
DIRECTORY:
    will-hauber/source/pages

DESCRIPTION:
    This file manages any requests that weren't mapped elsewhere.
"""

# Python
import os

# GAE
import webapp2

# Application
import requestHandler as rh
import source.utilities.jinjaTemplateRenderer as jtr
	
# Page Template
pathToContent = os.path.join(rh.rootDir, 'html/content')
contentFilename = 'notFound.html'
pageTemplateValues = { 
    'page_title': 'Will Hauber',
    'content_title': '404 Error - Page Not Found',
}

class NotFound(webapp2.RequestHandler):
    def get(self):
        # Render the page
        jtr.renderContentAndPage(self, pathToContent, contentFilename, {}, pageTemplateValues)
