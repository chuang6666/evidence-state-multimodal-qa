"""Entry points for the documented frozen-output workflow."""
import argparse
import json
from pathlib import Path
from .replay import replay, verify_manifest

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('command',nargs='?',default='verify',choices=['verify','replay','tables','statistics','structural','structural-statistics','prepare-references','rescore'])
    p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[2])
    p.add_argument('--output-dir',type=Path)
    p.add_argument('--reference-dir',type=Path)
    p.add_argument('--mmqa-data',type=Path)
    p.add_argument('--m3-data',type=Path)
    a=p.parse_args()
    if a.command=='verify':
        result={'verified_files':verify_manifest(a.root),'status':'PASS_CHECKSUMS'}
    elif a.command=='replay':result=replay(a.root)
    elif a.command in ['structural','structural-statistics']:
        from .structural_replay import run
        result=run(a.root,a.output_dir,a.command=='structural-statistics')
    else:
        if not a.output_dir:p.error('--output-dir must name a new/empty directory outside the repository')
        if a.command=='tables':
            from .ijmlc_tables import run
            result=run(a.root,a.output_dir)
        elif a.command=='statistics':
            from .statistics_run import reproduce_statistics
            result=reproduce_statistics(a.root,a.output_dir)
        elif a.command=='prepare-references':
            if not a.mmqa_data or not a.m3_data:p.error('Both provider files are required; do not put them in this repository')
            from .offline import prepare_references
            result=prepare_references(a.root,a.mmqa_data,a.m3_data,a.output_dir)
        else:
            if not a.reference_dir:p.error('--reference-dir is required')
            from .offline import rescore
            result=rescore(a.root,a.reference_dir,a.output_dir)
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
