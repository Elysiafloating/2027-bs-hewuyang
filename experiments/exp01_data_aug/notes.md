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
