"""Update download counts in data/skills.json from public source pages."""
import json, re, urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'data'/'skills.json'
URLS=['https://skillsmp.com/zh','https://skills.sh']
def fetch(url):
    req=urllib.request.Request(url,headers={'User-Agent':'skills.lilyluo.ai/1.0'})
    with urllib.request.urlopen(req,timeout=25) as r:return r.read().decode('utf-8','ignore')
def main():
    data=json.loads(OUT.read_text(encoding='utf-8')); pages='\n'.join(fetch(u) for u in URLS); changed=0
    for item in data:
        m=re.search(re.escape(item['n'])+r'.{0,240}?([0-9][0-9,.]*)([kKmM])',pages,re.S)
        if m:item['v']=m.group(1)+m.group(2).lower();changed+=1
    OUT.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(f'updated {changed}/{len(data)} skills')
if __name__=='__main__':main()
