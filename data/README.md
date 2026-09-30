# 数据集说明（data）

> ⚠️ **完整数据集不入库（Git）**：`MeteorCam` 真实数据集体积较大，提交会撑爆仓库。
> 本目录只保留**少量样例**与**说明**，完整数据靠本地链接 / Release 复现。

## 本地真实数据集：MeteorCam

| 项 | 内容 |
|---|---|
| 名称 | MeteorCam（本地流星监测数据） |
| 本地路径 | `D:/data_tianwen/MeteorCam/meteor_yolo_split` |
| 来源 | 本地采集/整理，基于 `D:/data_tianwen/MeteorDetection` 项目 |
| 类别 | 5 类：meteor / seagull / airplane / satellite / star |
| 训练集 | `images/train` + `labels/train` |
| 验证集 | `images/val`   + `labels/val` |
| 测试集 | `images/test`  + `labels/test` |
| 标注格式 | YOLO（`images/` + `labels/`，每张图一个 `.txt`） |

> 对应 `configs/data.yaml` 中的 `path / train / val / test`。

## 目录组织

```
data/raw/                     # 本仓库只保留该空目录结构，真实数据通过软链接/复制填充
├── images/
│   ├── train/
│   ├── val/
│   └── test/
└── labels/
    ├── train/
    ├── val/
    └── test/
```

## 本地使用方法

在 Windows PowerShell / Git Bash 中，把真实数据链接到本仓库：

```powershell
# 以管理员身份运行 PowerShell（Junction 不需要管理员，mklink 需要）
New-Item -ItemType Junction -Path "2027-bs-hewuyang/data/raw" -Target "D:/data_tianwen/MeteorCam/meteor_yolo_split"
```

或复制一份到 `data/raw/`（占用磁盘空间）。

## 类别说明

| 类别 | 含义 | 论文定位 |
|---|---|---|
| meteor | 流星 | **真实目标**（线状短时弱小目标） |
| seagull | 海鸥 | 虚警来源（飞鸟反光/运动轨迹） |
| airplane | 飞机 | 虚警来源（航线灯轨迹） |
| satellite | 卫星 | 虚警来源（缓慢移动光点） |
| star | 恒星 | 弱小目标 + 静止虚警来源 |

Baseline 关键指标：`meteor Recall=0.9365`，`star Recall=0.0558`。

## 入 Git 的内容

- `data/README.md`（本文件）
- `data/samples/`：少量（几张）样例图 + 对应 label，用于快速验证流程
- `data/metadata/`：数据划分清单、统计信息（CSV/JSON，纯文本，体积小）

## 注意事项

- 大文件（原始图、压缩包、数据库、完整模型权重）已被 `.gitignore` 忽略，请勿 `git add`。
- 若更换 / 新增数据集，请在本文件补充来源、许可证与获取方式，保证可复现。
- `scripts/download_uaemmn.py` 为 UAEMMN 公开数据集下载脚本，当前 Baseline 实际使用本地 `MeteorCam` 数据；UAEMMN 可作为后续跨域/补充数据备用。
