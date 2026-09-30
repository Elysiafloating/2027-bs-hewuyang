# 周记（weekly_log）

## 2026-W（09-30）

- 确定毕设仓库结构 `2027-bs-meteor`，按标准目录骨架 + 提交规范搭建。
- 明确题目（来自老师文件）：**面向流星监测的改进 YOLO 弱小目标检测与虚警抑制方法研究**。
  - 来源：`题目与任务要求总结.docx`、`技术方案与参考文献建议.docx`（曾维老师组 V2）。
  - 关键约束：star 类 Recall 当前为 0，须在开题阶段交**数据体检报告**定位根因；
    措施从数据侧走到模型侧；NWD 因 YOLOv8 anchor-free 需说明适配。
- 完成文档填充：`topic_confirm` / `task_requirements` / `technical_route` /
  `literature_list` / `verified_references`（NWD 正式版已核实）。
- 重写 `.gitignore`：落实"可提交/不提交"清单（数据集、权重、.venv、Conda、build、
  Vivado 临时目录、node_modules、隐私数据、版权 PDF 均不入库）。
- 新增 `data/metadata/data_health_report.md` 体检模板、`reports/` 小型 PDF 目录。
- 待办（旧）：下载 UAEMMN → 核对类别 → 填 data.yaml → 跑 Baseline → 10 月前决定是否补数据。

## 2026-W（09-30）后续更新

- 接入本地真实数据集 **MeteorCam**（`D:/data_tianwen/MeteorCam/meteor_yolo_split`），确认类别为 5 类：
  meteor / seagull / airplane / satellite / star。
- 更新 `configs/data.yaml`、`data/README.md`、所有设计/进度文档为 5 类设定。
- 将之前 `D:/data_tianwen/MeteorDetection/runs/detect/baseline_yolov8n/` 的真实 Baseline 指标
  回填到 `experiments/baseline/metrics.csv` 与 `notes.md`：
  - 整体 mAP@0.5=0.5908，mAP@0.5:0.95=0.26791
  - meteor Recall=0.9365，star Recall=0.0558
- 更新 `experiments/baseline/config.yaml` 与真实训练参数一致（seed=0，epochs=100，lr0=0.01 等）。
- 仓库名从 `2027-bs-meteor` 改为 `2027-bs-hewuyang`（GitHub 已重命名）。

---

（每周追加，建议正序 + 日期标题）
