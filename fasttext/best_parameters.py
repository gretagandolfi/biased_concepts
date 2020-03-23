import json
import sys
import codecs
import numpy as np
from docopt import docopt

def ranking(model):

    param_sets = []
    with codecs.open(model,'rU','utf-8') as f:
        for line in f:
           param_sets.append(json.loads(line))

    best_vals = []
    for param_set in param_sets:
        best_vals.append(param_set["target"])

    best_indices = np.argsort(best_vals)[-20:][::-1]

    rows = []
    columns=["target"]
    for k,v in param_sets[0]["params"].items():
        columns.append(k[:6])

    for best in best_indices:
        param_set = param_sets[best]
        row = [str(param_set["target"])[:6]]
        for k,v in param_set["params"].items():
            if k not in ["lrate","wdecay"]:
                row.append(str(float(v)))
            else:
                row.append(str(v)[:5])
        rows.append(row)

    tab = pd.DataFrame(rows)
    tab.columns = columns
    
    return tab