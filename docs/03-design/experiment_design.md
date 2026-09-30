# 实验设计（experiment_design）

## 评价指标

- **mAP@0.5**：主指标（IoU 阈值 0.5 的平均精度）。
- **Precision / Recall**：衡量误检与漏检。
- **推理速度**（FPS）：若涉及实时性。

## 实验规划

| 实验 | 目的 | 关键变量 | 落盘 |
|---|---|---|---|
| baseline | 验证流程跑通 | YOLOv8n，默认超参 | `experiments/baseline/` |
| exp01 | 尺度对比 | YOLOv8s vs n | `experiments/exp01/` |
| exp02 | 数据增强 / 负样本 | 加背景负样本 | `experiments/exp02/` |

## 消融思路（可选）

- 数据增强组合（Mosaic on/off、亮度抖动）
- 输入分辨率（640 vs 1280）
- 置信度阈值对 P/R 的权衡

## 记录规范

每个实验目录至少包含：

```
experiments/exp0X/
├── args.yaml        # 超参 & 随机种子
├── metrics.csv      # epoch → mAP/P/R
└── README.md        # 实验目的、结论、对比
```

## 结果归档

- 指标表 → `results/tables/`
- 可视化结果图 → `results/figures/`
- 训练日志 → `results/logs/`
- 最佳权重 → `results/checkpoints/`（Release 分发）
