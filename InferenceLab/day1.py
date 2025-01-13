from InferenceLab.find_curve import get_init_params, run
from InferenceLab.objects import Limits

day = 1
wavelen = 633e-9  # in m


def run_day1():
    data7()
    # -------------
    data8()
    # -------------
    data9()
    # -------------
    data13()
    # -------------
    data14()
    # -------------


def data7():
    MAX_INTENSITY = 1
    min_theta = -0.02
    max_theta = 0.01
    data_name = "data 7 (same as 6).txt"
    N = 2
    slit_width_init = 0.08e-3  # in m
    slit_dist_init = 0.25e-3  # in m. only relevant for multiple slits
    offset_init = -0.001918  # in radians
    i0_init = 1e2  # arbitrary units (the intensity is proportional to this)
    init_params = get_init_params(N, slit_width_init, slit_dist_init, offset_init, i0_init, wavelen)
    limit = Limits(max_intensity=MAX_INTENSITY, min_theta=min_theta, max_theta=max_theta)
    run(day, N, init_params, limit, data_name, wavelen, slit_width_init, slit_dist_init)


def data8():
    MAX_INTENSITY = 0.25
    min_theta = -0.03
    max_theta = 0.01
    data_name = "data 8 (5 slits 0125 004).txt"
    N = 5
    slit_width_init = 0.04e-3  # in m
    slit_dist_init = 0.125e-3  # in m. only relevant for multiple slits
    offset_init = -0.001918  # in radians
    i0_init = 1e1  # arbitrary units (the intensity is proportional to this)
    init_params = get_init_params(N, slit_width_init, slit_dist_init, offset_init, i0_init, wavelen)
    print(f"init params {init_params}")
    limit = Limits(max_intensity=MAX_INTENSITY, min_theta=min_theta, max_theta=max_theta)
    run(day, N, init_params, limit, data_name, wavelen, slit_width_init, slit_dist_init)


def data9():
    MAX_INTENSITY = 0.1
    min_theta = -0.03
    max_theta = 0.01
    data_name = "data 9 (4 slits 0125 004).txt"
    N = 4
    slit_width_init = 0.04e-3  # in m
    slit_dist_init = 0.125e-3  # in m. only relevant for multiple slits
    offset_init = -0.001918  # in radians
    i0_init = 1e1  # arbitrary units (the intensity is proportional to this)
    init_params = get_init_params(N, slit_width_init, slit_dist_init, offset_init, i0_init, wavelen)
    print(f"init params {init_params}")
    limit = Limits(max_intensity=MAX_INTENSITY, min_theta=min_theta, max_theta=max_theta)
    run(day, N, init_params, limit, data_name, wavelen, slit_width_init, slit_dist_init)

def data10():
    MAX_INTENSITY = 9
    min_theta = -0.02
    max_theta = 0.01
    data_name = "data 10 80 lines per something.txt"
    N = float('inf')
    slit_width_init = slit_dist_init=1.250e-3  # in m

    offset_init = -0.001918  # in radians
    i0_init = 1e2  # arbitrary units (the intensity is proportional to this)
    init_params = get_init_params(N, slit_width_init, slit_dist_init, offset_init, i0_init, wavelen)
    print(f"init params {init_params}")
    limit = Limits(max_intensity=MAX_INTENSITY, min_theta=min_theta, max_theta=max_theta)
    run(day, N, init_params, limit, data_name, wavelen, slit_width_init, slit_dist_init)


def data13():
    MAX_INTENSITY = 0.7
    min_theta =0.005
    max_theta =.1
    data_name = "data 13 05mm graphite (more centered).txt"
    N = "antislit"
    slit_width_init = 0.5e-3
    slit_dist_init = 0.5  # in m
    offset_init = 0  # in radians
    i0_init = 1  # arbitrary units (the intensity is proportional to this)
    init_params = get_init_params(N, slit_width_init, slit_dist_init, offset_init, i0_init, wavelen, alpha=500)
    print(f"init params {init_params}")
    limit = Limits(max_intensity=MAX_INTENSITY, min_theta=min_theta, max_theta=max_theta)
    run(day, N, init_params, limit, data_name, wavelen, slit_width_init, slit_dist_init)

def data14():
    MAX_INTENSITY = 0.7
    min_theta = -0.03
    max_theta = 0.2
    data_name = "data 14 hair.txt"

    N = "antislit"
    slit_width_init =  0.06e-3
    slit_dist_init = 6e-5  # in m
    offset_init = -2.12e-3  # in radians
    i0_init = 1e2  # arbitrary units (the intensity is proportional to this)
    init_params = get_init_params(N, slit_width_init, slit_dist_init, offset_init, i0_init, wavelen, alpha=450)
    print(f"init params {init_params}")
    limit = Limits(max_intensity=MAX_INTENSITY, min_theta=min_theta, max_theta=max_theta)
    run(day, N, init_params, limit, data_name, wavelen, slit_width_init, slit_dist_init)
