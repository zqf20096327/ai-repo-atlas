# amazon-science/auction-gym

⭐ 203 · Jupyter Notebook · Apache-2.0 · 推送 2026-02-11 · [GitHub](https://github.com/amazon-science/auction-gym) · 组织维护

**在线广告拍卖的仿真环境：可复现评测 bandit 与 RL 出价方法**

面向在线广告拍卖场景的仿真环境，用于对 bandit 与强化学习方法在广告分配与出价问题上的离线可复现评测。用户通过 JSON 配置文件定义环境与竞价者，运行脚本后输出多轮拍卖的 .csv 原始指标与可视化 PDF。提供两个 Jupyter 探索性 notebook（竞争效应、bid shading 效应）。配套论文发表于 KDD 2023 Applied Data Science Track，AdKDD '22 研讨会早期版本获 Best Paper Award。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一框架用于基准测试 learning-to-bid 新方法
- JSON 配置文件定义环境与竞价者，输出 CSV 指标与可视化
- 两个入门 notebook 演示二价拍卖竞争效应与一价拍卖 bid shading 效应

## 适用场景

- 我想在可复现的拍卖仿真中评测出价策略
- 研究 bandit/RL 方法在广告分配中的表现
- 复现论文报告的实验结果

## 场景标签

`模型评测` `强化学习` · 领域:评测与运维

## 证据(README 行号)

> L3: This repository contains the source code for AuctionGym: a simulation environment that enables reproducible offline 
> L14: AuctionGym aims to mitigate this problem, by providing a unified framework that practitioners and research can use 

## 星数曲线

```mermaid
xychart-beta
    title "amazon-science/auction-gym 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 202 --> 204
    line [203, 203]
```

2026-10-18 203 → 2026-10-27 203（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `841ab6d41402` · [字段定义](../../DATASET.md)*
