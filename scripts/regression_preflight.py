"""Inventory exact case IDs; no substitute for the approved regression runner."""
import argparse
import json
from pathlib import Path
from check_docx import inspect

CASES=['GD01','GD02','GD03','GD04','GD05','GD06','GD07','PR01']
def run(suite):
    results=[]
    for case in CASES:
        files=list(suite.rglob(case+'*.docx')) if suite.exists() else []
        results.append({'case':case,'status':'PRESENT_UNVERIFIED' if files else 'BLOCKED','files':[inspect(x) for x in files]})
    complete=all(x['status']=='PRESENT_UNVERIFIED' for x in results)
    return {'required_suite':'1.1','cases':results,'inventory':'PASS' if complete else 'BLOCKED','approved_regression':'NOT_RUN','promotion':'NOT_EVALUATED','reason':'Inventory only. Execute run_regression.py and enhanced_checks.py, then review all pages and final use.'}
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--suite',type=Path,required=True)
    p.add_argument('--report',type=Path,required=True)
    a=p.parse_args()
    result=run(a.suite)
    a.report.parent.mkdir(parents=True,exist_ok=True)
    a.report.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({'promotion':result['promotion'],'cases':{r['case']:r['status'] for r in result['cases']}}))
    raise SystemExit(0 if result['inventory']=='PASS' else 1)
