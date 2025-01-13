import math

import numpy
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

from InferenceLab.calibration import volts_to_angle
from InferenceLab.objects import Limits
from InferenceLab.read_data import parse_data_from_samples


def create_assumed_n_slit_function(N):
    def assumed_function_one_slit(theta, i_0, alpha, offset):
        angle_in_rad = theta - offset
        x = alpha * np.sin(angle_in_rad)
        return i_0 * ((np.sin(x) / x) ** 2)

    def assumed_n_slit_function(theta, i_0, alpha, beta, offset):
        angle_in_rad = theta - offset
        x_1 = alpha * np.sin(angle_in_rad)
        x_2 = beta * np.sin(angle_in_rad)
        return i_0 * ((np.sin(x_1) / x_1) ** 2) * (np.sin(N * x_2) / np.sin(x_2)) ** 2

    def assumed_anti_slit_function(theta, i_0, alpha, beta, offset):
        return create_assumed_n_slit_function(2)(theta, i_0, alpha, beta, offset)

    def assumed_infty_slit_function(theta, i_0, alpha, beta, offset):
        angle_in_rad = theta - offset
        x_1 = alpha * np.sin(angle_in_rad)
        x_2 = beta * np.sin(angle_in_rad)
        return i_0 * ((np.sin(x_1) / x_1) ** 2) / (2 * (np.sin(x_2)) ** 2)

    if N == 1 or N == "antislit":
        return assumed_function_one_slit
    if math.isinf(N):
        return assumed_infty_slit_function
    else:
        return assumed_n_slit_function


def get_init_params(N, slit_width_init, slit_dist_init, offset_init, i0_init, wavelen, alpha=None):
    if not alpha:
        if slit_width_init is None:
            alpha = None
        else:
            alpha = np.pi * slit_width_init / wavelen
    if N == 1 or N=="antislit":
        return [i0_init, alpha, offset_init]
    else:
        return [i0_init, alpha, np.pi * slit_dist_init / wavelen, offset_init]


def run(day, N, init_params, limits: Limits, data_name, wavelen, slit_width_init, slit_dist_init):
    data = [list(row) for row in parse_data_from_samples(day, data_name)]
    intensities_raw, thetas_volts = data[-2:]
    intensities_pos = -np.array(intensities_raw)
    thetas_deg = volts_to_angle(day, numpy.array(thetas_volts))
    filtered_thetas, filtered_intensities = [], []

    for i, intense in enumerate(intensities_pos):
        if intense < limits.max_intensity and limits.min_theta < thetas_deg[i] < limits.max_theta:
            filtered_thetas.append(thetas_deg[i])
            filtered_intensities.append(intense)

    results, loss = fit_curve(N, filtered_thetas, filtered_intensities, init_params)
    print(results)
    fit_vs_actual(N, results, thetas_deg, intensities_pos, data_name, wavelen, slit_width_init, slit_dist_init, limits)


def fit_vs_actual(N, results, thetas_rad, intensities, data_name, wavelen, slit_width_init, slit_dist_init, limits):
    title = ""
    i0_final = results[0]
    width_final = results[1] * wavelen / np.pi
    offset_final = 0.0
    if N == 1:
        title += f"1 slit, width={slit_width_init:.2e}[m]"
        title += f"\nMeasured width={width_final:.2e}[m]"
    elif N == "antislit":
        title += f"1 anti-slit separation={slit_dist_init:.2e}[m]"
        title += f"\nMeasured separation={width_final:.2e}[m]"
    elif N==float('inf'):
        title += f"Grating separation={slit_dist_init:.2e}[m]"
    else:
        dist_final = results[2] * wavelen / np.pi
        offset_final = results[3]
        title += f"{N} slits, width={slit_width_init:.2e}[m], separation={slit_dist_init:.2e}[m]"

        title += f"\nMeasured width={width_final:.2e}[m], measured separation={dist_final:.2e}[m]"

    plt.figure(dpi=400)
    plt.suptitle(title, fontsize=10)
    plt.figtext(0.01, 0.01, f"Filename: {data_name}", fontsize=6)

    x = np.array(thetas_rad, dtype=float)
    y = create_assumed_n_slit_function(N)(x, *results)

    plt.ylim(0, limits.max_intensity)
    plt.plot(x, intensities, label="Measured intensity", linewidth=0.5)
    plt.plot(x, y, label="Fitted intensity", linewidth=0.5)
    plt.legend(loc='upper right')
    plt.xlabel("Angle [rad]")
    plt.ylabel("Intensity [volt]")
    plt.show()


def fit_curve(N, thetas, intensities, init_params):
    assumed_function = create_assumed_n_slit_function(N)

    param = curve_fit(assumed_function, thetas, intensities, p0=init_params, maxfev=10000)
    return param
