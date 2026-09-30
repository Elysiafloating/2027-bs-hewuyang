# Experiment ID
EXP-002

## Purpose
验证**模型侧改进**（NWD 度量 + 改进检测头 / 轻量注意力）能否解决“极小标注尺度 / anchor 不匹配”导致的 star 类漏检，
并作为虚警抑制的模型侧基础。

## Compared with
Baseline（EXP-000）、exp01 数据增强（EXP-001）

## Configuration
- 继承 baseline 超参
- 新增：NWD loss（β=2.0）、改进检测头（小目标分支 + CBAM 注意力）
- 详见 `config.yaml`

## Dataset
同 Baseline。

## Random seed
42

## Command
见 `command.txt`。

## Result
（待跑，回填 `metrics.csv`）

## Conclusion
（待填：对比 Baseline/exp01，量化 NWD+检测头对 star R 与虚警率的影响）

## Problems
- [ ] NWD 两版文献出处核实（见 `docs/02-literature/verified_references.md`）
- [ ] 改进检测头是否引入额外虚警，需结合后处理评估
