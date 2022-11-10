#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 14:21:25 2022

@author: jeffyjaxon
"""

import pandas as pd
import matplotlib.pyplot as plt

def read_data(data_name):
    """
    This function reads the csv file and returns the dataframe

    Parameters
    ----------
    data_name : String
        The name of the file.

    Returns
    -------
    Dataframe
        The dataframe for the corresponding file.

    """
    return pd.read_csv(data_name)


def plot_spi_graph():
    """
    This function plots a bar graph between international teams and their SPI Index

    Returns
    -------
    None.

    """
    plt.figure(figsize = (9 , 9))
    plt.bar(intl_teams_data['name'], intl_teams_data['spi'])
    plt.xticks(rotation = 60)
    plt.xlabel("Teams")
    plt.ylabel("Soccer Power Index Points")
    plt.title("International Teams SPI Index")
    plt.savefig("SPI Graph")
    plt.show()

def plot_off_def_graph():
    """
    This function plots a line graph for the offensive and defensive rating for the first 10 teams

    Returns
    -------
    None.

    """
    plt.figure(figsize = (8 , 8))
    plt.plot(intl_teams_data['name'], intl_teams_data['off'], label = 'Offensive Rating')
    plt.plot(intl_teams_data['name'], intl_teams_data['def'], label = 'Defensive Rating')
    plt.xticks(rotation = 90)
    plt.xlabel("Teams")
    plt.ylabel("Ratings")
    plt.legend()
    plt.title("International Teams - Offensive Defensive Comparison")
    plt.savefig("Off_Def Graph")
    plt.show()

def plot_fatality_graph():
    """
    This function plots a pie chart for the fatalities occured in 2000 - 2014
    for the different airlines.

    Returns
    -------
    None.

    """
    plt.figure(figsize = (8 , 8))
    plt.pie(airline_data['fatalities_00_14'], labels = airline_data['airline'])
    plt.title('Airline Fatalities In 2000 - 2014', size = 14)
    plt.savefig("Fatalities Graph")
    plt.show()

#read data from spi global rankings csv
global_ranking_data = read_data("spi_global_rankings_intl.csv")

#retrieve the data for countries in top 10
intl_teams_data = global_ranking_data[0:10]

#read data from airline csv
airline_data_frame = read_data("airline-safety.csv")

#retrieve the data for 10 airlines
airline_data = airline_data_frame[0:10]

#Calling function to plot SPI graph
plot_spi_graph()

#Calling function to plot Offensive Defensive graph
plot_off_def_graph()

#Calling function to plot Fatality graph
plot_fatality_graph()
