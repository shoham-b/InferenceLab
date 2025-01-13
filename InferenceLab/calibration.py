import numpy

from InferenceLab.read_data import parse_calibration_samples


def volts_to_angle(day: int, volts_to_convert):
    read_calibrations = parse_calibration_samples(day)
    all_angles, all_volts = list(read_calibrations)
    interpolated = numpy.interp(volts_to_convert, all_volts, all_angles)
    in_rads = numpy.deg2rad(interpolated)
    return in_rads
