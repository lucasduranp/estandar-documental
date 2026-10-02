"""Recompute authoritative release decision; returns nonzero unless release PASS."""
import argparse,json
from pathlib import Path
from execution_manifest import save

def finalize(path):
    m=json.loads(Path(path).read_text(encoding='utf-8'))
    save(path,m)
    return m

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('manifest');a=p.parse_args()
    m=finalize(a.manifest)
    print(json.dumps({'release':m['release'],'gates':m['gates']},indent=2))
    raise SystemExit(0 if m['release']=='PASS' else 1)
