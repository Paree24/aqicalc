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
            (0, 40),
            (41, 80),
            (81, 120),
            (121, 200),
            (201, inf)],
        'bp': {
            POLLUTANT_O3_8H: [
                (Decimal('0'), Decimal('100')),
                (Decimal('101'), Decimal('130')),
                (Decimal('131'), Decimal('160')),
                (Decimal('161'), Decimal('200')),
                (Decimal('201'), inf),
            ],
            POLLUTANT_O3_1H: [
                (Decimal('0'), Decimal('100')),
                (Decimal('101'), Decimal('130')),
                (Decimal('131'), Decimal('160')),
                (Decimal('161'), Decimal('200')),
                (Decimal('201'), inf),
            ],
            POLLUTANT_PM10: [
                (Decimal('0'), Decimal('50')),
                (Decimal('51'), Decimal('100')),
                (Decimal('101'), Decimal('150')),
                (Decimal('151'), Decimal('250')),
                (Decimal('251'), inf),
            ],
            POLLUTANT_PM25: [
                (Decimal('0'), Decimal('25')),
                (Decimal('26'), Decimal('50')),
                (Decimal('51'), Decimal('75')),
                (Decimal('76'), Decimal('125')),
                (Decimal('126'), inf),
            ],
            POLLUTANT_CO_8H: [
                (Decimal('0.0'), Decimal('10.0')),
                (Decimal('10.1'), Decimal('13.0')),
                (Decimal('13.1'), Decimal('15.0')),
                (Decimal('15.1'), Decimal('17.0')),
                (Decimal('17.1'), inf),
            ],
            POLLUTANT_SO2_1H: [
                (Decimal('0'), Decimal('20')),
                (Decimal('21'), Decimal('40')),
                (Decimal('41'), Decimal('365')),
                (Decimal('366'), Decimal('800')),
                (Decimal('801'), inf),
            ],
            POLLUTANT_NO2_1H: [
                (Decimal('0'), Decimal('200')),
                (Decimal('201'), Decimal('240')),
                (Decimal('241'), Decimal('320')),
                (Decimal('321'), Decimal('1130')),
                (Decimal('1131'),inf),
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
