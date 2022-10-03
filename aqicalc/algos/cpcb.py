# -*- coding: utf-8 -*-

from decimal import *

from aqicalc.constants import *
from aqicalc.algos.base import PiecewiseAQI
from math import inf

class AQI(PiecewiseAQI):
    """Implementation of the CPCB AQI algorithm, CO is in mg/m3 units is in ug/3 for all except CO.
    """

    piecewise = {
        'aqi': [
            (0, 50),
            (51, 100),
            (101, 200),
            (201, 300),
            (301, 400),
            (301, 400),
            (401, inf)],
        'bp': {
            POLLUTANT_O3_8H: [
                (Decimal('0'), Decimal('50')),
                (Decimal('51'), Decimal('100')),
                (Decimal('101'), Decimal('168')),
                (Decimal('169'), Decimal('208')),
                (Decimal('209'), Decimal('748')),
                (Decimal('748'), inf),
            ],
            POLLUTANT_O3_1H: [
                (Decimal('0'), Decimal('50')),
                (Decimal('51'), Decimal('100')),
                (Decimal('101'), Decimal('168')),
                (Decimal('169'), Decimal('208')),
                (Decimal('209'), Decimal('748')),
                (Decimal('748'), inf),
            ],
            POLLUTANT_PM10: [
                (Decimal('0'), Decimal('50')),
                (Decimal('51'), Decimal('100')),
                (Decimal('101'), Decimal('250')),
                (Decimal('251'), Decimal('350')),
                (Decimal('351'), Decimal('430')),
                (Decimal('430'), inf),
            ],
            POLLUTANT_PM25: [
                (Decimal('0'), Decimal('30')),
                (Decimal('31'), Decimal('60')),
                (Decimal('61'), Decimal('90')),
                (Decimal('91'), Decimal('120')),
                (Decimal('121'), Decimal('250')),
                (Decimal('250'), inf),
            ],
            POLLUTANT_CO_8H: [
                (Decimal('0.0'), Decimal('1.0')),
                (Decimal('1.1'), Decimal('2.0')),
                (Decimal('2.1'), Decimal('10.0')),
                (Decimal('10.1'), Decimal('17.0')),
                (Decimal('17.1'), Decimal('34.0')),
                (Decimal('34.1'), inf),
            ],
            POLLUTANT_SO2_1H: [
                (Decimal('0'), Decimal('40')),
                (Decimal('41'), Decimal('80')),
                (Decimal('81'), Decimal('380')),
                (Decimal('381'), Decimal('800')),
                (Decimal('801'), Decimal('1600')),
                (Decimal('1600'), inf),
            ],
            POLLUTANT_NO2_1H: [
                (Decimal('0'), Decimal('40')),
                (Decimal('41'), Decimal('80')),
                (Decimal('81'), Decimal('180')),
                (Decimal('181'), Decimal('280')),
                (Decimal('281'), Decimal('400')),
                (Decimal('400'), inf),
            ],
        },
        'prec': {
            POLLUTANT_O3_8H: Decimal('.1'),
            POLLUTANT_O3_1H: Decimal('.1'),
            POLLUTANT_PM10: Decimal('1.'),
            POLLUTANT_PM25: Decimal('.1'),
            POLLUTANT_CO_8H: Decimal('.1'),
            POLLUTANT_SO2_1H: Decimal('1.'),
            POLLUTANT_NO2_1H: Decimal('1.'),
        },
        'units': {
            POLLUTANT_O3_8H: 'µg/m³',
            POLLUTANT_O3_1H: 'µg/m³',
            POLLUTANT_PM10: 'µg/m³',
            POLLUTANT_PM25: 'µg/m³',
            POLLUTANT_CO_8H: 'mg/m³',
            POLLUTANT_SO2_1H: 'µg/m³',
            POLLUTANT_NO2_1H: 'µg/m³',
        },
    }
