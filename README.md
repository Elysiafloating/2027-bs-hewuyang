# 2027届本科毕业论文

> 仓库：`2027-bs-meteor` · 题目冻结区见 `docs/01-topic/` · 实验规范见 `experiments/README.md`

## 基本信息

| 项 | 内容 |
|---|---|
| 姓名 | 何雾阳 |
| 学号 | 202319120902 |
| 专业 | 智能科学与技术 |
| 指导教师 | 曾维 |
| 毕业论文题目 | 面向流星监测的改进 YOLO 弱小目标检测与虚警抑制方法研究 |
| 研究方向 | 基于深度学习的弱小目标检测（流星监测 / 虚警抑制） |

## 一、研究问题

1. **研究对象**：夜空流星监测图像中的弱小目标——流星（瞬态条纹）与恒星（点状背景），基于公开数据集 **UAEMMN**（Zenodo 14512061）。
2. **当前问题**：YOLOv8 基线在恒星（star）类上 **Recall≈0**，弱小目标（仅数像素）严重漏检；同时夜空噪声（热噪声、飞机/卫星轨迹）造成大量虚警，现有通用检测头对小尺度目标不敏感。
3. **本论文准备解决的问题**：定位并解释 star 类 Baseline Recall=0 的根因（标注尺度极小、类别极度不平衡、anchor 与目标尺度不匹配），提出面向弱小目标的检测改进与虚警抑制方法，并通过对比实验 / 消融实验 / 异常分析验证有效性。

## 二、最低完成要求

- [x] **Baseline / 基础系统**：YOLOv8n 基线训练与推理流程跑通（代码就绪，待跑指标）
- [ ] **核心方法或关键机制**：≥1 项针对性改进（数据侧 / 模型侧，见技术路线）
- [ ] **对比实验**：改进 vs Baseline 的 mAP / P / R 对比
- [ ] **消融/性能测试**：逐项消融改进模块贡献
- [ ] **错误或异常情况分析**：如实报告 star 类失效根因、虚警来源、失败样例
- [ ] **完整毕业论文**：按学校模板提交

## 三、拓展目标

- [ ] 数据侧改进：star 类过采样 / 小目标切片（SliceAided）增强 / 负样本挖掘
- [ ] 模型侧改进：引入 **NWD**（Normalized Wasserstein Distance）度量、改进检测头、轻量注意力
- [ ] 虚警抑制：后处理阈值 / 时序一致性（多帧关联）策略
- [ ] 在更大规模 / 不同相机源上做泛化测试

## 四、技术路线

总体流程：**数据体检 → YOLOv8 Baseline（定位 star Recall=0）→ 核心工作（数据侧 + 模型侧改进）→ 实验设计与对比/消融 → 交付物与风险分析**。

详细流程、选型依据与风险见 👉 [`docs/01-topic/technical_route.md`](docs/01-topic/technical_route.md)
（题目冻结区另含 [`topic_confirm.md`](docs/01-topic/topic_confirm.md)、[`task_requirements.md`](docs/01-topic/task_requirements.md)）。

## 五、当前进展

- **当前阶段**：开题准备 / 数据体检
- **最近完成**：仓库目录规范化；UAEMMN 数据集获取与组织规划；题目与任务书冻结于 `docs/01-topic/`
- **当前问题**：star 类 Baseline Recall=0 待定位（疑似极小标注尺度 / 类别不平衡 / anchor 不匹配）
- **下一步**：① 完成 `data/metadata/data_health_report.md` 数据体检 → ② 跑通 `experiments/baseline` 并记录 `metrics.csv` → ③ 在 `notes.md` 中解释 star R=0 根因

## 六、主要实验结果

| Experiment | Result | Status |
|---|---|---|
| Baseline (YOLOv8n) | mAP@0.5=?，star R=0，meteor R=? | 待跑（重点解释 star R=0） |
| exp01 数据增强 | — | 计划 |
| exp02 NWD + 检测头 | — | 计划 |

> 指标记录在 `experiments/*/metrics.csv`，异常分析在 `experiments/*/notes.md`。

## 七、仓库目录说明

```
2027-bs-meteor/
├── README.md                 # 本文件（毕业论文总览）
├── .gitignore                # 提交规范（见下）
├── docs/
│   ├── 01-topic/             # ★题目冻结区：topic_confirm / task_requirements / technical_route
│   ├── 02-literature/        # 文献清单 / 已核实文献 / reading_notes/
│   ├── 03-design/            # 系统架构 / 实验设计 / figures/
│   └── 04-meetings/          # YYYY-MM-DD.md 组会记录
├── src/                      # train.py / detect.py（YOLOv8 二次开发）
├── configs/                  # data.yaml（数据集配置）
├── scripts/                  # download_uaemmn.py
├── data/
│   ├── README.md             # 数据集获取/组织/不入Git说明
│   ├── metadata/             # data_health_report.md（体检报告）
│   └── samples/              # 小型样例（可入库）
├── experiments/              # ★强制规范：README + baseline/exp01/exp02 四件套
├── results/                  # tables(CSV) / figures / logs / checkpoints(Release)
├── thesis/                   # outline / figures / tables / drafts / references
├── reports/                  # 小型 PDF 报告（可入库例外）
└── progress/                 # milestones / weekly_log / issues
```

## 八、本人主要贡献

- **代码**：基于 Ultralytics 二次开发 `src/train.py`、`src/detect.py`；编写 `scripts/download_uaemmn.py` 数据获取脚本；维护 `configs/data.yaml`。
- **实验**：设计 baseline / 数据增强 / 模型改进三阶段实验（见 `experiments/`），完成数据体检与 star R=0 根因分析。
- **数据**：UAEMMN 数据集下载、组织、体检；构建小型样例 `data/samples/`。
- **论文**：本仓库全部文档与毕业论文 Markdown 初稿撰写。

> 第三方项目均注明来源（见第九节），改进点明确标注于各实验 `notes.md`。

## 九、参考项目与第三方代码

- **项目**：YOLOv8（Ultralytics）
  - URL：https://github.com/ultralytics/ultralytics
  - License：AGPL-3.0
  - 本项目修改内容：基于其 `train` / `detect` 接口二次开发 `src/train.py`、`src/detect.py`
- **数据集**：UAEMMN（UAE Meteor Monitoring Network）
  - URL：https://zenodo.org/records/14512061
  - License：CC BY 4.0（待核实）
  - 本项目使用方式：经 `scripts/download_uaemmn.py` 下载，按 `configs/data.yaml` 组织 `images/labels`

## 十、环境与复现

- **OS**：Windows 10（本地开发） / Linux（训练服务器，可选）
- **Python**：3.10
- **深度学习框架**：PyTorch 2.x + Ultralytics 8.x
- **CUDA / cuDNN**：11.8（本地 GPU）
- **关键依赖**：opencv-python、numpy、pandas、PyYAML、tqdm

```bash
# 1. 安装依赖（建议在独立 venv，不入库）
pip install -r requirements.txt        # 或：pip install ultralytics torch

# 2. 下载并组织数据集
python scripts/download_uaemmn.py --out data/raw

# 3. 跑通 Baseline（指标写入 experiments/baseline/metrics.csv）
python src/train.py --name baseline --epochs 100 --imgsz 640 --batch 16 --seed 42

# 4. 推理 + 可视化框选
python src/detect.py --weights runs/baseline/weights/best.pt --source data/samples
```

复现细节与随机种子见 `experiments/*/config.yaml` 与 `command.txt`。

---
