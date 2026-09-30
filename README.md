# 2027届本科毕业论文

> 仓库：`2027-bs-hewuyang` · 题目冻结区见 `docs/01-topic/` · 实验规范见 `experiments/README.md`

## 基本信息

| 项 | 内容 |
|---|---|
| 姓名 | 何雾阳 |
| 学号 | 202319120902 |
| 专业 | 智能科学与技术 |
| 指导教师 | 曾维 |
| 毕业论文题目 | 面向流星监测的改进 YOLO 弱小目标检测与虚警抑制方法研究 |
| 研究方向 | 计算机视觉 / 弱小目标检测 / 虚警抑制 |

## 一、研究问题

1. **研究对象**：夜空流星监测图像中的弱小目标与常见虚警，基于本地数据集 **MeteorCam**（`D:/data_tianwen/MeteorCam/meteor_yolo_split`）。
2. **当前问题**：YOLOv8 基线在 **star** 类上 **Recall=0.0558**（极低漏检）；同时夜空背景含 seagull、airplane、satellite、star 等多类虚警，现有检测头对弱小目标和外观相似干扰区分能力不足。
3. **本论文准备解决的问题**：定位并解释 star 类 Recall 极低的根因（标注尺度极小、类别不平衡、anchor-free 分配不匹配），提出面向弱小目标的检测改进与虚警抑制方法，并通过对比实验 / 消融实验 / 异常分析验证有效性。

## 二、最低完成要求

- [x] **Baseline / 基础系统**：YOLOv8n 基线训练与推理流程跑通（指标已回填 `experiments/baseline/`）
- [ ] **核心方法或关键机制**：≥1 项针对性改进（数据侧 / 模型侧，见技术路线）
- [ ] **对比实验**：改进 vs Baseline 的 mAP / P / R 对比
- [ ] **消融/性能测试**：逐项消融改进模块贡献
- [ ] **错误或异常情况分析**：如实报告 star 类失效根因、seagull/airplane/satellite/star 虚警来源、失败样例
- [ ] **完整毕业论文**：按学校模板提交

## 三、拓展目标

- [ ] 数据侧改进：star 类过采样 / 小目标切片（SliceAided）增强 / 负样本挖掘
- [ ] 模型侧改进：引入 **NWD**（Normalized Wasserstein Distance）度量、改进检测头、轻量注意力
- [ ] 虚警抑制：后处理阈值 / 时序一致性（多帧关联）策略
- [ ] 在更大规模 / 不同相机源上做泛化测试

## 四、技术路线

总体流程：**数据体检 → YOLOv8 Baseline（定位 star Recall 极低根因）→ 核心工作（数据侧 + 模型侧改进）→ 实验设计与对比/消融 → 交付物与风险分析**。

详细流程、选型依据与风险见 👉 [`docs/01-topic/technical_route.md`](docs/01-topic/technical_route.md)
（题目冻结区另含 [`topic_confirm.md`](docs/01-topic/topic_confirm.md)、[`task_requirements.md`](docs/01-topic/task_requirements.md)）。

## 五、当前进展

- **当前阶段**：开题准备 / 数据体检
- **最近完成**：仓库目录规范化；本地 MeteorCam 5 类数据集接入；Baseline 真实指标已回填
- **当前问题**：star 类 Baseline Recall=0.0558 待定位根因；seagull/airplane/satellite/star 虚警待抑制
- **下一步**：① 完成 `data/metadata/data_health_report.md` 数据体检 → ② 在 `experiments/baseline/notes.md` 中形成根因结论 → ③ 推进 exp01/exp02 改进实验

## 六、主要实验结果

| Experiment | Result | Status |
|---|---|---|
| Baseline (YOLOv8n) | mAP@0.5=0.5908，meteor R=0.9365，**star R=0.0558** | ✅ 已跑通并回填 |
| exp01 数据增强 | — | 计划 |
| exp02 NWD + 检测头 | — | 计划 |

> 指标记录在 `experiments/*/metrics.csv`，异常分析在 `experiments/*/notes.md`。

## 七、仓库目录说明

```
2027-bs-hewuyang/
├── README.md                 # 本文件（毕业论文总览）
├── .gitignore                # 提交规范（见下）
├── docs/
│   ├── 01-topic/             # ★题目冻结区：topic_confirm / task_requirements / technical_route
│   ├── 02-literature/        # 文献清单 / 已核实文献 / reading_notes/
│   ├── 03-design/            # 系统架构 / 实验设计 / figures/
│   └── 04-meetings/          # YYYY-MM-DD.md 组会记录
├── src/                      # train.py / detect.py（YOLOv8 二次开发）
├── configs/                  # data.yaml（数据集配置，5 类）
├── scripts/                  # download_uaemmn.py（UAEMMN 公开数据备用脚本）
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

- **代码**：基于 Ultralytics 二次开发 `src/train.py`、`src/detect.py`；维护 `configs/data.yaml`；编写 `scripts/download_uaemmn.py` 作为 UAEMMN 公开数据获取脚本。
- **实验**：设计 baseline / 数据增强 / 模型改进三阶段实验（见 `experiments/`），完成数据体检与 star R=0.0558 根因分析。
- **数据**：本地 MeteorCam 数据集接入、组织、体检；构建小型样例 `data/samples/`。
- **论文**：本仓库全部文档与毕业论文 Markdown 初稿撰写。

> 第三方项目均注明来源（见第九节），改进点明确标注于各实验 `notes.md`。

## 九、参考项目与第三方代码

- **项目**：YOLOv8（Ultralytics）
  - URL：https://github.com/ultralytics/ultralytics
  - License：AGPL-3.0
  - 本项目修改内容：基于其 `train` / `detect` 接口二次开发 `src/train.py`、`src/detect.py`
- **本地数据集**：MeteorCam（`D:/data_tianwen/MeteorCam/meteor_yolo_split`）
  - 类别：meteor / seagull / airplane / satellite / star
  - 本项目使用方式：本地链接 / 复制到 `data/raw`，经 `configs/data.yaml` 组织训练
- **公开备用数据集**：UAEMMN（UAE Meteor Monitoring Network）
  - URL：https://zenodo.org/records/14512061
  - License：CC BY 4.0（待核实）
  - 本项目使用方式：经 `scripts/download_uaemmn.py` 下载，可作为跨域/补充数据备用

## 十、环境与复现

- **OS**：Windows 10（本地开发） / Linux（训练服务器，可选）
- **Python**：3.10+
- **深度学习框架**：PyTorch 2.x + Ultralytics 8.x
- **CUDA / cuDNN**：11.8（本地 GPU）
- **关键依赖**：opencv-python、numpy、pandas、PyYAML、tqdm、ultralytics

```bash
# 1. 安装依赖（建议在独立 venv，不入库）
pip install -r requirements.txt        # 或：pip install ultralytics torch

# 2. 把本地真实数据链接到仓库（Windows 推荐 Junction）
# New-Item -ItemType Junction -Path "2027-bs-hewuyang/data/raw" -Target "D:/data_tianwen/MeteorCam/meteor_yolo_split"

# 3. 跑通 Baseline（指标写入 experiments/baseline/metrics.csv）
python src/train.py --config experiments/baseline/config.yaml

# 4. 推理 + 可视化框选
python src/detect.py --weights results/checkpoints/best.pt --source data/samples
```

复现细节与随机种子见 `experiments/*/config.yaml` 与 `command.txt`。

---
