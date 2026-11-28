# harshacreate/NeuralEdge-IDS

⭐ 3 · Python · MIT · 推送 2026-11-27 · [GitHub](https://github.com/harshacreate/NeuralEdge-IDS) · 个人维护

**用合成 IoT 流量对比集中式与联邦式训练的威胁检测实验项目**

该项目为摄像头、恒温器、门锁、集线器生成合成 IoT 流量，分别训练一个集中式模型和联邦式（分设备训练后合并）模型，对比两种方式在正常测试数据与流量分布变化下的检测率、误报率与 F1，并统计联邦方式训练期通信量。流量为项目自造、非真实网络数据，README 明确列出特征集小、结果不外推到真实设备、不构成隐私保证等限制。提供 Docker 与 venv+make 两种运行方式及 Web 界面。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一数据上对比单模型与联邦合并模型两条训练路径
- 报告流量分布变化下的检测率/误报率/F1 变化
- 统计联邦训练通信量（1,400 vs 9,000 数值传输）
- Docker 一键运行，附带本地测试与绘图命令

## 适用场景

- 复现集中式与联邦学习在 IoT 入侵检测上的对比实验
- 评估正常流量分布变化对检测模型指标的影响
- 学习联邦学习实验的搭建与结果展示流程

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: NeuralEdge-IDS compares two ways to train a small threat detector using made-up IoT traffic. It checks how the resul
> L9: The project makes sample traffic for cameras, thermostats, locks, and hubs. One model trains on all the data. The ot
> L25: The combined model sent 1,400 numbers during training. The one-model setup counted 9,000. This is only a count of n

## 星数曲线

```mermaid
xychart-beta
    title "harshacreate/NeuralEdge-IDS 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-26 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `d4231507e00a` · [字段定义](../../DATASET.md)*
