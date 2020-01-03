from sklearn.utils import resample
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize
from sklearn.ensemble import RandomForestRegressor
from timeit import default_timer as timer
from sklearn.utils import resample

import shap

from stratx.featimp import *
from support import *

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#np.random.seed(666) # good results
np.random.seed(999)

n = 5_000

X, y = load_bulldozer()

X = X.iloc[-n:]
y = y.iloc[-n:]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# now undo
X = pd.concat([X_train, X_test], axis=0)
y = pd.concat([y_train, y_test], axis=0)

plot_stratpd(X, y, colname='age', targetname='SalePrice',
             show_slope_lines=False,
             show_impact=True,
             figsize=(4,3)
             )
plt.tight_layout()
plt.savefig(f"/Users/parrt/Desktop/james-age.pdf", pad_inches=0)
plt.show()
#
# plot_stratpd(X, y, colname='YearMade', targetname='SalePrice',
#              show_slope_lines=False,
#              show_impact=True,
#              figsize=(4,3)
#              )
# plt.tight_layout()
# plt.savefig(f"/Users/parrt/Desktop/james-YearMade.pdf", pad_inches=0)
# plt.show()

# plot_stratpd(X, y, colname='saledayofyear', targetname='SalePrice',
#              min_samples_leaf=10,
#              show_slope_lines=False)
# plt.tight_layout()
# plt.show()
#
# plot_stratpd(X, y, colname='ProductSize', targetname='SalePrice',
#              show_slope_lines=False)
# plt.tight_layout()
# plt.show()


# plot_catstratpd(X, y, colname='ModelID', targetname='SalePrice',
#                 min_samples_leaf=10, sort=None,
#                 alpha=.08,
#                 show_all_deltas=False,
#                 show_xticks=False,
#                 show_impact=True,
#                 min_y_shifted_to_zero=False,
#                 figsize=(4,3))
# plt.tight_layout()
# plt.savefig(f"/Users/parrt/Desktop/james-ModelID.pdf", pad_inches=0)
# plt.show()

# I = importances(X, y, catcolnames={'AC', 'ModelID', 'ProductSize'},
#                 min_samples_leaf=10,
#                 min_slopes_per_x=5)
# print(I)


col = 'age'
# col = 'ProductSize'

# plot_stratpd_gridsearch(X, y, colname=col, targetname='SalePrice',
#                         min_samples_leaf_values=(10,20,30),
#                         min_slopes_per_x_values=(5,10,20,30),
#                         show_slope_lines=False,
#                         yrange=None)

# plot_catstratpd_gridsearch(X, y, 'ProductSize', 'SalePrice',
#                            min_samples_leaf_values=(5,10,15,20),
#                            sort=None,
#                            show_xticks=False,
#                            show_mean_line=True,
#                            show_all_cat_deltas=False,
#                            style='scatter',
#                            min_y_shifted_to_zero=False)

# plot_catstratpd(X, y, 'YearMade', 'SalePrice',
#                 min_samples_leaf=10,
#                 show_mean_line=True,
#                 sort=None,
#                 show_xticks=False,
#                 min_y_shifted_to_zero=False)

plt.tight_layout()
# plt.savefig(f"/Users/parrt/Desktop/james-{col}.png", pad_inches=0, dpi=150)
plt.show()