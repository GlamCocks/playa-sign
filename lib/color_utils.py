#!/usr/bin/env python

def to_RGB(color, origin_colorspace):
    
    if origin_colorspace == 'GRB':
        return [color[1], color[0], color[2]]
    else:
        return color