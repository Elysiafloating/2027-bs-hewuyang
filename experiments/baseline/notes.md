# Experiment ID
EXP-000

## Purpose
验证 YOLOv8n 在 UAEMMN 上的整条训练/推理流程是否跑通，并**定位 star 类 Baseline Recall=0 的根因**。

## Compared with
（无，本实验即基线）

## Configuration
- 模型：YOLOv8n（pretrained yolov8n.pt）
- 数据：configs/data.yaml（meteor + star 两类）
- 关键超参：epochs=100, imgsz=640, batch=16, optimizer=auto, seed=42
- 详见 `config.yaml`

## Dataset
UAEMMN（Zenodo 14512061）。train/val 划分见 `configs/data.yaml`。

## Random seed
42（deterministic=true）

## Command
见 `command.txt`：
```
python src/train.py --name baseline --model yolov8n.pt --data configs/data.yaml --epochs 100 --imgsz 640 --batch 16 --optimizer auto --seed 42 --device 0
```

## Result
（待跑。关键指标回填到 `metrics.csv`）

预期关注：
- 整体 mAP@0.5 / mAP@0.5:0.95
- **star 类 Recall 是否≈0**（首要问题）
- meteor 类 Recall / Precision
- 虚警率（背景误检为 meteor/star 的数量）

## Conclusion
（待填）

## Problems
- [ ] **star 类 Recall=0**：根因待定位，候选：
  1. 标注框尺度极小（数像素），低于检测头最小可检尺度；
  2. meteor:star 类别极度不平衡，损失被 meteor 主导；
  3. 默认 anchor 与目标尺度严重不匹配；
  4. 训练样本不足 / 标签噪声。
- [ ] 虚警来源：热噪声、飞机/卫星轨迹被误检，需在后处理或模型侧抑制。

## Diagnosis Plan（根因诊断计划）

为区分上述 4 个候选根因，跑 Baseline 时同步执行以下诊断（脚本落 `scripts/`）：

1. **标注尺度统计**：统计 `star` 类所有标注框的宽高（像素）与占图比例，确认是否普遍 < 检测头最小可检尺度（YOLOv8 约 1–2 px）。
   - 若 90% 框 < 3 px → 命中根因 ①（极小标注尺度）。
2. **类别计数**：统计 train/val 中 `meteor` vs `star` 的实例数与图像数，计算不平衡比。
   - 若 star 占比极低 → 命中根因 ②（类别不平衡）。
3. **Anchor / 尺度匹配**：观察 Baseline 末层特征图上 star 目标中心激活是否稀疏；或临时把 `imgsz` 提升到 1280 复跑，若 star R 回升 → 命中根因 ③（尺度 / anchor 不匹配）。
4. **标签质量与样本量**：抽查 `star` 标注是否漏标、错标；统计含 star 的图像数。
   - 若含 star 图像极少或噪声高 → 命中根因 ④（样本不足 / 标签噪声）。

- 诊断脚本输出写入 `data/metadata/data_health_report.md`。
- 诊断结论回填本文件 `Conclusion`，并据此决定 exp01（数据侧）或 exp02（模型侧）为主攻方向。
