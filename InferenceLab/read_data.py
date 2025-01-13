from pathlib import Path

current_path = Path(__file__)
samples_path = current_path.parent.parent / "samples"


def parse_data_file(filepath):
    file = filepath.open()
    metadata_line = file.readline()
    while metadata_line != '\n':
        metadata_line = file.readline()
    headers = file.readline()
    as_floats = ((float(i) for i in line.split()) for line in file.readlines())
    return zip(*as_floats)


def parse_data_from_samples(day: int, filename):
    return parse_data_file(current_path.parent.parent / "samples" / f"day {day}" / filename)


def parse_calibration_samples(day: int):
    calibration_file = samples_path / f"day {day}" / "calibration.txt"
    as_floats = list((float(i) for i in line.split(',')) for line in calibration_file.open().readlines())
    return zip(*reversed(as_floats))
