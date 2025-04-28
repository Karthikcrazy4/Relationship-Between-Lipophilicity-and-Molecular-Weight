import pandas as pd
import matplotlib.pyplot as plt

# Load local CSV file
try:
    df = pd.read_csv('Manapharmadb.csv')
    print("Dataset loaded successfully!")
    
    # Basic dataset information
    print("\nDataset Information:")
    print(f"Number of compounds: {len(df)}")
    print("\nDataset Overview:")
    print(df.head())
    
    print("\nChecking for missing values:")
    
    # Data cleaning
    df['MolecularWeight'] = pd.to_numeric(df['MolecularWeight'], errors='coerce')
    df['XLogP'] = pd.to_numeric(df['XLogP'], errors='coerce')
    
    # Add compound names
    compound_names = {
        2244: "Aspirin",
        1983: "Acetaminophen",
        702: "Ethanol",
        6322: "L-Arginine",
        5957: "ATP"
    }
    
    df['CompoundName'] = df['CID'].map(compound_names)
    
    print("\nCleaned Dataset with Compound Names:")
    print(df)
    
    # Visualization 1: Molecular Weight vs XLogP
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(df['XLogP'], df['MolecularWeight'], 
                         c=df.index, cmap='viridis', 
                         s=100, alpha=0.7)
    
    for i, txt in enumerate(df['CompoundName']):
        plt.annotate(txt, (df['XLogP'].iloc[i], df['MolecularWeight'].iloc[i]),
                    fontsize=10, ha='center', va='bottom')
    
    plt.title('Relationship Between Lipophilicity and Molecular Weight', fontsize=14)
    plt.xlabel('XLogP (Lipophilicity)', fontsize=12)
    plt.ylabel('Molecular Weight (g/mol)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    
    # Visualization 2: Bar plot
    plt.figure(figsize=(12, 6))
    bars = plt.bar(df['CompoundName'], df['XLogP'], alpha=0.7)
    
    norm = plt.Normalize(df['MolecularWeight'].min(), df['MolecularWeight'].max())
    sm = plt.cm.ScalarMappable(cmap='viridis', norm=norm)
    sm.set_array([])
    
    for i, bar in enumerate(bars):
        bar.set_color(plt.cm.viridis(norm(df['MolecularWeight'].iloc[i])))
    
    plt.title('Lipophilicity (XLogP) of Different Compounds', fontsize=14)
    plt.xlabel('Compound', fontsize=12)
    plt.ylabel('XLogP Value', fontsize=12)
    plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)
    plt.grid(True, alpha=0.3, axis='y')
    plt.colorbar(sm, label='Molecular Weight (g/mol)')
    
    for i, v in enumerate(df['MolecularWeight']):
        plt.text(i, df['XLogP'].iloc[i] + (0.5 if df['XLogP'].iloc[i] >= 0 else -0.5), 
                 f"MW: {v}", ha='center', fontsize=9)
    
    plt.tight_layout()
    plt.show()
    
    # Analysis summary
    print("\nCompound Properties Summary:")
    summary_df = df[['CompoundName', 'MolecularWeight', 'XLogP']].sort_values('XLogP')
    print(summary_df)
    
    print("\nSolvent Selection Implications:")
    print("Compounds with positive XLogP values (lipophilic):")
    print(df[df['XLogP'] > 0][['CompoundName', 'XLogP', 'MolecularWeight']])
    
    print("\nCompounds with negative XLogP values (hydrophilic):")
    print(df[df['XLogP'] <= 0][['CompoundName', 'XLogP', 'MolecularWeight']])

except Exception as e:
    print(f"Error processing the dataset: {e}")
