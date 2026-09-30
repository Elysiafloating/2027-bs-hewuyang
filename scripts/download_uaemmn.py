"""下载 UAEMMN 流星数据集（Zenodo record 14512061）。

UAEMMN 约 437 MB，含 14800 张 YOLO 格式标注图像。本脚本通过 Zenodo
公开 API 拉取文件清单并下载，避免手动点击。下载后解压到 data/raw/。

用法：
    python scripts/download_uaemmn.py --out data/raw
    python scripts/download_uaemmn.py --out data/raw --record 14512061
"""

import argparse
import os
import sys
import urllib.request

import requests

ZENODO_API = "https://zenodo.org/api/records/{record}"


def list_files(record: str):
    """返回 Zenodo record 的文件清单 [(filename, download_url), ...]"""
    resp = requests.get(ZENODO_API.format(record=record), timeout=30)
    resp.raise_for_status()
    files = resp.json().get("files", [])
    return [(f["key"], f["links"]["self"]) for f in files]


def download(url: str, dest: str):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    print(f"[下载] {os.path.basename(dest)} ...")
    urllib.request.urlretrieve(url, dest)


def main():
    parser = argparse.ArgumentParser(description="Download UAEMMN from Zenodo")
    parser.add_argument("--record", default="14512061")
    parser.add_argument("--out", default="data/raw")
    args = parser.parse_args()

    try:
        files = list_files(args.record)
    except Exception as e:  # noqa: BLE001
        print(f"[错误] 无法获取文件清单：{e}", file=sys.stderr)
        print("请手动前往 https://zenodo.org/record/14512061 下载。")
        sys.exit(1)

    if not files:
        print("[警告] 未找到文件，请检查 record id。")
        sys.exit(1)

    for fname, url in files:
        download(url, os.path.join(args.out, fname))

    print(f"\n[完成] 文件已下载到 {args.out}/")
    print("请将压缩包解压，并按 configs/data.yaml 组织 images/ 与 labels/ 目录。")


if __name__ == "__main__":
    main()
