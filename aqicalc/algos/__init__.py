# -*- coding: utf-8 -*-
import pkgutil
from aqicalc.constants import ALGOS

def get_algo(algo_mod):
    """Instanciate an AQI algorithm class. If there is a problem during
    the import or instanciation, return None.

    :param algo_mod: algorithm module canonical name
    :type algo_mod: str
    """
    # try to import the algorithm module
    try:
        mod = __import__(algo_mod, fromlist=[algo_mod])
    except ImportError:
        return None

    # try to instanciate an AQI class
    try:
        return mod.AQI()
    except AttributeError:
        return None

def list_algos():
    """Return a list of available algorithms with corresponding
    pollutant
    """
    return ALGOS
