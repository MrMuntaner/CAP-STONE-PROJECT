# CAP-STONE-PROJECT
In this repo I will have my code and documentation for the final capstone project for AI Academy 

# A prediction of molecular solubility 
Authors: Leo Muntaner 
(Deloitte Strategy and Analytics - Orlando)

# GitHub Navigation Instructions 

Notebooks Folder

- For a detailed overview of the complete analysis and predictions please go [here.](Final_Capstone) 

Data Folder

- To review each of the datasets, access the data folder. 

# Overview

I conducted a series of analyses to predict the solubility of molecules based on 4 descriptors. My results lead to the following suggestions:

1. Aim at using the Delaney descriptors to achieve great results. 
2. Use the Extra Trees Regressor algorithm for best model performance. 

The presentation for this project can be found [here.](Presentation)

# Business Understanding

## The Problem

The soluability of molecules is an important physical chemical property for drug discovery, design and development. 
This type of project is performed by pharmaceutical companies, academia and research.

Among the factors that greatly influence bioavailability of pharmaceutical drugs is water solubility. 

Solubility is an important parameter because it depends on reaching the desired concentration in systemic circulation and obtaining an optimal therapeutic response

Therefore, predicting solubility is one of the main things that need to be investigated in the development of dosage forms, particularly those intended for oral or transdermal administration.

## The Goal

The scientific industry is a creative and diverse market with several avenues to success. With the understanding that there is no one path to success, I aimed to generate insight into a simple action the scientific community may want to take in order to carve their own path to success. To accomplish this goal, I analyzed four different molecular descriptors of compounds. These descriptors included (Octanol-water partition coefficient), (Molecular weight), (Number of rotatable bonds) and (Aromatic proportion = number of aromatic atoms / total number of heavy atoms). 

# Data Understanding and Analysis

## Data Sources, Descriptions, Relevant Visualizations

The range of my analyses required utilization of one dataset. For this area of analysis, I used:

Molecular Information:
 - Molecule Info dataset, which is from https://pubs.acs.org/doi/10.1021/ci034243x# which includes Molecular information on 1,114 compounds.
 
Feature Engineering:
 - cLogP (Octanol-water partition coefficient) - the ratio between solubility of a molecule in optinal and water
 - MW (Molecular weight)
 - RB (Number of rotatable bonds)
 - AP (Aromatic proportion = number of aromatic atoms / total number of heavy atoms)

# Methods 

## Programming Methods

Language: Python 3.10.8 and 3.8 (Only for CAPTSTONE-4 notebook)

Major Packages and Version Numbers can be found [here.](requirements.txt)
    
## Data Science and Machine Learning Model

For this portion of the project I used Linear Regression as my base model. I then comapred it to other models to see which one would be the most optimal. I decided to use Extra Trees Regressor model because after model testing was done, it was the best performer.

The model aims at predicting the soluability of molecules.

To evaluate the model performance, I will use MAE, R^2, MSE and RMSE.

## Streamlit Web App:

Instead of training the model over and over again, I will make use of the .pkl file. This will be used for deploying my model in the web application.
This web application will take the query(input) molecule and then use the rdkit to perform the molecular descriptor calculation. After that, it will make the predictions based on the user input molecular SMILES notation.

This is a super basic web app that visualizes the ML model predictions.

For a detailed overview of the complete web app please reference the `sol_app.py` file [here.](Final_Capstone) 

# Application Structure:

1. User puts in the molecule that they want as a SMILES notation
2. App runs the molecular descriptor calculation and shows the computed molecular descriptors
3. Takes the computed molecular descriptors and applies the ML model on it to make the prediction
4. Displays the resulting predicted values 

Imagine used comes from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3399483/

# Conclusions 

Based on my analyses and ML prediction I suggest the following actions:

1. Aim at sticking to the Delaney descriptors to get the best predictions. 
2. Use Molecules with the lowest solubility to achieve faster drug development, particularly those intended for oral or transdermal administration.
3. Use Extra Trees Regressor model for the best performance and predictions. 
