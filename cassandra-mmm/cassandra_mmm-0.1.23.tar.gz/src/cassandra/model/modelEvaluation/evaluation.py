import pandas as pd
import numpy as np
from sklearn import metrics
import plotly.graph_objects as go


def show_nrmse(y_actual, y_pred, verbose = False):
    # normalized root mean square error
    value = round(np.sqrt(metrics.mean_squared_error(y_actual, y_pred)) / np.mean(y_actual), 3)
    passed = "✔️" if value < 0.15 else "❌"
    if verbose:
        return value, passed
    else:
        return value

def show_mape(y_actual, y_pred, verbose = False):
    # mean absolute percentage error
    value = round(metrics.mean_absolute_error(y_actual, y_pred)/np.mean(y_actual),3)
    passed = "✔️" if value < 0.15 else "❌"
    if verbose:
        return value, passed
    else:
        return value

def show_rsquared(y_actual, y_pred, verbose = False):
    # r squared
    value = round(metrics.r2_score(y_actual, y_pred), 3)
    passed = "✔️" if value > 0.8 else "❌"
    if verbose:
        return value, passed
    else:
        return value

def show_coefficients(features, model, name_model, graph = True):
    # Given model = LinearRegression() model already executed

    # Create an array of the variables you want to check coeffs
    # features = ['g_display_cost', 'g_shopping_cost', 'g_video_cost', 'g_search_brand_cost', 'g_search_no_brand_cost',
    #             'fb_cost', 'pinterest_cost', 'b_audience_cost', 'b_search_cost', 'avg_price',
    #             'solostove_organic_traffic', 'solostove_paid_traffic', 'trend_smokeless_fire_pit']

    coeffs = model.coef_
    roas = pd.DataFrame(data=coeffs, index=features, columns=['contribution'])
    title_graph = name_model + " Model Coefficients graph"

    if graph == True:

        fig = go.Figure(
            data=[go.Bar(x=roas.index, y=roas['contribution'])],
            layout=go.Layout(
                title=go.layout.Title(text=title_graph)
            )
        )

        fig.show()
        return coeffs
    else:
        print(coeffs)
        return coeffs


def response_regression_to_dataset(df, name_date_column, name_target_colum, name_prediction_column, coef_dict,
                                   features):
    columns = features
    coef_array = list(coef_dict.values())
    new_dict = {}

    for x in range(len(coef_array) - 1):
        new_dict[columns[x]] = df[columns[x]] * coef_array[x]

    new_dict['intercept'] = coef_array[-1]
    response_df = df[[name_date_column, name_target_colum, name_prediction_column]].join(pd.DataFrame(new_dict))
    return response_df

def decomposition_to_dataset(df, coef_dict, features):
    columns = features
    coef_array = list(coef_dict.values())
    result = df[columns]

    result['intercept'] = coef_array[-1]

    decomp_df = pd.DataFrame(result.sum(axis=0))
    decomp_df.reset_index(inplace=True)
    decomp_df.rename(columns={decomp_df.columns[0]: 'canale', decomp_df.columns[1]: 'xDecompAgg'},
                        inplace=True)

    new_dict = {}

    for x in range(len(coef_array) - 1):
        new_dict[columns[x]] = coef_array[x]

    new_dict['intercept'] = coef_array[-1]

    coef_df = pd.DataFrame(list(new_dict.items()))
    coef_df.rename(columns={coef_df.columns[0]: 'canale', coef_df.columns[1]: 'coef'}, inplace=True)

    response_df = pd.merge(left=decomp_df, right=coef_df, left_on='canale', right_on='canale')
    response_df['xDecompPerc'] = response_df['xDecompAgg'] / response_df['xDecompAgg'].sum()
    return response_df