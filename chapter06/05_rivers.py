rivers = {'nile': 'egypt', 'nile': 'Tanzania', 'Huanghe': 'china', 'Amazon': 'America', 'Changjiang': 'china'}

for k, v in rivers.items():
    print('The', k.lower().title(), 'runs through', v.lower().title())

for river in sorted(rivers.keys()):
    print(river.lower().title())

for nation in sorted(set(rivers.values())):
    print(nation.lower().title())