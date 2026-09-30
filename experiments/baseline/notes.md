# Experiment ID
EXP-000

## Purpose
验证 YOLOv8n 在本地真实流星监测数据上的整条训练/推理流程，并**定位 star 类 Recall 极低的根因**（实测 0.0558）。

## Compared with
（无，本实验即基线）

## Configuration
- 模型：YOLOv8n（pretrained yolov8n.pt）
- 数据：`configs/data.yaml`（5 类：meteor / seagull / airplane / satellite / star）
- 本地真实数据：`D:/data_tianwen/MeteorCam/meteor_yolo_split`（需链接到本仓库 `data/raw`）
- 关键超参：epochs=100, imgsz=640, batch=16, optimizer=auto, seed=0, deterministic=true, device=0
- 完整超参见 `config.yaml`

## Dataset
本地数据集 `D:\data_tianwen\MeteorCam\meteor_yolo_split`，含 5 类夜空目标：
- meteor：流星（真实目标）
- seagull / airplane / satellite：常见虚警来源
- star：恒星（弱小目标 / 静止虚警来源）

train/val/test 划分见 `configs/data.yaml`。

## Random seed
0（deterministic=true）

## Command
见 `command.txt`：
```
python src/train.py --config experiments/baseline/config.yaml
```

## Result
（已回填 `metrics.csv`；关键指标如下）

| epoch | precision | recall | mAP@0.5 | mAP@0.5:0.95 | meteor_recall | star_recall |
|---|---|---|---|---|---|---|
| 1 | 0.00249 | 0.3788 | 0.1652 | 0.05241 | — | — |
| 50 | 0.79541 | 0.51272 | 0.54366 | 0.22991 | — | — |
| 100 | 0.61642 | 0.6008 | 0.59082 | 0.26791 | **0.9365** | **0.0558** |

> 数据来源：`D:/data_tianwen/MeteorDetection/runs/detect/baseline_yolov8n/` 下的 `args.yaml`、`results.csv` 与 `experiment_metrics.json`。

## Conclusion
1. **meteor 类识别效果良好**：最终 Recall=0.9365、mAP@0.5=0.9459，说明模型对流星主目标已基本学会。
2. **star 类 Recall 极低（0.0558）**：不是完全为 0，但几乎漏检；与论文关注的“弱小目标漏检”问题一致，是后续改进的核心对象。
3. **虚警来源多元**：seagull、airplane、satellite 与 star 均会被模型输出，如何在保持 meteor 高召回的同时降低这四类的误检，是“虚警抑制”部分的主攻方向。
4. **训练收敛正常**：整体 mAP@0.5 达到 0.5908，可作为后续改进的可靠基线。

## Problems
- [x] **star 类 Recall 极低（0.0558）**：根因待定位，候选：
  1. 标注框尺度极小（数像素），低于检测头最小可检尺度；
  2. meteor:star 类别极度不平衡，损失被流星/其他虚警类主导；
  3. 默认 anchor-free 分配对 star 这种点状目标不敏感；
  4. star 样本不足 / 与背景恒星特征混淆。
- [x] **虚警来源**：seagull / airplane / satellite / star 均可能产生误检，需在后处理或模型侧抑制。
- [ ] 5 类中除 meteor 外其余 4 类召回/精度差异大，后续需按类别分别分析漏检/误检样例。

## Diagnosis Plan（根因诊断计划）

为区分上述候选根因，跑 Baseline 时同步执行以下诊断（脚本落 `scripts/`）：

1. **标注尺度统计**：统计 `star` 类所有标注框的宽高（像素）与占图比例，确认是否普遍 < 检测头最小可检尺度（YOLOv8 约 1–2 px）。
   - 若 90% 框 < 3 px → 命中根因 ①（极小标注尺度）。
2. **类别计数**：统计 train/val 中 5 类实例数与图像数，计算不平衡比。
   - 若 star 占比极低 → 命中根因 ②（类别不平衡）。
3. **分配策略对照**：观察 star 目标在末层特征图上是否被分配为正样本；或临时把 `imgsz` 提升到 1280 复跑，若 star R 回升 → 命中根因 ③（尺度 / 分配不匹配）。
4. **标签质量与样本量**：抽查 `star` 标注是否漏标、错标；统计含 star 的图像数。
   - 若含 star 图像极少或噪声高 → 命中根因 ④（样本不足 / 标签噪声）。

- 诊断脚本输出写入 `data/metadata/data_health_report.md`。
- 诊断结论回填本文件 `Conclusion`，并据此决定 exp01（数据侧）或 exp02（模型侧）为主攻方向。
