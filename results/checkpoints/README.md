#  checkpoints 说明

本目录用于存放训练得到的模型权重（`.pt`），但 **`.pt` 文件已被 `.gitignore` 忽略，不入库**。

## 本地权重

| 文件 | 来源 | 说明 |
|---|---|---|
| `baseline_yolov8n_best.pt` | `D:/data_tianwen/MeteorDetection/runs/detect/baseline_yolov8n/weights/best.pt` | Baseline（YOLOv8n，5 类）最佳权重，约 6 MB |

## 复现方式

1. 按 `data/README.md` 把本地真实数据链接到 `data/raw/`。
2. 运行：
   ```bash
   python src/train.py --config experiments/baseline/config.yaml
   ```
3. 或直接使用本目录权重做推理：
   ```bash
   python src/detect.py --weights results/checkpoints/baseline_yolov8n_best.pt --source data/samples
   ```

## 分发

如需分享，请通过 GitHub Release 附件或网盘，不要在 Git 中提交 `.pt`。
