# GradientHQ/symphony

⭐ 48 · Python · MIT · 推送 2025-10-30 · [GitHub](https://github.com/GradientHQ/symphony) · [官网](https://arxiv.org/abs/2508.20019) · 组织维护

**在消费级边缘设备上运行去中心化多智能体协作的框架**

Symphony 是一个去中心化多智能体框架，通过信标（Beacon）引导的任务路由和思维链（CoT）投票机制，让分布在异构边缘设备上的智能体协作完成任务。无需中央编排器，采用去中心化账本跟踪智能体能力与声誉，支持全局广播与邻居 P2P 两种网络拓扑。面向消费级硬件（RTX 3060/4090、Jetson、Apple M 系列）编排轻量模型（如 Mistral-7B、DeepSeek-LLM-7B-chat）。以 Python 库形式提供 Agent/User/CapabilityManager 等核心类，通过 git clone 源码安装，配套论文引用格式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 信标引导的能力感知任务路由与负载均衡
- 多路径 CoT 并行推理与可靠性加权多数投票
- 无中央编排器的去中心化协调与容错
- 支持全局广播与邻居广播（P2P）两种网络拓扑

## 适用场景

- 把多台家用 GPU 设备组成智能体网络协同执行任务
- 在不依赖服务器级 GPU 的情况下部署多智能体系统
- 研究去中心化智能体协作与 CoT 投票机制

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L10: **Symphony** is a groundbreaking decentralized multi-agent framework that enables intelligent agents to collaborate
> L67: - **🖥️ Worker Nodes**: Edge devices with local LLM engines and specialized prompts

## 星数曲线

```mermaid
xychart-beta
    title "GradientHQ/symphony 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-26 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `01070b0a5b4a` · [字段定义](../../DATASET.md)*
