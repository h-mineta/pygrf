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
            data_bytes: bytes = grf.open(args.filename).data
            try:
                # Shift-JIS(CP932) データとしてデコード可能か確認
                text_data = data_bytes.decode("cp932")
                print(text_data)  # テキストとして出力
            except UnicodeDecodeError:
                # デコードできない場合はバイナリデータとして出力
                sys.stdout.buffer.write(data_bytes)
        else:
            for file in grf.files():
                print(f"{file}")

if __name__ == "__main__":
    main(args)
