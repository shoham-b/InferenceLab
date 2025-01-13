import InferenceLab
from InferenceLab.find_curve import get_init_params, run
from InferenceLab.objects import Limits

day = 0
wavelen = 633e-9  # in m


def run_day0():
    data1()

    # -------------------------------------------------------------------------------
    data2()

    # -------------------------------------------------------------------------------
    data3()
    #
    # -------------------------------------------------------------------------------
    data4()

    # -------------------------------------------------------------------------------
    data5()


def data5():
    MAX_INTENSITY = 10
    min_theta = -10
    max_theta = 10
    data_name = "data 5 2 slits 004mm 05mm.txt"
    N = 2
    slit_width_init = 0.04e-3  # in m
    slit_dist_init = 0.5e-3  # in m. only relevant for multiple slits
    offset_init = -5.2e-2  # in radians
    i0_init = 1.7  # arbitrary units (the intensity is proportional to this)
    init_params = get_init_params(N, slit_width_init, slit_dist_init, offset_init, i0_init, wavelen)
    limit = Limits(max_intensity=MAX_INTENSITY, min_theta=min_theta, max_theta=max_theta)
    run(day, N, init_params, limit, data_name, wavelen, slit_width_init, slit_dist_init)


def data4():
    MAX_INTENSITY = 0.8
    min_theta = -10
    max_theta = 10
    data_name = "data 4 2 slits 004mm, 025mm.txt"
    N = 2
    slit_width_init = 0.04e-3  # in m
    slit_dist_init = 0.25e-3  # in m. only relevant for multiple slits
    offset_init = -5.2e-2  # in radians
    i0_init = 1.7  # arbitrary units (the intensity is proportional to this)
    init_params = get_init_params(N, slit_width_init, slit_dist_init, offset_init, i0_init, wavelen)
    limit = Limits(max_intensity=MAX_INTENSITY, min_theta=min_theta, max_theta=max_theta)
    run(day, N, init_params, limit, data_name, wavelen, slit_width_init, slit_dist_init)


def data3():
    MAX_INTENSITY = 9
    min_theta = -7
    max_theta = -0.024
    data_name = "data 3 (more points).txt"
    N = 1
    slit_width_init = 0.2e-3  # in m
    slit_dist_init = None  # in m. only relevant for multiple slits
    offset_init = -5.067e-2  # in radians
    i0_init = 1.37e2  # arbitrary units (the intensity is proportional to this)
    alpha = 7.73e2

    init_params = get_init_params(N, slit_width_init, slit_dist_init, offset_init, i0_init, wavelen, alpha)
    limit = Limits(max_intensity=MAX_INTENSITY, min_theta=min_theta, max_theta=max_theta)
    run(day, N, init_params, limit, data_name, wavelen, slit_width_init, slit_dist_init)


def data2():
    MAX_INTENSITY = 6
    min_theta = -10
    max_theta = 10
    data_name = "data 2 (same measurement as 1).txt"
    N = 1
    slit_width_init = 0.2e-3  # in m
    slit_dist_init = 0.5e-3  # in m. only relevant for multiple slits
    offset_init = -5.067e-2  # in radians
    i0_init = 1.57  # arbitrary units (the intensity is proportional to this)
    init_params = get_init_params(N, slit_width_init, slit_dist_init, offset_init, i0_init, wavelen)
    limit = Limits(max_intensity=MAX_INTENSITY, min_theta=min_theta, max_theta=max_theta)
    run(day, N, init_params, limit, data_name, wavelen, slit_width_init, slit_dist_init)


def data1():
    MAX_INTENSITY = 10
    min_theta = -10
    max_theta = 10
    data_name = "data 1 slit 02 shutter 01.txt"
    N = 1
    slit_width_init = 0.2e-3  # in m
    slit_dist_init = 0.5e-3  # in m. only relevant for multiple slits
    offset_init = -5.2e-2  # in radians
    i0_init = 1.7  # arbitrary units (the intensity is proportional to this)
    init_params = get_init_params(N, slit_width_init, slit_dist_init, offset_init, i0_init, wavelen)
    limit = Limits(max_intensity=MAX_INTENSITY, min_theta=min_theta, max_theta=max_theta)
    run(day, N, init_params, limit, data_name, wavelen, slit_width_init, slit_dist_init)

# -------------------------------------------------------------------------------
