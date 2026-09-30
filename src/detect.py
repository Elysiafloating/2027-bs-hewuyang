"""流星检测推理 / 可视化脚本 (YOLOv8)。

读取训练好的权重，对单图或目录做推理，将检测框叠加回原图，
结果（图 + 预测标签）保存到 results/。
"""

import argparse

from ultralytics import YOLO


def main():
    parser = argparse.ArgumentParser(description="Infer meteor detections")
    parser.add_argument(
        "--weights",
        default="experiments/exp01_baseline/weights/best.pt",
        help="训练好的权重",
    )
    parser.add_argument("--source", default="data/samples", help="图片 / 目录 / 视频")
    parser.add_argument("--conf", type=float, default=0.25, help="置信度阈值")
    parser.add_argument("--name", default="infer_demo", help="结果子目录名")
    args = parser.parse_args()

    model = YOLO(args.weights)
    model.predict(
        source=args.source,
        conf=args.conf,
        save=True,
        project="results",
        name=args.name,
    )


if __name__ == "__main__":
    main()
