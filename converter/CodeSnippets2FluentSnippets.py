#!/usr/bin/env python
# coding: utf-8

import json
import base64
import hashlib
from datetime import datetime

def detect_snippet_type_from_scope(scope):
    scope = (scope or "").lower()
    if scope == "content":
        return "php_content"
    if "css" in scope:
        return "css"
    if "js" in scope:
        return "js"
    return "php"

def prepare_code(code_str):
    encoded = base64.b64encode(code_str.encode("utf-8")).decode("utf-8")
    code_hash = hashlib.md5(code_str.encode("utf-8")).hexdigest()
    return encoded, code_hash

def normalize_tags(raw_tags):
    if isinstance(raw_tags, list):
        return [t for t in raw_tags if isinstance(t, str)]
    if isinstance(raw_tags, str):
        parts = [t.strip() for t in raw_tags.split(',')]
        return [t for t in parts if t]
    return []

def clean_description(raw_desc):
    desc = (raw_desc or "").strip()
    if desc.lower().startswith("<p>") and desc.lower().endswith("</p>"):
        desc = desc[3:-4].strip()
    return desc

def convert_code_snippets(raw):
    output = {"file_type":"fluent_code_snippets","version":"10.51","snippets":[]}
    for item in raw.get("snippets", []):
        name     = item.get("name","Untitled")
        desc     = clean_description(item.get("desc",""))
        code_str = item.get("code","")
        scope    = item.get("scope")
        active   = item.get("active",True)
        modified = item.get("modified") or raw.get("date_created") or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        priority = str(item.get("priority",10))
        stype    = detect_snippet_type_from_scope(scope)
        run_map  = {"php":"all","php_content":"shortcode","css":"wp_head","js":"wp_footer"}
        run_at   = run_map.get(stype,"all")
        if stype in ("php","php_content") and not code_str.strip().startswith("<?php"):
            code_str = "<?php\n" + code_str
        encoded, code_hash = prepare_code(code_str)
        raw_tags = item.get("tags",[])
        tags_list= normalize_tags(raw_tags)
        if not tags_list: tags_list=[stype]
        tags_str = ",".join(tags_list)
        info_type= stype.upper() if stype=="php" else stype
        info = {"name":name,"status":"published" if active else "draft","tags":tags_str,
                "description":desc,"type":info_type,"run_at":run_at,
                "group":"","condition":{"status":"no","run_if":"assertive","items":[[]]},
                "load_as_file":"","created_by":"1","created_at":modified,
                "updated_at":modified,"is_valid":"1","updated_by":"1","priority":priority}
        output["snippets"].append({"code":encoded,"code_hash":code_hash,"info":info})
    output["snippets_count"]=len(output["snippets"])
    return output

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python convert_snippets.py input.json output.fluent-snippets.json")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    with open(input_file, "r", encoding="utf-8") as f:
        raw = json.load(f)
    fluent_data = convert_code_snippets(raw)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(fluent_data, f, indent=4)
    print(f"✅ Saved to {output_file}")