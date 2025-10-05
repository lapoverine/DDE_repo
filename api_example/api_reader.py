import requests
import pandas as pd
import time


base_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
properties = ['MolecularWeight',
    'MolecularFormula', 
    'IUPACName',
    'XLogP',
    'RotatableBondCount',
    'ExactMass',
    'MonoisotopicMass',
    'TPSA',
    'Complexity',
    'Charge',
    'HeavyAtomCount',
    'IsotopeAtomCount',
    'CovalentUnitCount'
]



import requests
import pandas as pd
import time

def get_compound_properties(compound_names):

    base_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
    all_data = []
    
    for name in compound_names:
        try:
            cid_url = f"{base_url}/compound/name/{name}/cids/JSON"
            cid_response = requests.get(cid_url, timeout=10)
            cid_data = cid_response.json()
            cid = cid_data['IdentifierList']['CID'][0]

            compound_info = {'CompoundName': name, 'CID': cid}
            
            for prop in properties:
                try:
                    prop_url = f"{base_url}/compound/cid/{cid}/property/{prop}/JSON"
                    prop_response = requests.get(prop_url, timeout=10)
                    prop_data = prop_response.json()
                    

                    value = prop_data['PropertyTable']['Properties'][0].get(prop, 'N/A')
                    compound_info[prop] = value
                    
                except Exception as e:
                    print(f"  Ошибка свойства {prop} для {name}: {e}")
                    compound_info[prop] = 'N/A'
                

                time.sleep(0.2)
            
            all_data.append(compound_info)
            print(f"Загружено: {name}")
            
        except Exception as e:
            continue
    

    df = pd.DataFrame(all_data)
    return df


compounds = ["aspirin",
        "caffeine",
        "glucose",
        "ethanol",
        "methanol",
        "acetone",
        "benzene",
        "toluene",
        "formic acid",
        "acetic acid",
        "urea",
        "glycine",
        "alanine",
        "phenol",
        "aniline",
        "pyridine",
        "cyclohexane",
        "naphthalene",
        "cholesterol",
        "testosterone"   
    ]


df = get_compound_properties(compounds)

print(df)

df.to_csv('data/chemical_compounds.csv', index=False)
print(f"\nДанные сохранены в chemical_compounds.csv")