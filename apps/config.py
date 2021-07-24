import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import pathlib
from app import app
import numpy as np
import math


layout = html.Div([

    #Title
    html.Div("Simon Simulation Configuration", style={'text-align':'center', 'font-size': '28px' }),
    html.Br(),

    #Second row titles w/ dropdown box
    html.Div([
        html.Div("Initial Conditions", style={
            'text-align':'center',
            'display':'inline-block',
            'width':'50%',
            'vertical-align': 'middle',
            'font-weight': 'bold',
            'font-size': '20px'
        }),
        html.Div("Global configurations: ", style={
            'text-align':'center',
            'display':'inline-block',
            'width':'25%',
            'vertical-align': 'middle',
            'font-weight': 'bold',
            'font-size': '20px'
        }),

    ]),

    #Graphs
    #Graph all simulations
    html.Br(),
    #Tolerance Exponent + sim data root title
    html.Div([
        html.Div("Tolerance Exponent: ", style={
            'text-align':'center',
            'display':'inline-block',
            'width':'25%',
            'vertical-align': 'middle',
            'font-size': '18px'
        }),
        html.Div("Simulation Data Root Directory: ", style={
            'text-align':'center',
            'display':'inline-block',
            'width':'75%',
            'vertical-align': 'middle',
            'font-size': '18px'
        }),
    ], style={'padding-bottom':'5px'}),

    #Tolerance Exponent + sim data root fill in
    html.Div([
        html.Div(
            dcc.Input(
                id="tol_exp",
                type="text",
                placeholder="Enter tolerance exponent vector: [ ]",
                style={
                    'background-color': 'transparent',
                    'border-radius': '5px',
                    'font-size': '15px',
                    'border-color': 'lightgrey',
                    'display':'inline-block',
                    'width':'90%',
                    'vertical-align': 'middle',
                }
            ),
            style={'display':'inline-block',
                   'width':'45%',
                   'padding-right':'15px'},


        ),

        html.Div(
            dcc.Input(
                id="root_dir",
                type="text",
                placeholder="Enter simulation data root directory:",
                style={
                    'background-color': 'transparent',
                    'border-radius': '5px',
                    'font-size': '15px',
                    'border-color': 'lightgrey',
                    'display':'inline-block',
                    'width':'90%',
                    'vertical-align': 'middle',
                    #'text-align': 'center',
                }
            ),
            style={'display':'inline-block',
                   'width':'45%'},

        ),

    ]),




    html.Br(),

    #Length of word  + Time interval title
    html.Div([
        html.Div("Length of Word: ", style={
            'text-align':'center',
            'display':'inline-block',
            'width':'25%',
            'vertical-align': 'middle',
            'font-size': '18px'
        }),
        html.Div("Time interval to check all the simulations (in sec) [Default:180]: ", style={
            'text-align':'center',
            'display':'inline-block',
            'width':'75%',
            'vertical-align': 'middle',
            'font-size': '18px'
        }),
    ], style={'padding-bottom':'5px'}),


    #Length of word  + Time interval fill box
    html.Div([
        html.Div(
            dcc.Input(
                id="length_word",
                type="text",
                placeholder="Enter length of word vector: [ ]",
                style={
                    'background-color': 'transparent',
                    'border-radius': '5px',
                    'font-size': '15px',
                    'border-color': 'lightgrey',
                    'display':'inline-block',
                    'width':'90%',
                    'vertical-align': 'middle',
                }
            ),
            style={'display':'inline-block',
                   'width':'45%',
                   'padding-right':'15px'},


        ),

        html.Div(
            dcc.Input(
                id="time_interval",
                type="text",
                placeholder="Enter time interval:",
                style={
                    'background-color': 'transparent',
                    'border-radius': '5px',
                    'font-size': '15px',
                    'border-color': 'lightgrey',
                    'display':'inline-block',
                    'width':'90%',
                    'vertical-align': 'middle',
                    #'text-align': 'center',
                }
            ),
            style={'display':'inline-block',
                   'width':'45%'},

        ),

    ]),



    html.Br(),

    #Output Time Step + num simulations simultaneously title
    html.Div([
        html.Div("Output Time Step: ", style={
            'text-align':'center',
            'display':'inline-block',
            'width':'25%',
            'vertical-align': 'middle',
            'font-size': '18px'
        }),
        html.Div("The number of simulations to be carried out simultaneously [Default: 2]: ", style={
            'text-align':'center',
            'display':'inline-block',
            'width':'75%',
            'vertical-align': 'middle',
            'font-size': '18px'
        }),
    ], style={'padding-bottom':'5px'}),

    #Output Time Step + num simulations fill box

    html.Div([
        html.Div(
            dcc.Input(
                id="output_time_step",
                type="text",
                placeholder="Enter output time step vector: [ ]",
                style={
                    'background-color': 'transparent',
                    'border-radius': '5px',
                    'font-size': '15px',
                    'border-color': 'lightgrey',
                    'display':'inline-block',
                    'width':'90%',
                    'vertical-align': 'middle',
                }
            ),
            style={'display':'inline-block',
                   'width':'45%',
                   'padding-right':'15px'},


        ),

        html.Div(
            dcc.Input(
                id="num_concurrrent_jobs",
                type="text",
                placeholder="Enter number of simulations:",
                style={
                    'background-color': 'transparent',
                    'border-radius': '5px',
                    'font-size': '15px',
                    'border-color': 'lightgrey',
                    'display':'inline-block',
                    'width':'90%',
                    'vertical-align': 'middle',
                    #'text-align': 'center',
                }
            ),
            style={'display':'inline-block',
                   'width':'45%'},

        ),

    ]),


    html.Br(),

    #Input files + Log level title
    html.Div([
        html.Div("Initial Condition input files: ", style={
            'text-align':'center',
            'display':'inline-block',
            'width':'25%',
            'vertical-align': 'middle',
            'font-size': '18px'
        }),
        html.Div("Log level of the daemon: INFO/WARNING/ERROR/CRITICAL [Default: INFO]: ", style={
            'text-align':'center',
            'display':'inline-block',
            'width':'75%',
            'vertical-align': 'middle',
            'font-size': '18px'
        }),
    ], style={'padding-bottom':'5px'}),

    #Input files + Log level fill box
    html.Div([
        html.Div(
            dcc.Input(
                id="ic_file_list",
                type="text",
                placeholder="Enter input files list: [ ]",
                style={
                    'background-color': 'transparent',
                    'border-radius': '5px',
                    'font-size': '15px',
                    'border-color': 'lightgrey',
                    'display':'inline-block',
                    'width':'90%',
                    'vertical-align': 'middle',
                }
            ),
            style={'display':'inline-block',
                   'width':'45%',
                   'padding-right':'15px'},


        ),

        html.Div(
            dcc.Input(
                id="log_level",
                type="text",
                placeholder="Enter log level of deamon:",
                style={
                    'background-color': 'transparent',
                    'border-radius': '5px',
                    'font-size': '15px',
                    'border-color': 'lightgrey',
                    'display':'inline-block',
                    'width':'90%',
                    'vertical-align': 'middle',
                    #'text-align': 'center',
                }
            ),
            style={'display':'inline-block',
                   'width':'45%'},

        ),

    ]),


    html.Br(),

    #Number obj + stall time title
    html.Div([
        html.Div("Number of objects: ", style={
            'text-align':'center',
            'display':'inline-block',
            'width':'25%',
            'vertical-align': 'middle',
            'font-size': '18px'
        }),
        html.Div("The time in second beyond which a simulation is considered stalled: ", style={
            'text-align':'center',
            'display':'inline-block',
            'width':'75%',
            'vertical-align': 'middle',
            'font-size': '18px'
        }),
    ], style={'padding-bottom':'5px'}),

    #Number obj + stall time fill box
    html.Div([
        html.Div(
            dcc.Input(
                id="num_obj",
                type="text",
                placeholder="Enter number of objects: [ ]",
                style={
                    'background-color': 'transparent',
                    'border-radius': '5px',
                    'font-size': '15px',
                    'border-color': 'lightgrey',
                    'display':'inline-block',
                    'width':'90%',
                    'vertical-align': 'middle',
                }
            ),
            style={'display':'inline-block',
                   'width':'45%',
                   'padding-right':'15px'},


        ),

        html.Div(
            dcc.Input(
                id="stall_time",
                type="text",
                placeholder="Enter stall_time:",
                style={
                    'background-color': 'transparent',
                    'border-radius': '5px',
                    'font-size': '15px',
                    'border-color': 'lightgrey',
                    'display':'inline-block',
                    'width':'90%',
                    'vertical-align': 'middle',
                    #'text-align': 'center',
                }
            ),
            style={'display':'inline-block',
                   'width':'45%'},

        ),

    ]),

    html.Br(),

    #Starting time
    html.Div("Starting Time (in sec): ", style={
        'text-align':'center',
        'display':'inline-block',
        'width':'25%',
        'vertical-align': 'middle',
        'font-size': '18px'
    }),
    html.Div(
        dcc.Input(
            id="start_time",
            type="text",
            placeholder="Enter starting time: ",
            style={
                'background-color': 'transparent',
                'border-radius': '5px',
                'font-size': '15px',
                'border-color': 'lightgrey',
                'display':'inline-block',
                'width':'40%',
                'vertical-align': 'middle',
            }
        )

    ),

    html.Br(),

    #End Time
    html.Div("End Time (in sec): ", style={
        'text-align':'center',
        'display':'inline-block',
        'width':'25%',
        'vertical-align': 'middle',
        'font-size': '18px'
    }),
    html.Div(
        dcc.Input(
            id="end_time",
            type="text",
            placeholder="Enter end time: ",
            style={
                'background-color': 'transparent',
                'border-radius': '5px',
                'font-size': '15px',
                'border-color': 'lightgrey',
                'display':'inline-block',
                'width':'40%',
                'vertical-align': 'middle',
            }
        )

    ),

    html.Br(),

    #Buttons
    html.Div([
        html.Button('Run', id='run_button',
                    style={
                        'background-color': 'transparent',
                        'border-radius': '12px',
                        'font-size': '15px',
                    }),
        html.Button('Restart', id='restart_button',
                    style={
                        'margin': '0px 20px',
                        'background-color': 'transparent',
                        'border-radius': '12px',
                        'font-size': '15px'
                    }),
        html.Button('Stop', id='stop_button',
                    style={
                        'background-color': 'transparent',
                        'border-radius': '12px',
                        'font-size': '15px',
                    }),

    ], style={'text-align':'center'}
    ),

    #Most outer
],
    style={'font-family':'Open Sans'})
