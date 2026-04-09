import json

data = json.load(open('/Users/chunhsienfu/Documents/GitHub/MDJimmyFu.github.io/PriSalary/薪水小幫手_備份_2026-04-01.json'))
companies = {c['id']: c['name'] for c in data.get('companies', [])}
results = {}

for dt, shifts in data.get('entries', {}).items():
    if isinstance(shifts, dict):
        items = [v for v in shifts.values() if v and isinstance(v, dict)]
    elif isinstance(shifts, list):
        items = shifts
    else:
        continue
        
    for s in items:
        if isinstance(s, dict) and 'companyId' in s and s['companyId']:
            cid = s['companyId']
            hrs = str(s.get('hours', ''))
            sal = str(s.get('salary', ''))
            if hrs and sal:
                if cid not in results: results[cid] = set()
                results[cid].add((hrs, sal))

for cid, pairs in results.items():
    print(f"[{companies.get(cid, cid)}]")
    for h, s in pairs:
        print(f"  {h} hrs -> ${s}")
print("DONE!")
