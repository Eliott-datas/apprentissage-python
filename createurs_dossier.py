from pathlib import Path

d = {
    "Films" : ["le seigneur des anneaux", 
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
    "Employes" : ["Paul",
                  "Pierre",
                  "Marie"]
}

CUR_DIR = Path(__file__).resolve().parent

for k,v in d.items():
    k_dirs = CUR_DIR / k
    for value in v:
        v_dir = k_dirs / value
        v_dir.mkdir(exist_ok = True, parents=True)