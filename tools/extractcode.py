#!/usr/bin/env python

import argparse
import re
import os
import sys

RX = re.compile(r"```(\w+)(?:\s+filename=(\S+))?\n(.*?)```", re.DOTALL)


def extract_code_blocks(md_file, destdir="."):
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex for code blocks: ```lang filename=filename.ext ... ```
    for i, (lang, filename, code) in enumerate(RX.findall(content)):
        if not filename:
            bn = os.path.splitext(os.path.basename(md_file))[0]
            bn = bn.lower()
            bn = bn.replace("-", "_")
            bn = bn.replace(" ", "_")
            filename = f"{bn}_ex_{i+1:02}.py"
        
        destfn = os.path.join(destdir, filename)

        with open(destfn, 'w', encoding='utf-8') as out:
            out.write(code)

        print(f"Wrote {destfn}")

def main(args=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--destdir", default=".", help="Destination directory")
    ap.add_argument("files", nargs="*", help="Input files")
    args = ap.parse_args(args)

    for fn in args.files:
        extract_code_blocks(fn, args.destdir)

if __name__ == '__main__':
    sys.exit(main() or 0)
