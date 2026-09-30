# 问题跟踪（issues）

| # | 问题 | 类型 | 状态 | 备注 |
|---|---|---|---|---|
| I1 | **star 类 Recall=0.0558**（Baseline 极低，需数据体检定位根因） | 模型/数据 | 🟡 进行中 | 样本量/尺度/标签分配/损失权重 四选根因；虚警类为 seagull/airplane/satellite/star |
| I2 | 训练环境未确认（CUDA / torch 版本） | 环境 | 待解决 | 需确认本地 GPU 可用；Baseline 真实指标来自 D:/data_tianwen/MeteorDetection |
| I3 | 本地 MeteorCam 已接入；UAEMMN 作为公开备用数据 | 数据 | 🟢 已解决 | 用 scripts/download_uaemmn.py 下载 UAEMMN 备用 |
| I4 | 大文件不入库，复现依赖脚本/Release | 工程 | 已知 | 已写入 .gitignore & data/README.md |
| I5 | 10 月前须决定是否补数据/数据合成 | 进度 | 🟡 进行中 | 否则来不及重训 |
| I6 | 参考文献逐条核实真实存在 | 文献 | 🟡 进行中 | 仅 NWD 正式版已核实 |

> 状态：🟢 已解决 / 🟡 进行中 / 🔴 待解决
