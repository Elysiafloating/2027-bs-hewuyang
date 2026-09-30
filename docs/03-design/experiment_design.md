# 实验设计（experiment_design）

> 对齐 `experiments/` 实际目录：`baseline/` + `exp01_data_aug/` + `exp02_nwd_head/`。
> 每个实验目录强制四件套：`config.yaml` + `command.txt` + `notes.md` + `metrics.csv`（见 `experiments/README.md`）。
> 运行入口统一为 `python src/train.py --config experiments/<name>/config.yaml`。

## 评价指标

- **mAP@0.5**：主指标（IoU 阈值 0.5 的平均精度）。
- **mAP@0.5:0.95**：综合定位精度。
- **Precision / Recall**：分总体与分 5 类记录（重点盯 `star_recall`，同时关注 seagull / airplane / satellite 虚警率）。
- **虚警率 FAR（False Alarm Rate）**：背景 / 非目标被误检为 meteor/star 的比例，衡量虚警抑制。
- **推理速度（FPS）**：若涉及实时监测场景。

## 实验规划

| 实验 | 侧重点 | 关键变量 | 落盘 |
|---|---|---|---|
| `baseline` | 验证整条流程跑通 | YOLOv8n + 默认超参（无改进） | `experiments/baseline/` |
| `exp01_data_aug` | **数据侧**：缓解 star 类 Recall=0 | star 过采样 + 小目标切片增强 + 降 mosaic | `experiments/exp01_data_aug/` |
| `exp02_nwd_head` | **模型侧**：极小尺度 / anchor 不匹配 | NWD 度量 + 改进检测头（小目标分支 + CBAM） | `experiments/exp02_nwd_head/` |

- exp01 / exp02 的 `config.yaml` 通过 `inherits: baseline` 继承基线超参，确保除目标变量外严格一致。
- exp01 / exp02 的改进策略（数据增强、NWD、检测头）当前为**配置声明**，需在 `src/` 中实现对应模块后才会真正生效（见各自 `notes.md` 的 Implementation Note）。

## 消融 / 对比思路

- **数据侧**：star 过采样 on/off、SliceAided 切片 on/off、mosaic 比例（1.0 vs 0.5）。
- **模型侧**：IoU Loss vs NWD Loss（β=2.0）、原始检测头 vs 小目标分支 + CBAM。
- **输入分辨率**：640 vs 1280（小目标通常获益）。
- **置信度阈值**对 P/R 与 FAR 的权衡（后处理虚警抑制）。

## 记录规范（四件套）

```
experiments/<exp_name>/
├── config.yaml     # 超参 & 随机种子（可复现，支持 inherits）
├── command.txt     # 完整可复现命令（--config 形式）
├── notes.md        # 实验日志（EXP 模板 + 实现状态）
└── metrics.csv     # epoch → P / R / mAP / 分类比 / 虚警
```

## 结果归档

- 指标汇总表 → `results/tables/`
- 可视化结果图（含 star 类检测框、虚警样例）→ `results/figures/`
- 训练日志 → `results/logs/`
- 最佳权重 → `results/checkpoints/`（通过 Release 分发，不入库）
