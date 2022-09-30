# -*- coding: utf-8 -*-

from decimal import *

from aqicalc.constants import (POLLUTANT_PM25, POLLUTANT_PM10,
                          POLLUTANT_O3_8H, POLLUTANT_O3_1H,
                          POLLUTANT_CO_8H, POLLUTANT_SO2_1H,
                          POLLUTANT_NO2_1H)
from aqicalc.algos.base import PiecewiseAQI


class AQI(PiecewiseAQI):
    """Implementation of the EPA AQI algorithm.
    """

    piecewise = {
        'aqi': [
            (Decimal('0'), Decimal('50')),
            (Decimal('51'), Decimal('100')),
            (Decimal('101'), Decimal('199')),
            (Decimal('200'), Decimal('299')),
            (Decimal('300'), Decimal('399')),
            (Decimal('400'), Decimal(math.inf)),
        ],
        'bp': {
            POLLUTANT_O3_8H: [
                (Decimal('0'), Decimal('70')),
                (Decimal('70.1'), Decimal('140')),
                (Decimal('140.1'), Decimal('200')),
                (Decimal('200.1'), Decimal('400')),
                (Decimal('400.1'), Decimal('600')),
                (Decimal('600.1'), Decimal(math.inf)),
            ],
            POLLUTANT_O3_1H: [
                (Decimal('0'), Decimal('70')),
                (Decimal('70.1'), Decimal('140')),
                (Decimal('140.1'), Decimal('200')),
                (Decimal('200.1'), Decimal('400')),
                (Decimal('400.1'), Decimal('600')),
                (Decimal('600.1'), Decimal(math.inf)),
            ],
            POLLUTANT_PM10: [
                (Decimal('0'), Decimal('40')),
                (Decimal('40.1'), Decimal('120')),
                (Decimal('120.1'), Decimal('250')),
                (Decimal('250.1'), Decimal('420')),
                (Decimal('420.1'), Decimal('500')),
                (Decimal('500.1'), Decimal(math.inf)),
            ],
            POLLUTANT_PM25:  [
                (Decimal('0'), Decimal('20')),
                (Decimal('20.1'), Decimal('60')),
                (Decimal('60.1'), Decimal('125')),
                (Decimal('125.1'), Decimal('210')),
                (Decimal('210.1'), Decimal('250')),
                (Decimal('250.1'), Decimal(math.inf)),
            ],
            POLLUTANT_CO_8H:  [
                (Decimal('0'), Decimal('4.5')),
                (Decimal('4.6'), Decimal('9.0')),
                (Decimal('9.1'), Decimal('15')),
                (Decimal('15.1'), Decimal('30')),
                (Decimal('30.1'), Decimal('40')),
                (Decimal('40.1'), Decimal(math.inf)),
            ],
            POLLUTANT_SO2_1H: [
                (Decimal('0'), Decimal('40')),
                (Decimal('40.1'), Decimal('125')),
                (Decimal('125.1'), Decimal('800')),
                (Decimal('800.1'), Decimal('1600')),
                (Decimal('1600.1'), Decimal('2100')),
                (Decimal('2100.1'), Decimal(math.inf)),
            ],
            POLLUTANT_NO2_1H: [
                (Decimal('0'), Decimal('60')),
                (Decimal('60.1'), Decimal('260')),
                (Decimal('260.1'), Decimal('1130')),
                (Decimal('1130.1'), Decimal('2260')),
                (Decimal('2260.1'), Decimal('3000')),
                (Decimal('3000.1'), Decimal(math.inf)),
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
