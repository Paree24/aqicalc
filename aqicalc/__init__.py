# -*- coding: utf-8 -*-

from aqicalc.constants import *

from aqicalc.algos import get_algo, list_algos

__author__ = "Stefan \"hr\" Berder"
__contact__ = "hr@bonz.org"
__license__ = "BSD 3-Clause"
__version__ = "0.6.1"


class InvalidConversionArguments(Exception):
    pass


def to_iaqi(elem, cc, algo=ALGO_EPA):
    """Calculate an intermediate AQI for a given pollutant. This is the
    heart of the algo.

    .. warning:: the concentration is passed as a string so
        :class:`decimal.Decimal` doesn't act up with binary floats.

    :param elem: pollutant constant
    :type elem: int
    :param cc: pollutant contentration (µg/m³ or ppm)
    :type cc: str
    :param algo: algorithm module canonical name
    :type algo: str
    """
    _aqi = get_algo(algo)
    return _aqi.iaqi(elem, cc)


def to_aqi(ccs, algo=ALGO_EPA):
    """Calculate the AQI based on a list of pollutants

    :param ccs: a list of tuples of pollutants concentrations with
                pollutant constant and concentration as values
    :type ccs: list
    :param algo: algorithm module name
    :type algo: str
    """
    _aqi = get_algo(algo)
    return _aqi.aqi(ccs)


def to_cc(elem, iaqi, algo=ALGO_EPA):
    """Calculate a concentration for a given pollutant.

    .. warning:: the intermediate AQI is passed as a string

    :param elem: pollutant constant
    :type elem: int
    :param cc: intermediate AQI
    :type iaqi: str
    :param algo: algorithm module canonical name
    :type algo: str
    """
    _aqi = get_algo(algo)
    return _aqi.cc(elem, iaqi)


def get_units(algo=ALGO_EPA):
    """
    Returns units
    """
    _aqi = get_algo(algo)
    return _aqi.get_units()

def convert_grams_to_parts(x, pollutant):
    """
    Converts ug/m3 to ppb for O3, NO2 and SO2 and mg/m3 to ppm for CO.
    Note: If you are looking to convert ug/m3 for CO, multiply the results by 1000
    If you are looking to convert ppm to ppb multiply results by 1000 and divide for vice versa
    """
    if pollutant == POLLUTANT_O3_1H or pollutant == POLLUTANT_O3_8H:
        return x/1.96  # ugm3 to ppb
    if pollutant == POLLUTANT_NO2_1H or pollutant == POLLUTANT_NO2_24H:
        return x/1.88  # ugm3 to ppb
    if pollutant == POLLUTANT_CO_1H or pollutant == POLLUTANT_CO_24H or pollutant == POLLUTANT_CO_8H:
        return x/1.15  # mgm3 to ppb
    if pollutant == POLLUTANT_SO2_1H or pollutant == POLLUTANT_SO2_24H:
        return x/2.62  # ugm3 to ppb
    else:
        raise InvalidConversionArguments('Pollutant or Value Invalid')

def convert_ppm_to_ppb(ppm):
    "converts ppm to ppb"
    return ppm*1000

def convert_ppb_to_ppm(ppb):
    "converts ppb to ppm"
    return ppb/1000

def convert_pphm_to_ppb(pphm):
    "converts pphm to ppb"
    return pphm*10

def convert_ppb_to_pphm(ppb):
    "converts ppb to pphm"
    return ppb/10

def convert_pphm_to_ppm(pphm):
    "converts pphm to ppm"
    return pphm/100

def convert_ppm_to_pphm(ppm):
    "converts ppm to pphm"
    return ppm*100

def convert_milli_to_micro(milli):
    "converts mg/m3 to ug/m3"
    return milli*1000

def convert_micro_to_milli(micro):
    "converts ug/m3 to mg/m3"
    return micro/1000

def convert_parts_to_grams(x, pollutant):
    """
    Converts ppb to ug/m3 for O3, NO2 and SO2 and ppm to mg/m3 for CO.
    Note: If you are looking to convert ppb for CO, multiply the results by 1000
    If you are looking to convert ppm to ppb multiply results by 1000 and divide for vice versa
    """
    if pollutant == POLLUTANT_O3_1H or pollutant == POLLUTANT_O3_8H:
        return x*1.96  # ugm3 to ppb
    if pollutant == POLLUTANT_NO2_1H or pollutant == POLLUTANT_NO2_24H:
        return x*1.88  # ugm3 to ppb
    if pollutant == POLLUTANT_CO_1H or pollutant == POLLUTANT_CO_24H or pollutant == POLLUTANT_CO_8H:
        return x*1.15  # mgm3 to ppb
    if pollutant == POLLUTANT_SO2_1H or pollutant == POLLUTANT_SO2_24H:
        return x*2.62  # ugm3 to ppb
    else:
        raise InvalidConversionArguments('Pollutant or Value Invalid')


def console_aqi():
    """Console entry point, this function is used as an entry point to
    the 'aqi' command.
    """
    import sys
    import argparse

    parser = argparse.ArgumentParser(description="""Convert between AQI value and pollutant concentration (µg/m³ or
    ppm).""")
    parser.add_argument('-c', dest='conv', choices=['aqi', 'cc'], default='aqi',
                        help="Conversion to perform, defaults to 'aqi'")
    parser.add_argument('-l', action='store_true', dest='list',
                        help='list the available algorithms and '
                             'corresponding pollutants')
    parser.add_argument('-v', action='store_true', dest='verbose',
                        help='add IAQIs to the result')
    parser.add_argument('algo', nargs='?',
                        help='the formula to use for the AQI '
                             'calculation, use the python module path')
    parser.add_argument('measures', nargs='*', metavar='measure',
                        help='pollutant measure, format is '
                             'element_name:concentration. Unknown '
                             'pollutants are silently ignored.')
    args = parser.parse_args()

    # list available algorithms
    if args.list is True:
        for _algo in list_algos():
            print("{algo}: {elem}".format(
                algo=_algo[0], elem=', '.join(
                    ["{0} ({1})".format(elem, unit) for (elem, unit)
                     in _algo[1]])))
    else:
        # if not listing but missing other positional argument
        if args.algo is None or args.measures is None:
            sys.stderr.write("Missing algorithm or measure.\n")
            parser.print_help()
            sys.exit(1)
        _aqi = get_algo(args.algo)
        # couln't load the algo module or instanciate AQI class
        if _aqi is None:
            sys.stderr.write("Unknown algorithm or module is missing an "
                             "AQI class\n")
            parser.print_help()
            sys.exit(1)
        if args.conv == 'aqi':
            ccs = []
            for measure in args.measures:
                (elem, cc) = measure.split(':')
                ccs.append((elem, cc))

            ret = _aqi.aqi(ccs, iaqis=args.verbose)
            if args.verbose is True:
                iaqis = []
                for (constant, iaqi) in ret[1].items():
                    iaqis.append(constant + ':' + str(iaqi))
                sys.stdout.write(' '.join(iaqis) + "\n")
                sys.stdout.write(str(ret[0]) + "\n")
            else:
                sys.stdout.write(str(ret) + "\n")
        else:
            iaqis = []
            for measure in args.measures:
                (elem, iaqi) = measure.split(':')
                iaqis.append((elem, iaqi))

            ret = []
            for iaqi in iaqis:
                ret.append((iaqi[0], _aqi.cc(iaqi[0], iaqi[1])))
            if len(ret) == 1:
                sys.stdout.write(str(ret[0][1]) + "\n")
            elif len(ret) > 1:
                ccs = []
                for (elem, cc) in ret:
                    if cc is None:
                        ccs.append(elem + ':na')
                    else:
                        ccs.append(elem + ':' + str(cc))
                sys.stdout.write('\n'.join(ccs) + "\n")

    # end the script without a problem
    sys.exit(0)
