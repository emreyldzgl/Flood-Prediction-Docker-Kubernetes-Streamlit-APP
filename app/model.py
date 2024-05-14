import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# import optuna

from catboost import CatBoostRegressor

from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, mean_squared_log_error

pd.set_option('display.max_columns', 30)

df = pd.read_csv("../data/flood.csv")
df.head()


############# FONKSIYONLAR ##################

def num_summary(dataframe, numerical_cols, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_cols].describe(quantiles).T)

    if plot:
        num_col = 4
        num_row = 6

        fig, axes = plt.subplots(num_row, num_col, figsize=(15, 5 * num_row))
        axes = axes.flatten()  # 2D convert 1D

        for i, column in enumerate(numerical_cols):
            axes[i].hist(dataframe[column], bins=50)
            axes[i].set_title(column)

        plt.tight_layout()
        plt.show()


def outlier_thresholds(dataframe, variable, low_quantile=0.05, up_quantile=0.95):
    quantile_one = dataframe[variable].quantile(low_quantile)
    quantile_three = dataframe[variable].quantile(up_quantile)
    interquantile_range = quantile_three - quantile_one
    up_limit = quantile_three + 1.5 * interquantile_range
    low_limit = quantile_one - 1.5 * interquantile_range
    return low_limit, up_limit


def check_outlier(dataframe, col_name):
    low_limit, up_limit = outlier_thresholds(dataframe, col_name)
    if dataframe[(dataframe[col_name] > up_limit) | (dataframe[col_name] < low_limit)].any(axis=None):
        return True
    else:
        return False


def replace_with_thresholds(dataframe, variable):
    low_limit, up_limit = outlier_thresholds(dataframe, variable)
    dataframe.loc[(dataframe[variable] < low_limit), variable] = low_limit
    dataframe.loc[(dataframe[variable] > up_limit), variable] = up_limit


num_cols = ['MonsoonIntensity', 'TopographyDrainage', 'RiverManagement',
            'Deforestation', 'Urbanization', 'ClimateChange', 'DamsQuality',
            'Siltation', 'AgriculturalPractices', 'Encroachments',
            'IneffectiveDisasterPreparedness', 'DrainageSystems',
            'CoastalVulnerability', 'Landslides', 'Watersheds',
            'DeterioratingInfrastructure', 'PopulationScore', 'WetlandLoss',
            'InadequatePlanning', 'PoliticalFactors', 'FloodProbability']

num_summary(df, num_cols, plot=True)

corr = df[num_cols].corr()
sns.set(rc={'figure.figsize': (12, 12)})
sns.heatmap(corr, cmap="RdPu")
plt.show(block=True)



X = df[['MonsoonIntensity', 'TopographyDrainage', 'RiverManagement',
        'Deforestation', 'Urbanization', 'ClimateChange', 'DamsQuality',
        'Siltation', 'AgriculturalPractices', 'Encroachments',
        'IneffectiveDisasterPreparedness', 'DrainageSystems',
        'CoastalVulnerability', 'Landslides', 'Watersheds',
        'DeterioratingInfrastructure', 'PopulationScore', 'WetlandLoss',
        'InadequatePlanning', 'PoliticalFactors']]
y = df[['FloodProbability']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=17)

"""
def objective(trial):
    params = {
        "iterations": 1000,
        "learning_rate": trial.suggest_float("learning_rate", 1e-3, 0.1, log=True),
        "depth": trial.suggest_int("depth", 4, 12),
        "subsample": trial.suggest_float("subsample", 0.05, 1.0),
        "colsample_bylevel": trial.suggest_float("colsample_bylevel", 0.05, 1.0),
        "min_data_in_leaf": trial.suggest_int("min_data_in_leaf", 1, 100),
    }

    model = CatBoostRegressor(**params, silent=True)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    r2 = r2_score(predictions, y_test)
    return r2

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=30)


print('Best hyperparameters:', study.best_params)
print('Best R2:', study.best_value)
"""


best_params = {'learning_rate': 0.09956443667034971, 'depth': 11, 'subsample': 0.5508700989725369, 'colsample_bylevel': 0.7810820091677154, 'min_data_in_leaf': 89}
reg = CatBoostRegressor(**best_params, verbose=False, random_state=17)
reg.fit(X_train, y_train)


joblib.dump(reg, 'model.pkl')
