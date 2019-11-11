# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 13:00:49 2017

@author: scherer
"""

#------------------------------------------------------------------------------
# OSMnx by Geoff Boeing
# http://geoffboeing.com/2016/11/osmnx-python-street-networks/
#------------------------------------------------------------------------------

# setup
import os
path = "C:/Users/Cedric/Google Drive/Bio/Programing/Python/OSMnx/"
os.chdir(path)
import osmnx as ox
from IPython.display import Image
ox.config(log_file=True, log_console=True, use_cache=True)

# configure the inline image display
img_folder = './images'
extension = 'png'
size = 350
dpi = 900

# Configure street width pixels
street_widths = {'footway' : 0.5,
                 'steps' : 0.5,
                 'pedestrian' : 0.5,
                 'path' : 0.5,
                 'track' : 0.75,
                 'service' : 1.5,
                 'residential' : 2.5,
                 'primary' : 2.5,
                 'motorway' : 3}

# create diagrams by passing in lat-long points
place = 'Berlin-Home'
point = (52.529556, 13.345430)
fig, ax = ox.plot_figure_ground(point=point, filename=place, network_type='all', street_widths=street_widths, dpi=dpi)
Image('{}/{}.{}'.format(img_folder, place, extension), height=size, width=size)

place = 'Berlin-Work'
point = (52.506396, 13.521521)
fig, ax = ox.plot_figure_ground(point=point, filename=place, network_type='all', street_widths=street_widths, dpi=dpi)
Image('{}/{}.{}'.format(img_folder, place, extension), height=size, width=size)

place = 'SanFrancisco'
point = (37.793897, -122.402189)
fig, ax = ox.plot_figure_ground(point=point, filename=place, network_type='all', street_widths=street_widths, dpi=dpi)
Image('{}/{}.{}'.format(img_folder, place, extension), height=size, width=size)

place = 'Matera'
point = (40.666512, 16.606072)
fig, ax = ox.plot_figure_ground(point=point, filename=place, network_type='all', street_widths=street_widths, dpi=dpi)
Image('{}/{}.{}'.format(img_folder, place, extension), height=size, width=size)
