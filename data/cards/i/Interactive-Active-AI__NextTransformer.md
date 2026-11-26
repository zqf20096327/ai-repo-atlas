# Interactive-Active-AI/NextTransformer

⭐ 498 · Python · MIT · 推送 2026-11-24 · [GitHub](https://github.com/Interactive-Active-AI/NextTransformer) · [官网](https://interactive-active-ai.github.io/NextTransformer/) · 组织维护 · 中文 README

**下一代 Transformer/LLM 的公平基准框架与自动架构研究平台**

在固定训练预算下训练并比较多种语言模型架构（recurrent depth、稀疏/线性注意力、残差变体、混合结构与 MoE），所有模型使用相同数据、相同 tokens 数、相同理论 FLOPs 并在相同检查点评测；结果为可审计的文件化记录。提供统一训练器、数据管线、观测站（学习曲线/排行榜/模型卡）、MoE 赛道，以及支持 MCP 工具与计量算力的 agent 研究竞技场（Arena v2）。面向做架构研究的科研人员与 agent 开发者。运行环境要求 Linux、NVIDIA GPU 与 uv，数据集约 600 GB。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一协议的 compute-matched 基准：训练 FLOPs 偏差 ±1% 并全程审计
- 多架构家族插件式接入：GQA、NSA、MoBA、GDN、KDA、Ouro、AttnRes 等
- Agent-native Arena：任意 LLM 可在相同协议下提交自主发现的架构
- 观测站提供学习曲线、排行榜、模型图集与训练回放

## 适用场景

- 在固定算力预算下对比不同注意力/深度架构的语言模型表现
- 让 AI agent 在统一规则下自主研究并提交新架构
- 查阅已审计的 46 次运行结果与 Hugging Face 模型权重

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L3:  The comprehensive, cutting-edge open-source framework, benchmark and auto-research platform for next-generation Tra
> L22: **When the training budget is fixed, how should a language model spend its computation?** NextTransformer trains
> L44: Agent-native research: hand the arena task to your agent; the full version, Arena v2, has been live since November 
> L63: **1. Install** (Linux, NVIDIA GPUs, uv):

## 星数曲线

```mermaid
xychart-beta
    title "Interactive-Active-AI/NextTransformer 星数(近 18 点)"
    x-axis ["2026-11-01", "2026-11-02", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 0 --> 546
    line [16, 87, 393, 402, 404, 408, 411, 412, 421, 457, 476, 481, 483, 487, 489, 492, 493, 498]
```

2026-11-01 16 → 2026-11-26 498（+482）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `a52b98625c45` · [字段定义](../../DATASET.md)*
