# Experiment ID
EXP-001

## Purpose
验证**数据侧改进**（star 类过采样 + 小目标切片增强 + 难例负样本挖掘）能否：
1. 提升 star 类 Recall（Baseline 仅 0.0558）；
2. 降低 seagull / airplane / satellite / star 等虚警类的误检。

## Compared with
Baseline（EXP-000）

## Configuration
- 继承 baseline 超参（seed=0，5 类）
- 新增：star 过采样、SliceAided 切片增强、mosaic 比例降至 0.5、难例负样本挖掘
- 详见 `config.yaml`

## Dataset
同 Baseline（`D:/data_tianwen/MeteorCam/meteor_yolo_split`，5 类）；
叠加过采样与切片增强（在线）。

## Random seed
0

## Command
见 `command.txt`：
```
python src/train.py --config experiments/exp01_data_aug/config.yaml
```

## Result
（待跑，回填 `metrics.csv`）

## Conclusion
（待填：若 star R 明显提升 → 根因为不平衡/样本不足；若仍≈0 → 转向标注尺度/分配策略根因）

## Problems
（待记录）

## Implementation Note（实现状态）
- `config.yaml` 中 `data_side`（star 过采样 / 切片增强 / mosaic 比例 / 难例负样本）当前为**配置声明**，`src/train.py` 仅读取 `training.*` 超参，不会自动实现这些增强。
- 真正实现需在 `src/` 中接入自定义数据增强（如 Albumentations、Copy-Paste、SliceAidedHyperInference），或改写 Ultralytics `Augment` / `build_dataloader`。
- 当前 exp01 与 baseline 的**唯一可比差异**来自 `training` 超参一致性（`inherits: baseline`）；增强效果待自定义模块接入后生效，届时本文件需补充实际增强实现说明。
