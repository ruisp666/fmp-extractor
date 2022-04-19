# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 08:54:23 2021

@author: sapereira
"""
import json
from urllib.request import urlopen


def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)
