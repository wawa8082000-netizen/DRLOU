# %%
import pandas as pd
import json
import os
from pathlib import Path
if not os.path.exists('info.xlsx'):
    raise FileNotFoundError('数据文件不存在:需要info.xlsx')
if not os.path.exists('template.html'):
    raise FileNotFoundError('模版文件不存在:需要template.html')
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('./'))
template = env.get_template("template.html")
import shutil
if Path('docs').is_dir():
    d=Path('docs')
    [shutil.rmtree(x) if x.is_dir() else x.unlink() for x in d.iterdir()]

for sheet_name, df in pd.read_excel('info.xlsx', sheet_name=None).items():
    for _,row in df.iterrows():
        path = row['网址']
        prompt = row['提示词']
        html_path = Path('docs')/ sheet_name.replace('/','') / path
        html_path.parent.mkdir(exist_ok=True, parents=True)
        content = template.render(prompt=prompt)
        
        with open(html_path.with_suffix(".html"), 'w') as f:
            f.write(content)
