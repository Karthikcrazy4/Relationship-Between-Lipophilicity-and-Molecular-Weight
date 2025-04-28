# Relationship-Between-Lipophilicity-and-Molecular-Weight
This project analyzes pharmaceutical compounds from Manapharmadb.csv, focusing on molecular properties that influence drug development. The analysis uses pandas for data handling and matplotlib for visualization to explore relationships between molecular weight and lipophilicity (XLogP). Five compounds were analyzed: Aspirin, Acetaminophen, Ethanol, L-Arginine, and ATP. The dataset provides compound identifiers (CID), molecular weights, XLogP values, InChIKeys, and canonical SMILES notations for each molecule. Visualization shows ATP as a high-molecular-weight outlier (507 g/mol) with strong hydrophilicity, while Aspirin and Acetaminophen demonstrate lipophilic properties. Both data cleaning and exploration were performed to ensure accurate analysis and interpretation. The project demonstrates how physicochemical properties inform solvent selection during pharmaceutical development. Lipophilic compounds typically require organic solvents, while hydrophilic molecules dissolve better in water-based solutions. These properties significantly impact membrane permeability, bioavailability, and formulation strategies. Understanding these relationships helps pharmaceutical scientists develop effective drug delivery systems and optimize therapeutic outcomes.


Plot Features:

Title: "Relationship Between Lipophilicity and Molecular Weight"
X-axis: XLogP (Lipophilicity) - ranging from approximately -6 to +1
Y-axis: Molecular Weight (g/mol) - ranging from 0 to about 500 g/mol
Data Points: Five colored dots representing each compound in the dataset, with labels identifying each compound
Grid Lines: Light gray grid lines to help with value estimation

Compound Distribution:

ATP (top left):

Highest molecular weight (~507 g/mol)
Very hydrophilic with an XLogP of about -5.7
Positioned as an outlier in terms of molecular weight


L-Arginine (middle left):

Moderate molecular weight (~174 g/mol)
Hydrophilic with an XLogP of about -4.2


Ethanol (bottom center-right):

Lowest molecular weight (~46 g/mol)
Nearly neutral lipophilicity with an XLogP just below 0 (-0.1)


Acetaminophen (middle right):

Moderate molecular weight (~151 g/mol)
Slightly lipophilic with an XLogP of about 0.5


Aspirin (middle-upper right):

Moderate molecular weight (~180 g/mol)
Most lipophilic in the dataset with an XLogP of about 1.2



Key Insights:

Clustering Pattern:

The compounds form three distinct groups:

ATP as a high-molecular-weight, highly hydrophilic outlier
A cluster of moderate-weight compounds (Aspirin, Acetaminophen, L-Arginine)
Ethanol as a low-molecular-weight compound




Polarity Distribution:

Clear separation between hydrophilic compounds (negative XLogP: ATP, L-Arginine) and lipophilic compounds (positive XLogP: Aspirin, Acetaminophen)
Ethanol sits near the boundary between hydrophilic and lipophilic


Pattern Observations:

No strict correlation between molecular weight and lipophilicity in this small dataset
The most hydrophilic compound (ATP) has the highest molecular weight
Compounds with similar molecular weights (Aspirin, Acetaminophen, L-Arginine) can have very different lipophilicity values
