"""
FILE:
    requestHandler.py
 
DIRECTORY:
    will-hauber

DESCRIPTION:
    This file contains the app field, which maps requests to their appropriate
    handler. It also sets up the environment.
"""

# Python
import os
import sys

# GAE
import webapp2

# Application
rootDir = os.path.dirname(__file__) # Be sure to do this before the below imports

from source.pages import home

#------#
# Data #
#------#
app = webapp2.WSGIApplication([ 
    ('/', home.Home)#,

    #('/.*', notFound.NotFound)
], debug=True)