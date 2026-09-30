# Experiment ID
EXP-001

## Purpose
验证**数据侧改进**（star 类过采样 + 小目标切片增强）能否提升 star 类 Recall，
从而判断 Baseline star R=0 是否源于样本不足 / 类别不平衡。

## Compared with
Baseline（EXP-000）

## Configuration
- 继承 baseline 超参
- 新增：star 过采样、SliceAided 切片增强、mosaic 比例降至 0.5
- 详见 `config.yaml`

## Dataset
同 Baseline；叠加过采样与切片增强（在线）。

## Random seed
42

## Command
见 `command.txt`。

## Result
（待跑，回填 `metrics.csv`）

## Conclusion
（待填：若 star R 明显提升 → 根因为不平衡/样本不足；若仍≈0 → 转向标注尺度/anchor 根因）

## Problems
（待记录）

## Implementation Note（实现状态）
- `config.yaml` 中 `data_side`（star 过采样 / 切片增强 / mosaic 比例）当前为**配置声明**，`src/train.py` 仅读取 `training.*` 超参，不会自动实现这些增强。
- 真正实现需在 `src/` 中接入自定义数据增强（如 Albumentations、Copy-Paste、SliceAidedHyperInference），或改写 Ultralytics `Augment` / `build_dataloader`。
- 当前 exp01 与 baseline 的**唯一可比差异**来自 `training` 超参一致性（`inherits: baseline`）；增强效果待自定义模块接入后生效，届时本文件需补充实际增强实现说明。
