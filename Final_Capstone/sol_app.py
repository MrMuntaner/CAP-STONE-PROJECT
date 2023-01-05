import pickle
import numpy as np
import pandas as pd
import streamlit as st
from rdkit import Chem
from rdkit.Chem import Descriptors

# *Instead of training the model over and over again, I will make use of the .pkl file. This will be used for deploying my model in the web application.
# *This web application will take the query(input) molecule and then use the rdkit to-
# *perform the molecular descriptor calculation. After that, it will make the predictions based on the user input molecule SMILES notation.

# *This is a super basic web app that visualizes the ML model predictions.

# *Application Structure:
# *1. User puts in the molecule that they want as a SMILES notation
# *2. App runs the molecular descriptor calculation and shows the computed molecular descriptors
# *3. Takes the computed molecular descriptors and applies the ML model on it to make the prediction
# *4. Displays the resulting predicted values 

# TODO: create molecular descriptors calculation functions
def AromaticProportion(m):
    aromatic_atoms = [m.GetAtomWithIdx(i).GetIsAromatic() for i in range(m.GetNumAtoms())]
    aa_count = []
    for i in aromatic_atoms:
        if i == True:
            aa_count.append(1)
    
    AromaticAtom = sum(aa_count)
    HeavyAtom = Descriptors.HeavyAtomCount(m)
    AR = AromaticAtom/HeavyAtom
    return AR


def generate(smiles, verbose=False):
    # This will create an empty list and for each of the smiles notation in the sol.SMILES and iterate through each one-
    # converting them into rdkit objects.
    moldata = []
    for elem in smiles:
        mol = Chem.MolFromSmiles(elem)
        moldata.append(mol)
    
    baseData = np.arange(1,1)
    i = 0
    # computes the 3 descriptors and then converts them into the numpy array.
    for mol in moldata:
        desc_MolLogP = Descriptors.MolLogP(mol)
        desc_MolWt = Descriptors.MolWt(mol)
        desc_NumRotatableBonds = Descriptors.NumRotatableBonds(mol)
        desc_AromaticProportion = AromaticProportion(mol)
        
        row = np.array([desc_MolLogP,
                        desc_MolWt,
                        desc_NumRotatableBonds,
                        desc_AromaticProportion])
        
        if(i==0):
            baseData = row
        else:
            baseData = np.vstack([baseData, row])
        i = i+1
    
    #dumps the above code into a dataframe 
    columnNames = ["MolLogP", "MolWt", "NumRotatableBonds", "AromaticProportion"]
    descriptors = pd.DataFrame(data=baseData, columns=columnNames)
    
    return descriptors

# TODO: display the title of the web app
# In streamlit the markdown language is used for writing. 
st.write("""
# Molecular Solubility Prediction Web App

The purpose of this app is to predict the **Solubility (LogS)** values of molecules!

The soluability of molecules is an important physical chemical property for drug discovery, design and development. 

This type of analysis is performed by pharmaceutical companies and academia.

The data used for this app was obtained from  https://pubs.acs.org/doi/10.1021/ci034243x#
***
""")

# TODO: display the side panel on the webpage and input molecules
# Note that when the web app is displayed, this will show a text box that takes in the SMILES notation as the input-
# file. The user will then input the desired molecules to be predicted 
st.sidebar.header('Input Features')

# read in the SMILES input
# the user would hit enter after each desired SMILES notation input
SMILES_input = "NCCCC\nCCC\nCN"

SMILES = st.sidebar.text_area("SMILES input", SMILES_input)

# adds C as a dummy, first item
SMILES = "C\n" + SMILES
SMILES = SMILES.split('\n')

st.header('Input SMILES')
# skips the dummy first item 
SMILES[1:]

# calculate the molecular descriptors
st.header('Computed Molecular Descriptors')

# this will assign the calculated descriptor to the X variable 
X = generate(SMILES)
X[1:]

# TODO: read in the pre-built model I saved
load_model = pickle.load(open('sol_model.pkl', 'rb'))

# apply the model to make predictions on the molecular descriptor the user generated.
# it will use the molecular descriptor that has been calculated from the user input from the side panel-
# and it makes the prediction. it then assigns it to the pred variable
pred = load_model.predict(X)

st.header('Predicted LogS Values')
# skips the dummy item
pred[1:]