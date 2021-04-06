# The estimation of a regression of ln(vio + rob + mur)
# against shall, incarc_rate, density, avginc, pop, pb1064,
# pw1064, and pm1029.
# https: // www.statsmodels.org/stable/index.html

# The import of all needed dependencies.
import numpy as np
import pandas as pd
import statsmodels.api as sm


def write_into_file(file_name, item):
    """This function writes item into file.
    This function requires 2 parameters:
        "file_name" - the name of destination file
        "item" - item to write in (have to be a string type). 
    """
    with open(file_name, 'a') as f:
        f.write(item)


def statistics(y_arr, x_arr):
    """This function fits the linear regression model.
    This function requires 2 parameters:
        y_arr - ndarray
        x_arr - ndarray
    """
    y = y_arr
    x = sm.add_constant(x_arr)
    model = sm.OLS(y, x)
    return model.fit()


# Moving data from "guns.xlsx" file to "df" a Pandas DataFrame.
df = pd.read_excel('guns.xlsx')

# Creating lists for x and y columns.
x_columns_ls = [['shall'], ['shall', 'incarc_rate', 'density', 'avginc',
                            'pop', 'pb1064', 'pw1064', 'pm1029']]
y_columns_ls = ['vio', 'mur', 'rob']

# Calculating the required statistic values.
y = pd.DataFrame(df, columns=y_columns_ls).to_numpy()
y = np.sum(y, axis=1)
y = list(map(lambda item: np.math.log(item), y))
y = np.array(y)

# Calculating the required statistic values.
for i in x_columns_ls:
    x = pd.DataFrame(df, columns=i).to_numpy()
    results = statistics(y, x)

    # Writing results into text file "guns_output.txt".
    results_str = str(results.summary())
    write_into_file('guns_output.txt',
                    'ln(vio + rob + mur)' + '   vs  ' + str(i) + '\n')
    write_into_file('guns_output.txt', results_str + '\n'*3)

# Writing the chart of variables into text file "guns_output.txt".
write_into_file('guns_output.txt', 'The chart of variables' +
                '\n' + '-'*20 + '\n')
for i, x in enumerate(x_columns_ls[1], 1):
    write_into_file('guns_output.txt', f': x{i} : ' + x + '\n')
write_into_file('guns_output.txt', '\nWell DONE!!!\n')

# Console output.
print('Well DONE!!!')
input('Push "Enter" to finish: ')
