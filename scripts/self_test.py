"""Negative tests for fail-closed QA helpers, not golden regression cases."""
import tempfile
from pathlib import Path
from check_docx import inspect
from font_gate import evaluate
from regression_preflight import run

def test():
    with tempfile.TemporaryDirectory() as d:
        p=Path(d)/'broken.docx'
        p.write_bytes(b'not a docx')
        assert inspect(p)['structural_preflight']=='FAIL'
        assert inspect(Path(d)/'absent.docx')['structural_preflight']=='FAIL'
        assert all(x['status']=='BLOCKED' for x in run(Path(d))['cases'])
    native=[{'name':'ABCDEF+Aptos','embedded':True},{'name':'ABCDEF+Aptos-Bold','embedded':True}]
    assert evaluate(native)['font_embedding_gate']=='PASS'
    assert evaluate([])['font_embedding_gate']=='FAIL'
    assert evaluate(native+[{'name':'NotoSans','embedded':True}])['font_embedding_gate']=='FAIL'
    assert evaluate([{'name':'Aptos','embedded':False},native[1]])['font_embedding_gate']=='FAIL'
    assert evaluate([native[0]])['font_embedding_gate']=='FAIL'
    assert evaluate(native+[{'name':'SymbolMT','embedded':True}],{'symbolmt':'\uf0b7'})['font_embedding_gate']=='PASS'
    assert evaluate(native+[{'name':'SymbolMT','embedded':True}],{'symbolmt':'Business text'})['font_embedding_gate']=='FAIL'
    assert evaluate(native+[{'name':'SymbolMT','embedded':True}])['font_embedding_gate']=='FAIL'
    print('11 helper self-tests PASS; approved regression tested separately')

if __name__=='__main__':
    test()
