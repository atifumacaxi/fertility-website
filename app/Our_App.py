import streamlit as st
import requests
import pandas as pd
import os
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt


# import pyecharts.options as opts
# from pyecharts.charts import Line
# from streamlit_option_menu import option_menu

# st.set_page_config(
#     page_title="mi-person", # => Quick reference - Streamlit
#     page_icon="🏠",
#     layout="centered", # wide
#     initial_sidebar_state="auto") # auto - prefixed bar

# st.subheader('Predicting the fertility rate country for the next 4 years')
api_past = 'https://fertility-djqdzjunta-ew.a.run.app/past'
api_pred = 'https://fertility-djqdzjunta-ew.a.run.app/predict'
api_all = 'https://fertility-djqdzjunta-ew.a.run.app/all'


# with st.form(key='main_form', clear_on_submit=True):
#     c = st.selectbox('Select country', ['Select country', 'Afghanistan', 'Brazil', 'Japan', 'Yemen', 'All countries'])
#     submit = st.form_submit_button('Lock & Load !')
# if submit:
#     if c == 'Select country':
#         st.text('Please, select a country :) ')
#     elif c == 'All countries':
#         res = requests.get(api_all)
#         st.write(res)
#         df = pd.DataFrame(res.json())
#         st.line_chart(df, use_container_width=True)
#     else:
#         response = requests.get(api_past, params={'country': c})
#         df_past = response.json()
#         resp = requests.get(api_pred, params={'country': c})
#         df_pred = resp.json()
#         df_past = pd.DataFrame(df_past)
#         df_pred = pd.DataFrame(df_pred)
#         df_plot = [df_past, df_pred]
#         result = pd.concat(df_plot, axis=0)
#         st.line_chart(result, use_container_width=True)
#         aux = (
#             Line()
#             .add_xaxis('Year')
#             .add_yaxis("fertility", Faker.values())
#             .set_global_opts(title_opts=opts.TitleOpts(title="Country lines"))
#             .render("countrylines.PNG")
#         )

# import streamlit as st
# import streamlit.components.v1 as components

# # bootstrap 4 collapse example
# components.html(
#     """
#    <!DOCTYPE html>
# <html>
# <head>
#     <meta charset="UTF-8">
#     <title>Awesome-pyecharts</title>
#                 <script type="text/javascript" src="https://assets.pyecharts.org/assets/v5/echarts.min.js"></script>

# </head>
# <body >
#     <div id="6bed797ae6c34ecb853a0b7f59fbe8b8" class="chart-container" style="width:900px; height:500px; "></div>
#     <script>
#         var chart_6bed797ae6c34ecb853a0b7f59fbe8b8 = echarts.init(
#             document.getElementById('6bed797ae6c34ecb853a0b7f59fbe8b8'), 'white', {renderer: 'canvas'});
#         var option_6bed797ae6c34ecb853a0b7f59fbe8b8 = {
#     "animation": true,
#     "animationThreshold": 2000,
#     "animationDuration": 1000,
#     "animationEasing": "cubicOut",
#     "animationDelay": 0,
#     "animationDurationUpdate": 300,
#     "animationEasingUpdate": "cubicOut",
#     "animationDelayUpdate": 0,
#     "aria": {
#         "enabled": false
#     },
#     "color": [
#         "#5470c6",
#         "#91cc75",
#         "#fac858",
#         "#ee6666",
#         "#73c0de",
#         "#3ba272",
#         "#fc8452",
#         "#9a60b4",
#         "#ea7ccc"
#     ],
#     "series": [
#         {
#             "type": "line",
#             "name": "fertility",
#             "connectNulls": false,
#             "xAxisIndex": 0,
#             "symbolSize": 4,
#             "showSymbol": true,
#             "smooth": false,
#             "clip": true,
#             "step": false,
#             "data": [
#                 [
#                     "Y",
#                     20
#                 ],
#                 [
#                     "e",
#                     47
#                 ],
#                 [
#                     "a",
#                     116
#                 ],
#                 [
#                     "r",
#                     95
#                 ]
#             ],
#             "hoverAnimation": true,
#             "label": {
#                 "show": true,
#                 "margin": 8
#             },
#             "logBase": 10,
#             "seriesLayoutBy": "column",
#             "lineStyle": {
#                 "show": true,
#                 "width": 1,
#                 "opacity": 1,
#                 "curveness": 0,
#                 "type": "solid"
#             },
#             "areaStyle": {
#                 "opacity": 0
#             },
#             "zlevel": 0,
#             "z": 0
#         }
#     ],
#     "legend": [
#         {
#             "data": [
#                 "fertility"
#             ],
#             "selected": {},
#             "show": true,
#             "padding": 5,
#             "itemGap": 10,
#             "itemWidth": 25,
#             "itemHeight": 14,
#             "backgroundColor": "transparent",
#             "borderColor": "#ccc",
#             "borderWidth": 1,
#             "borderRadius": 0,
#             "pageButtonItemGap": 5,
#             "pageButtonPosition": "end",
#             "pageFormatter": "{current}/{total}",
#             "pageIconColor": "#2f4554",
#             "pageIconInactiveColor": "#aaa",
#             "pageIconSize": 15,
#             "animationDurationUpdate": 800,
#             "selector": false,
#             "selectorPosition": "auto",
#             "selectorItemGap": 7,
#             "selectorButtonGap": 10
#         }
#     ],
#     "tooltip": {
#         "show": true,
#         "trigger": "item",
#         "triggerOn": "mousemove|click",
#         "axisPointer": {
#             "type": "line"
#         },
#         "showContent": true,
#         "alwaysShowContent": false,
#         "showDelay": 0,
#         "hideDelay": 100,
#         "enterable": false,
#         "confine": false,
#         "appendToBody": false,
#         "transitionDuration": 0.4,
#         "textStyle": {
#             "fontSize": 14
#         },
#         "borderWidth": 0,
#         "padding": 5,
#         "order": "seriesAsc"
#     },
#     "xAxis": [
#         {
#             "show": true,
#             "scale": false,
#             "nameLocation": "end",
#             "nameGap": 15,
#             "gridIndex": 0,
#             "inverse": false,
#             "offset": 0,
#             "splitNumber": 5,
#             "minInterval": 0,
#             "splitLine": {
#                 "show": true,
#                 "lineStyle": {
#                     "show": true,
#                     "width": 1,
#                     "opacity": 1,
#                     "curveness": 0,
#                     "type": "solid"
#                 }
#             },
#             "data": "Year"
#         }
#     ],
#     "yAxis": [
#         {
#             "show": true,
#             "scale": false,
#             "nameLocation": "end",
#             "nameGap": 15,
#             "gridIndex": 0,
#             "inverse": false,
#             "offset": 0,
#             "splitNumber": 5,
#             "minInterval": 0,
#             "splitLine": {
#                 "show": true,
#                 "lineStyle": {
#                     "show": true,
#                     "width": 1,
#                     "opacity": 1,
#                     "curveness": 0,
#                     "type": "solid"
#                 }
#             }
#         }
#     ],
#     "title": [
#         {
#             "show": true,
#             "text": "Country lines",
#             "target": "blank",
#             "subtarget": "blank",
#             "padding": 5,
#             "itemGap": 10,
#             "textAlign": "auto",
#             "textVerticalAlign": "auto",
#             "triggerEvent": false
#         }
#     ]
# };
#         chart_6bed797ae6c34ecb853a0b7f59fbe8b8.setOption(option_6bed797ae6c34ecb853a0b7f59fbe8b8);
#     </script>
# </body>
# </html>

#     """,
#     height=600,
# )


# api_past = 'http://127.0.0.1:8000/past'
# api_pred = 'http://127.0.0.1:8000/predict'
# api_all = 'http://127.0.0.1:8000/all'

st.set_page_config(
    page_title="Fertility Rate Research Tool", # => Quick reference - Streamlit
    page_icon=":earth_africa:",
    layout="centered", # wide
    initial_sidebar_state="auto") # auto - prefixed bar

with st.sidebar:
    selected = option_menu(
        menu_title= "Fertility",
        options=['Afghanistan', 'Brazil', 'Japan', 'Yemen', 'Niger', 'Uganda', 'Mali', 'Senegal', 'Cameroon', 'All countries'],
        #icons = ['people', 'globe'],
        styles={
        "container": {"padding": "0!important", "background-color": "#090126"},
        "icon": {"color": "#fafafa", "font-size": "15px"},
        "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "rgba(89, 179, 103, 0.571)"}}
    )

    selected2 = option_menu(
        menu_title= "Schooling",
        options=['Afghanistan', 'Brazil', 'Japan', 'Yemen', 'Niger', 'Uganda', 'Mali', 'Senegal', 'Cameroon', 'All countries'],
        #icons = ['people', ':flag-af:'],
        styles={
        "container": {"padding": "0!important", "background-color": "#090126"},
        "icon": {"color": "#fafafa", "font-size": "15px"},
        "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "rgba(89, 179, 103, 0.571)"}}
    )

#user_colour = st.color_picker(label='Choose a colour for your plot')

#st.markdown("<h1 style='text-align: center; color: red;'>Some title</h1>", unsafe_allow_html=True)
st.subheader('Fertility Rate - Le Wagon')

if selected == 'All countries':
         res = requests.get(api_all)
        #  st.write(res)
         df = pd.DataFrame(res.json())
         st.line_chart(df, use_container_width=True)
else:
        response = requests.get(api_past, params={'country': selected})
        df_past = response.json()
        resp = requests.get(api_pred, params={'country': selected})
        df_pred = resp.json()
        df_past = pd.DataFrame(df_past)
        df_pred = pd.DataFrame(df_pred)
        df_plot = [df_past, df_pred]
        result = pd.concat(df_plot, axis=0)
        #fig = px.scatter(result, name='95% CI Upper')
        #fig2 = px.
        #st.plotly_chart(fig)
        st.line_chart(result, use_container_width=True)

# if selected2 == 'All countries':
#         st.write('We are working on it ')
