# 实验记录（experiments）

本目录为**强制规范目录**。每个实验一个独立子目录，子目录内**至少**包含以下四件套：

```
experiments/<exp_name>/
├── config.yaml     # 超参 & 随机种子（可复现）
├── command.txt     # 完整可复现运行命令
├── notes.md        # 实验日志（按下方 EXP 模板）
└── metrics.csv     # epoch → P / R / mAP / 分类比指标
```

## 子目录约定

| 目录 | 含义 | 状态 |
|---|---|---|
| `baseline/` | 基线：YOLOv8n + 默认超参，验证整条流程 | 待跑 |
| `exp01_data_aug/` | 数据侧改进：star 类过采样 / 小目标切片增强 | 计划 |
| `exp02_nwd_head/` | 模型侧改进：NWD 度量 + 改进检测头 / 注意力 | 计划 |

> 后续实验继续按 `exp03_xxx/`、`exp04_xxx/` 命名，保持 `_xxx` 描述性后缀。

## 实验日志模板（notes.md）

每个实验的 `notes.md` 必须包含如下结构：

```markdown
# Experiment ID
EXP-000

## Purpose
验证……

## Compared with
Baseline

## Configuration
- 模型：YOLOv8n
- 数据：configs/data.yaml
- 关键超参：epochs=100, imgsz=640, batch=16, optimizer=auto

## Dataset
UAEMMN（Zenodo 14512061），train/val 划分见 data.yaml

## Random seed
42

## Command
python src/train.py --name baseline --epochs 100 --imgsz 640 --batch 16 --seed 42

## Result
（贴 metrics.csv 关键行 / 截图）

## Conclusion
……

## Problems
- star 类 Recall=0：根因待定位（标注尺度极小 / 类别不平衡 / anchor 不匹配）
```

## 训练落盘

`src/train.py` 默认 `project="runs"`，`name` 即实验子目录名（如 `baseline`）。
权重与日志落到 `runs/<name>/`，**不入库**；只把 `metrics.csv` 与 `notes.md` 留在 `experiments/<name>/`。
