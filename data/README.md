# 数据集说明（data）

> ⚠️ **数据集不入库（Git）**：UAEMMN 体积约 437 MB、14800 张图像，提交会撑爆仓库。
> 本目录只保留**少量样例**与**说明**，完整数据靠下载脚本 / Release 复现。

## 数据集：UAEMMN

| 项 | 内容 |
|---|---|
| 名称 | UAEMMN（UAV / All-sky Meteor Event Dataset，具体以官方为准） |
| 来源 | Zenodo record **14512061** |
| 规模 | 约 437 MB，14800 张图像 |
| 标注格式 | YOLO（`images/` + `labels/`，每张图一个 `.txt`） |
| 类别 | 单类：meteor（流星） |

## 获取方式

1. **脚本下载**（推荐）：
   ```bash
   python scripts/download_uaemmn.py --out data/raw
   ```
2. **手动下载**：访问 https://zenodo.org/record/14512061 下载压缩包。

## 目录组织（解压后）

```
data/raw/
├── images/
│   ├── train/
│   ├── val/
│   └── test/
└── labels/
    ├── train/
    ├── val/
    └── test/
```

对应 `configs/data.yaml` 中的 `path / train / val / test`。

## 入 Git 的内容

- `data/README.md`（本文件）
- `data/samples/`：少量（几张）样例图 + 对应 label，用于快速验证流程
- `data/metadata/`：数据划分清单、统计信息（CSV/JSON，纯文本，体积小）

## 注意事项

- 大文件（原始图、压缩包、数据库）已被 `.gitignore` 忽略，请勿 `git add`。
- 若更换 / 新增数据集，请在本文件补充来源、许可证与获取方式，保证可复现。
