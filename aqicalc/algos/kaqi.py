# -*- coding: utf-8 -*-

from decimal import *

from aqicalc.constants import (POLLUTANT_PM25, POLLUTANT_PM10,
                          POLLUTANT_O3_8H, POLLUTANT_O3_1H,
                          POLLUTANT_CO_8H, POLLUTANT_SO2_1H,
                          POLLUTANT_NO2_1H)
from aqicalc.algos.base import PiecewiseAQI
from math import inf

class AQI(PiecewiseAQI):
    """Implementation of the EPA AQI algorithm.
    """

    piecewise = {
        'aqi': [
            (0, 50),
            (51, 100),
            (101, 150),
            (151, 200),
            (201, 300),
            (301, 500),
            ],
        'bp': {
            POLLUTANT_O3_8H: [
                (Decimal('0.000'), Decimal('0.054')),
                (Decimal('0.055'), Decimal('0.070')),
                (Decimal('0.071'), Decimal('0.085')),
                (Decimal('0.086'), Decimal('0.105')),
                (Decimal('0.106'), Decimal('0.2')),
                (Decimal('0.21'), inf)
            ],
            POLLUTANT_O3_1H: [
                (0, 0),
                (0, 0),
                (Decimal('0.125'), Decimal('0.164')),
                (Decimal('0.165'), Decimal('0.204')),
                (Decimal('0.205'), Decimal('0.404')),
                (Decimal('0.405'), Decimal('0.604')),
            ],
            POLLUTANT_PM10: [
                (Decimal('0'), Decimal('100')),
                (Decimal('100.1'), Decimal('350')),
                (Decimal('350.1'), Decimal('400')),
                (Decimal('400.1'), Decimal('450')),
                (Decimal('450.1'), Decimal('500')),
                (Decimal('500.1'), inf),
            ],
            POLLUTANT_PM25: [
                (Decimal('0.0'), Decimal('25.0')),
                (Decimal('25.1'), Decimal('75.0')),
                (Decimal('75.1'), Decimal('100')),
                (Decimal('100.1'), Decimal('150.4')),
                (Decimal('150.5'), Decimal('250.4')),
                (Decimal('250.5'), inf),
            ],
            POLLUTANT_CO_8H: [
                (Decimal('0.0'), Decimal('4.4')),
                (Decimal('4.5'), Decimal('9.4')),
                (Decimal('9.5'), Decimal('12.4')),
                (Decimal('12.5'), Decimal('15.4')),
                (Decimal('15.5'), Decimal('30.4')),
                (Decimal('30.5'), inf),
            ],
            POLLUTANT_SO2_1H: [
                (Decimal('0'), Decimal('35')),
                (Decimal('36'), Decimal('75')),
                (Decimal('76'), Decimal('185')),
                (Decimal('186'), Decimal('304')),
                (Decimal('305'), Decimal('604')),
                (Decimal('605'), inf),
            ],
            POLLUTANT_NO2_1H: [
                (Decimal('0'), Decimal('53')),
                (Decimal('54'), Decimal('100')),
                (Decimal('101'), Decimal('360')),
                (Decimal('361'), Decimal('649')),
                (Decimal('650'), Decimal('1249')),
                (Decimal('1250'), inf),
            ],
        },
        'prec': {
            POLLUTANT_O3_8H: Decimal('.001'),
            POLLUTANT_O3_1H: Decimal('.001'),
            POLLUTANT_PM10: Decimal('1.'),
            POLLUTANT_PM25: Decimal('.1'),
            POLLUTANT_CO_8H: Decimal('.1'),
            POLLUTANT_SO2_1H: Decimal('1.'),
            POLLUTANT_NO2_1H: Decimal('1.'),
        },
        'units': {
            POLLUTANT_O3_8H: 'ppm',
            POLLUTANT_O3_1H: 'ppm',
            POLLUTANT_PM10: 'µg/m³',
            POLLUTANT_PM25: 'µg/m³',
            POLLUTANT_CO_8H: 'ppm',
            POLLUTANT_SO2_1H: 'ppb',
            POLLUTANT_NO2_1H: 'ppb',
        },
    }
