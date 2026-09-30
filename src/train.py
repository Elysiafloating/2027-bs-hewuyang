"""流星检测训练脚本 (YOLOv8)。

基于 Ultralytics 实现，数据集为 UAEMMN（Zenodo 14512061）。
训练产物落盘到 experiments/<name>/，便于按实验归档。
"""

import argparse

from ultralytics import YOLO


def main():
    parser = argparse.ArgumentParser(description="Train YOLOv8 meteor detector")
    parser.add_argument("--data", default="configs/data.yaml", help="数据集配置文件")
    parser.add_argument("--model", default="yolov8n.pt", help="预训练权重 / 尺寸")
    parser.add_argument("--epochs", type=int, default=100)
    parser.add_argument("--imgsz", type=int, default=640)
    parser.add_argument("--batch", type=int, default=16)
    parser.add_argument("--name", default="exp01_baseline", help="实验名")
    parser.add_argument("--seed", type=int, default=42, help="随机种子，保证可复现")
    args = parser.parse_args()

    model = YOLO(args.model)
    model.train(
        data=args.data,
        epochs=args.epochs,
        imgsz=args.imgsz,
        batch=args.batch,
        name=args.name,
        project="experiments",
        seed=args.seed,
        exist_ok=True,
    )


if __name__ == "__main__":
    main()
