# 系统架构（system_architecture）

## 模块划分

```
┌──────────────────────────────────────────────────────────┐
│                      流星识别系统                          │
├──────────────┬──────────────────┬────────────────────────┤
│  数据层      │  模型层          │  应用/评测层            │
│ data/              │  src/train.py    │  src/detect.py          │
│  MeteorCam(本地)   │  YOLOv8(n/s)     │  推理 + 可视化          │
│  UAEMMN(备用)      │  configs/        │  results/ 指标 & 图     │
│  划分/增强         │                  │                         │
└──────────────┴──────────────────┴────────────────────────┘
```

## 数据流向

1. **输入**：夜空图像（本地 MeteorCam 数据集，YOLO 格式 `images/ + labels/`；UAEMMN 作为公开备用数据集）。
2. **预处理**：resize 至 `imgsz`（默认 640），Mosaic / 翻转 / 亮度增强。
3. **模型**：YOLOv8 主干 + 检测头，输出 (x,y,w,h,conf,cls)。
4. **后处理**：NMS 去重，按置信度阈值过滤。
5. **输出**：检测框叠加图、`labels/*.txt` 预测文件、指标表。

## 目录与模块对应

| 模块 | 路径 | 说明 |
|---|---|---|
| 训练 | `src/train.py` | 读取 `configs/data.yaml`，训练并落盘到 `experiments/` |
| 推理 | `src/detect.py` | 读取权重，输出结果到 `results/` |
| 配置 | `configs/data.yaml` | 数据集路径、类别数、类名 |
| 数据 | `data/` | 数据集说明 + 少量样例（大文件不入库） |
| 实验 | `experiments/` | 每个实验独立子目录（baseline/exp01/exp02） |
| 结果 | `results/` | tables / figures / logs / checkpoints |

## 部署 & 复现

- 训练超参、随机种子写入实验目录的 `args.yaml`，保证可复现。
- 权重通过 GitHub Release 附件分发（不入库，见 `.gitignore`）。
