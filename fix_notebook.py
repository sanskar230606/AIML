import json

with open('ass7.ipynb') as f:
    nb = json.load(f)

for c in nb['cells']:
    new_src = []
    for line in c['source']:
        # Replace unescaped newline within string literals
        line = line.replace('print("Confusion Matrix :\n', 'print("Confusion Matrix :\\n')
        line = line.replace('print("\nConfusion Matrix:\n', 'print("\\nConfusion Matrix:\\n')
        line = line.replace('print("\nEnter flower measurements in cm :', 'print("\\nEnter flower measurements in cm :')
        line = line.replace('print("\nLogistic Regression Prediction:', 'print("\\nLogistic Regression Prediction:')
        new_src.append(line)
    c['source'] = new_src

with open('ass7.ipynb', 'w') as f:
    json.dump(nb, f, indent=1)

for i, c in enumerate(nb['cells']):
    src = ''.join(c['source'])
    compile(src, f'cell_{i}', 'exec')

print('Confirmed: All 19 cells compile cleanly without errors!')
