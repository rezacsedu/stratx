from sklearn.utils import resample
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize
from sklearn.ensemble import RandomForestRegressor
from timeit import default_timer as timer
from sklearn.utils import resample

import shap

from support import *
from stratx.featimp import *
from stratx.partdep import *

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# def rent_pdp():
#     X, y = load_rent(n=2_000)
#     # plot_stratpd_gridsearch(X, y, 'bedrooms', 'price')
#     # plot_stratpd_gridsearch(X, y, 'bathrooms', 'price')
#     plot_stratpd_gridsearch(X, y, 'Wvillage', 'price',
#                             min_samples_leaf_values=(2,3,5,8,10,15))
#     # plot_stratpd_gridsearch(X, y, 'latitude', 'price')
#     # plot_stratpd_gridsearch(X, y, 'longitude', 'price')


#np.random.seed(999)

n=25_000
#r = (500,600)
# r = (0,500)
_, _, df_flights = load_flights(n=n)
# df_flights = df_flights[df_flights['FLIGHT_NUMBER']>r[0]] # look at subset of flight numbers
# df_flights = df_flights[df_flights['FLIGHT_NUMBER']<r[1]] # look at subset of flight numbers
X, y = df_flights.drop('ARRIVAL_DELAY', axis=1), df_flights['ARRIVAL_DELAY']

print(f"Avg arrival delay {df_flights['ARRIVAL_DELAY'].mean()}")

# plot_stratpd_gridsearch(X, y, 'TAXI_IN', 'ARRIVAL_DELAY',
#                         min_samples_leaf_values=(3,5,10,15),
#                         min_slopes_per_x_values=(15,20,25,30,40,50),
#                         show_slope_lines=False,
#                         yrange=(-10,90)
#                         )

col = 'TAXI_OUT'
col = 'DEPARTURE_TIME_HOUR'
col = 'SCHEDULED_DEPARTURE_HOUR'

# plot_stratpd(X, y, colname='SCHEDULED_DEPARTURE_HOUR', targetname='delay',
#              show_slope_lines=False,
#              show_impact=True)
#              # yrange=(-10,100))
# plt.tight_layout()
# plt.show()
#
# plot_stratpd(X, y, colname='DEPARTURE_TIME_HOUR', targetname='delay',
#              show_slope_lines=False,
#              show_impact=True)
#              # yrange=(-10,100))
# plt.tight_layout()
# plt.show()

plot_stratpd_gridsearch(X, y, 'SCHEDULED_DEPARTURE_HOUR', 'ARRIVAL_DELAY',
                        show_impact=True)
plt.tight_layout()
plt.show()

# plot_catstratpd(X, y, 'DEPARTURE_TIME_MIN', 'ARRIVAL_DELAY',
#                 min_samples_leaf=10,
#                 sort=None,
#                 # yrange=(-110,250),
#                 show_xticks=False,
#                 show_mean_line=True,
#                 style='scatter')
# plt.tight_layout()
# plt.show()

# I = spearmans_importances(X, y)
# print(I)

# plot_stratpd_gridsearch(X, y, col, 'ARRIVAL_DELAY',
#                         min_samples_leaf_values=(10,15,20,30),
#                         min_slopes_per_x_values=(5,10,15,20,25),
#                         show_slope_lines=False,
#                         yrange=(-10,90)
#                         )

# #
# plot_catstratpd(X, y, 'SCHEDULED_DEPARTURE_HOUR', 'ARRIVAL_DELAY',
#                 min_samples_leaf=10,
#                 # sort=None,
#                 yrange=(-110,250),
#                 show_xticks=False,
#                 style='scatter')
# plt.title(f"X range {r[0]}..{r[1]} with {n} records")

# I = importances(X, y,
#                 min_samples_leaf=10, # default
#                 min_slopes_per_x=20,
#                 catcolnames={'AIRLINE',
#                              'ORIGIN_AIRPORT', 'DESTINATION_AIRPORT',
#                              'FLIGHT_NUMBER',
#                              'DAY_OF_WEEK', 'dayofyear'},
#                 )
# print(I)

# plot_catstratpd_gridsearch(X, y, col, 'ARRIVAL_DELAY',
#                            yrange=(-100,500))
# plt.savefig(f"/Users/parrt/Desktop/flight-{col}-cat.png", pad_inches=0, dpi=150)


plt.tight_layout()
# rent_pdp()
# plt.savefig(f"/Users/parrt/Desktop/flight-{col}.png", pad_inches=0, dpi=150)
plt.show()