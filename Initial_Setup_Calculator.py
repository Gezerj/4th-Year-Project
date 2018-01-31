#!/usr/bin/python
"""
Created on Wed Oct 04 10:57:34 2017

@author: Gerwyn
"""

from __future__ import division

import numpy as np
import scipy as sc
import scipy.constants as sp
import astropy.constants as ap
import astropy.units as au
import math


""" Units"""


G = ap.G.to('cm3 / (g s2)')

M_cu = 1.991e33 * au.g

print "Mass unit : ", M_cu

dist_cu = 9.9999998e16 * au.cm

print "Distance unit : ", dist_cu

time_cu = 2.7436898e12 * au.s

print "Time unit : ", time_cu

v_cu = dist_cu / time_cu

vkms = 1e5*au.cm/au.km

vel_cu = v_cu/vkms

print "Velocity unit : ", vel_cu

rho_cu = M_cu/dist_cu**3

print "Density unit : ", rho_cu

ergs_cu = (M_cu*dist_cu**2)/time_cu**2

print "Energy unit (ergs) : ", ergs_cu


print "Energy density : ", ergs_cu/dist_cu**3


""" Calculator """


def CloudRadius(n, m_cloud):

    m_sol = ap.M_sun.to('g')

    m_p = ap.m_p.to('g')

    m_cloud_sol = m_cloud*m_sol

    r = ((3*m_cloud_sol)/(4*np.pi*1.4*m_p*n))**(1/3)

    distance_unit = 1e17  # cm

    radius = r/distance_unit

    return radius


while True:

    print " "

    print "Calculation options : "

    print " "

    print "Radius, Velocity, Time-Code, Time-Real, Crossing-Time-Ext, Crossing-Time-Int"

    print " "

    print "Optimal-Distance, Boxsize, No.Density, Second-Cloud-Distance"

    print " "

    parameter = raw_input("What to calculate or 0 to exit: ")

    if parameter == '0':

        break

    if parameter == 'radius' or parameter == 'Radius':

        n = raw_input("What is the number density, n?: ")

        n_int = np.float64(n)

        m_c = raw_input("What is the mass of the cloud, m?: ")

        m_cint = np.float64(m_c)

        Rint = CloudRadius(n_int, m_cint)

        print Rint

        decision = raw_input("New calculation (y/n)?: ")

        if decision == 'y' or decision == 'yes':

            continue

        else:

            break

    if parameter == 'velocity' or parameter == 'Velocity':

        V = raw_input("What is the velocity (Kms-1), v?: ")

        Vel = np.float(V)

        Vint = Vel/vel_cu*(au.km/au.s)

        print Vint

        decision = raw_input("New calculation (y/n)?: ")

        if decision == 'y' or decision == 'yes':

            t = 0

        else:

            break

    if parameter == 'time-code' or parameter == 'Time-Code' or parameter == 'time code':

        year_or_second = raw_input("MYears, Years or Seconds?: ")

        if year_or_second == 'MY' or year_or_second == 'my' or year_or_second == 'Myears' or year_or_second == 'MYears' or year_or_second == 'myears':

            t = raw_input("What is the time (Myear), t?: ")

            t_year = np.float64(t)*au.megayear.to('s')*au.s

            tint = t_year / time_cu

            print tint

        if year_or_second == 'Y' or year_or_second == 'y' or year_or_second == 'Years' or year_or_second == 'years' or year_or_second == 'year':

            t = raw_input("What is the time (year), t?: ")

            t_year = np.float64(t)*au.year.to('s')*au.s

            tint = t_year / time_cu

            print tint

        if year_or_second == 'S' or year_or_second == 's' or year_or_second == 'Seconds' or year_or_second == 'seconds':

            t = raw_input("What is the time (s), t?: ")

            tint = np.float(t)*au.s / time_cu

            print tint

        decision = raw_input("New calculation (y/n)?: ")

        if decision == 'y' or decision == 'yes':

            continue

        else:

            break

    if parameter == 'time-real' or parameter == 'Time-Real' or parameter == 'time real':

        t = raw_input("What is the time (code), t?: ")

        t_int = np.float(t)

        year_or_second = raw_input("MYears, Years or Seconds?: ")

        if year_or_second == 'MY' or year_or_second == 'my' or year_or_second == 'Myears' or year_or_second == 'MYears' or year_or_second == 'myears':

            t_real = (t_int * time_cu)/(au.megayear.to('s')*(au.s / au.megayear))

        if year_or_second == 'Y' or year_or_second == 'y' or year_or_second == 'Years' or year_or_second == 'years' or year_or_second == 'year':

            t_real = (t_int * time_cu)/(au.year.to('s')*(au.s / au.year))

        if year_or_second == 'S' or year_or_second == 's' or year_or_second == 'Seconds' or year_or_second == 'seconds':

            t_real = t_int * time_cu

        tint = t_real

        print tint

        decision = raw_input("New calculation (y/n)?: ")

        if decision == 'y' or decision == 'yes':

            continue

        else:

            break

    if parameter == 'crossing-time-ext' or parameter == 'Crossing-Time-Ext' or parameter == 'crossing time ext':

        Mirror = raw_input("Are the velocities of the clouds mirrored (y/n)?: ")

        if Mirror == 'y' or Mirror == 'yes':

            try:

                V1 = Vint
                V2 = -Vint

            except NameError:

                V = raw_input("What is the velocity (Code_Units), v?: ")

                V1 = np.float(V)
                V2 = -np.float(V)

        else:

            V_1 = raw_input("What is the velocity of Cloud 1 (Code_Units), v?: ")

            V_2 = raw_input("What is the velocity of Cloud 2 (Code_Units), v?: ")

            V1 = np.float(V_1)

            V2 = np.float(V_2)

        try:

            dint = L

        except NameError:

            d = raw_input("What is the seperation in terms of cloud radii (Code_Units), d?: ")

            dint = np.float(d)

        dV = V1 - V2

        T_Cross = dint/dV

        print T_Cross

        decision = raw_input("New calculation (y/n)?: ")

        if decision == 'y' or decision == 'yes':

            continue

        else:

            break

    if parameter == 'crossing-time-int' or parameter == 'Crossing-Time-Int' or parameter == 'crossing time int':

        try:

            Vint_disp

        except NameError:

            V_disp = raw_input("What is the velocity dispersion (Code_Units), v?: ")

            Vint_disp = np.float(V_disp)

        try:

            Rint

        except NameError:

            R = raw_input("What is the radius of the cloud (Code_Units), r?: ")

            Rint = np.float(R)

        T_Cross = Rint / Vint_disp

        print T_Cross

        decision = raw_input("New calculation (y/n)?: ")

        if decision == 'y' or decision == 'yes':

            continue

        else:

            break

    if parameter == 'optimal-distance' or parameter == 'Optimal-Distance' or parameter == 'optimal distance':

        Mirror = raw_input("Are the velocities of the clouds mirrored (y/n)?: ")

        if Mirror == 'y' or Mirror == 'yes':

            try:

                V1 = Vint
                V2 = -Vint

            except NameError:

                V = raw_input("What is the velocity (Code_Units), v?: ")

                V1 = np.float(V)
                V2 = -np.float(V)

        else:

            V_1 = raw_input("What is the velocity of Cloud 1 (Code_Units), v?: ")

            V_2 = raw_input("What is the velocity of Cloud 2 (Code_Units), v?: ")

            V1 = np.float(V_1)

            V2 = np.float(V_2)

        try:

            Vint_disp

        except NameError:

            V_disp = raw_input("What is the velocity dispersion (Code_Units), v?: ")

            Vint_disp = np.float(V_disp)

        try:

            Rint

        except NameError:

            R = raw_input("What is the radius of the cloud (Code_Units), r?: ")

            Rint = np.float(R)

        Tc_ratio = raw_input("How much of crossing time (Percent or Fraction)?: ")

        Tcross_ratio = np.float(Tc_ratio)

        if Tcross_ratio > 1:

            Tcross_ratio = Tcross_ratio/100

        T_Cross = (Rint / Vint_disp)

        dV = V1 - V2

        L = dV*T_Cross*Tcross_ratio

        if L <= Rint:

            print "Less than Radius    "

            print Rint

        else:

            print L

        decision = raw_input("New calculation (y/n)?: ")

        if decision == 'y' or decision == 'yes':

            continue

        else:

            break

    if parameter == 'boxsize' or parameter == 'Boxsize':

        try:

            Rint

        except NameError:

            R = raw_input("What is the radius of the cloud (Code_Units), r?: ")

            Rint = np.float(R)

        try:
            Dint = L

        except NameError:

            D = raw_input("What is the optimal distance between the two clouds (Code_Units), d?: ")

            Dint = np.float(D)

        boxsize = 4*Rint + Dint

        print "Boxsize =", boxsize

        print "Y,Z =", boxsize/2

        print "X1 =", Rint*2

        print "X2 =", Rint*2 + Dint

        decision = raw_input("New calculation (y/n)?: ")

        if decision == 'y' or decision == 'yes':

            continue

        else:

            break

    if parameter == 'no.density' or parameter == 'No.Density':

        nd = raw_input("What is the number density (Code_Units), n?: ")

        N_int = np.float(nd)*(au.cm**-3)

        D_int = N_int*(ap.m_p.to('g'))/rho_cu

        print D_int

        decision = raw_input("New calculation (y/n)?: ")

        if decision == 'y' or decision == 'yes':

            continue

        else:

            break

