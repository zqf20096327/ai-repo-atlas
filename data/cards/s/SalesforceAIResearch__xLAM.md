# SalesforceAIResearch/xLAM

⭐ 640 · Python · Apache-2.0 · 推送 2026-06-02 · [GitHub](https://github.com/SalesforceAIResearch/xLAM) · 组织维护

**Salesforce 的大动作模型系列：面向 Agent 的函数调用与多轮对话模型**

由 Salesforce AI Research 维护的 Large Action Model 模型家族仓库，发布 1B 至 141B 参数的多组模型权重，面向函数调用、多轮对话与通用 Agent 任务，提供 GGUF 格式下载。兼容 vLLM、FastChat 与 Transformers 推理框架，附 OpenAI API 兼容端点的 vLLM 部署流程（含专属 tool call parser 插件）。仓库同时包含 ActionStudio 训练框架（统一轨迹数据格式、训练配置跟踪）与 APIGen-MT 多轮数据生成管线。代码 Apache 2.0，数据集 CC-BY-NC-4.0，声明仅供研究用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 1B–141B 参数的模型家族，覆盖函数调用与多轮对话，部分提供 GGUF 文件
- 兼容 vLLM / FastChat / Transformers，附 vLLM 部署与 OpenAI API 兼容端点示例
- ActionStudio：统一 agent 轨迹数据格式与训练框架，含统一配置跟踪
- APIGen-MT：多轮函数调用数据生成管线（APIGen-MT-5k 数据集）

## 适用场景

- 为 Agent 系统选用支持函数调用的开源模型
- 用 vLLM 部署 OpenAI API 兼容的 xLAM 推理端点
- 使用 ActionStudio 在统一轨迹数据上训练大动作模型

## 场景标签

`推理引擎` `微调` · 领域:训练与推理

## 证据(README 行号)

> L26: - **[08.2024]**: We are excited to announce the release of full xLAM family, our suite of Large Action Models! From
> L40: This repo introduces xLAM that aggregates agent trajectories from distinct environments, spanning a wide array of s
> L128: # 🧠 ActionStudio: A Lightweight Framework for Agentic Data and Training of Large Action Models

## 星数曲线

```mermaid
xychart-beta
    title "SalesforceAIResearch/xLAM 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26"]
    y-axis "stars" 638 --> 641
    line [639, 640, 640]
```

2026-10-18 639 → 2026-10-26 640（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `8e077c237d27` · [字段定义](../../DATASET.md)*
