#!/usr/bin/env python3

import argparse
import sys

from pygrf import api

parser = argparse.ArgumentParser(description="Command Line Tool")

parser.add_argument("grf_path",
                    action="store",
                    nargs=1,
                    default="data.grf",
                    type=str,
                    help="grf path")

parser.add_argument("filename",
                    action="store",
                    nargs="?",
                    default=None,
                    type=str,
                    help="filename to extract")

args = parser.parse_args()

def main(args):
    grf = None
    with open(args.grf_path[0], "rb") as fp:
        grf = api.open_grf(fp)

        if args.filename is not None:
            sys.stdout.buffer.write(grf.open(args.filename).data)
        else:
            # ファイル一覧を表示
            for file in grf.files():
                print(f"{file}")

if __name__ == "__main__":
    main(args)
