"""流星检测训练脚本 (YOLOv8)。

读取 experiments/<name>/config.yaml，支持 inherits 继承基础配置，
将 model / data / training 字段映射给 Ultralytics 的 model.train()。
CLI 参数可覆盖 config 中的同名项。
"""

import argparse
import os

import yaml


def load_config(path):
    """加载 YAML 配置，支持 inherits 继承（同层 ../<name>/config.yaml）。"""
    with open(path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f) or {}
    if "inherits" in cfg:
        base_name = cfg["inherits"]
        base_path = os.path.join(os.path.dirname(path), "..", base_name, "config.yaml")
        if os.path.isfile(base_path):
            base = load_config(base_path)
            merged = {**base, **{k: v for k, v in cfg.items() if k != "inherits"}}
            for key in ("model", "data", "training"):
                if key in base and key in cfg:
                    merged[key] = {**base[key], **cfg[key]}
            return merged
    return cfg


def main():
    parser = argparse.ArgumentParser(description="Train YOLOv8 meteor detector")
    parser.add_argument("--config", default="experiments/baseline/config.yaml",
                        help="实验配置 YAML（experiments/<name>/config.yaml）")
    parser.add_argument("--data", default=None, help="覆盖 data.yaml 路径")
    parser.add_argument("--model", default=None, help="覆盖预训练权重")
    parser.add_argument("--name", default=None, help="覆盖实验名（落盘目录）")
    parser.add_argument("--epochs", type=int, default=None)
    parser.add_argument("--imgsz", type=int, default=None)
    parser.add_argument("--batch", type=int, default=None)
    parser.add_argument("--optimizer", default=None)
    parser.add_argument("--device", default=None)
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--lr0", type=float, default=None)
    parser.add_argument("--momentum", type=float, default=None)
    parser.add_argument("--weight_decay", type=float, default=None)
    parser.add_argument("--warmup_epochs", type=float, default=None)
    parser.add_argument("--close_mosaic", type=int, default=None)
    parser.add_argument("--deterministic", default=None)
    args = parser.parse_args()

    cfg = load_config(args.config) if os.path.isfile(args.config) else {}

    m = cfg.get("model", {})
    model_path = args.model or m.get("pretrained") or (m.get("arch", "yolov8n") + ".pt")

    d = cfg.get("data", {})
    data_yaml = args.data or d.get("yaml") or "configs/data.yaml"

    # training.* 直接映射给 model.train()
    train_kwargs = dict(cfg.get("training", {}))

    cli_map = {
        "epochs": args.epochs, "imgsz": args.imgsz, "batch": args.batch,
        "optimizer": args.optimizer, "device": args.device, "seed": args.seed,
        "lr0": args.lr0, "momentum": args.momentum, "weight_decay": args.weight_decay,
        "warmup_epochs": args.warmup_epochs, "close_mosaic": args.close_mosaic,
        "deterministic": args.deterministic,
    }
    for k, v in cli_map.items():
        if v is not None:
            if k == "deterministic":
                v = str(v).lower() == "true"
            train_kwargs[k] = v

    name = args.name or cfg.get("name") or os.path.basename(os.path.dirname(args.config))
    train_kwargs["name"] = name
    train_kwargs["project"] = "experiments"
    train_kwargs["data"] = data_yaml
    train_kwargs["exist_ok"] = True

    print(f"[train] model={model_path}  data={data_yaml}  name={name}")
    print(f"[train] train_kwargs={train_kwargs}")

    model = YOLO(model_path)
    model.train(**train_kwargs)


if __name__ == "__main__":
    main()
