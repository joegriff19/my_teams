# Import Packages and other files for app
import index
from app import app, server  # NEED THE IMPORT SERVER FOR RENDER
from dash import dcc, html, clientside_callback, State
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
import requests
from bs4 import BeautifulSoup
import pandas as pd
# import lxml
import warnings
from datetime import date
import time
import dash_player as dp
import dash_leaflet as dl
# import coordinates
# import globe
# import weather
# import city_list
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import dash_extensions as de
import os
from flask import send_from_directory
import dash_loading_spinners as dls

# today = date.today()
# warnings.simplefilter(action='ignore', category=FutureWarning)

# GITHUB = 'https://github.com/joegriff19'
# LINKEDIN = 'https://www.linkedin.com/in/joseph-m-griffin/'
# VENMO = 'https://venmo.com/u/joegriff19'
# LOTTIE = 'https://assets5.lottiefiles.com/packages/lf20_GoeyCV7pi2.json'
# LOTTIE = 'https://assets2.lottiefiles.com/packages/lf20_mDnmhAgZkb.json'
# options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "2rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

# Index Page Layout
colors = {
    # 'background': '#ffffff',
    'text': '#0000CD'
}

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

# standings_url = "https://fbref.com/en/comps/9/Premier-League-Stats"
# data = requests.get(standings_url)
# soup = BeautifulSoup(data.text)
# standings_table = soup.select('table.stats_table')[0]
# print(standings_table)
#
# links = standings_table.find_all('a')
# links = [l.get("href") for l in links]
# links = [l for l in links if '/squads/' in l]
#
# team_urls = [f"https://fbref.com{l}" for l in links]
#
# data = requests.get(team_urls[0])
#
# matches = pd.read_html(data.text, match="Scores & Fixtures")[0]
#
# soup = BeautifulSoup(data.text)
# links = soup.find_all('a')
# links = [l.get("href") for l in links]
# links = [l for l in links if l and 'all_comps/shooting/' in l]
#
# data = requests.get(f"https://fbref.com{links[0]}")
# shooting = pd.read_html(data.text, match="Shooting")[0]
# print(shooting)


# define layout
app.layout = html.Div([
    dcc.Location(id="url"),
    content,
])
# index page layout
index_layout = html.Div(
    children=[
        html.Header(
            children=[
                # html.Div(dls.Hash(fullscreen=True), style={"height": "200px"}),
                html.Div(children="Club Teams", className="wg"),
                html.Div(children="Arsenal FC"),
                html.Div(children="FC Barcelona"),
                html.Div(children="Boca Juniors CF"),
                html.Div(children="BV Borussia Dortmund"),
                html.Div(children="Chicago Fire FC"),
                html.Div(children="Holstein Kiel SV"),
                html.Div(children="Inter Miami CF"),
                html.Div(children="1. FC Union Berlin"),
                html.Br(),
                
                html.Div(children="National Teams", className="wg"),
                html.Div(children="Argentina 🇦🇷"),
                html.Div(children="Germany 🇩🇪"),
                html.Div(children="Spain 🇪🇸"),
                html.Div(children="USA 🇺🇸"),

            ]
        )
        ]
)


@app.callback(
    Output('page-content', 'children', ),
    [Input('url', 'pathname', )]
)
def render_page_content(pathname):
    if pathname == '/':
        return index_layout
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognized..."),
        ]
    )

def show_game():
    pass


def recent_form():
    pass


def show_table():
    pass


