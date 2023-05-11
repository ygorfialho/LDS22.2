from django.shortcuts import render

import numpy as np
import pandas as pd

# Create your views here.

def index(request):
    df = pd.read_csv('static/data/Mobile phone price.csv')
    data = { }
    data['dados'] = df[(df['RAM'] == '12GB')]\
        .drop(['Camera (MP)'], axis=1)\
        .dropna()\
        .head()\
        .to_html(index=False, classes=['table', 'table-striped'])
    data['dados2'] = df[(df['Brand'] == 'Xiaomi')]\
        .dropna()\
        .to_html(index=False, classes=['table', 'table-striped'])
    return render(request, 'index.html', data);