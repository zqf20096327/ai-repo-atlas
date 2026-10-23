# tao-hpu/cognitive-workspace

⭐ 105 · TeX · MIT · 推送 2025-11-08 · [GitHub](https://github.com/tao-hpu/cognitive-workspace) · [官网](https://arxiv.org/abs/2508.13171) · 个人维护 · 中文 README

**认知工作区论文的概念验证代码：验证 LLM 主动记忆管理架构**

支持论文 arXiv:2508.13171 的概念验证实现，用 Python 实验对比认知工作区（分层记忆缓冲、状态持久化、主动信息准备、置信度追踪）与传统 RAG 在多轮对话、多跳推理与信息冲突场景下的记忆复用率与净效率。提供三种运行模式：OpenAI API 完整模式、无需 API key 的规则模拟模式、以及基于 Ollama 等本地模型的本地模式。面向研究人员与开发者复现论文实验结果。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 分层记忆架构：immediate→working→episodic 三级缓冲与提升机制
- 五种实验场景（单轮/多轮/10轮扩展/多跳推理/冲突消解）含统计显著性分析
- 模拟模式无需 API key，结果确定性可复现
- 支持 OpenAI 兼容 API 与 Ollama、llama.cpp 等本地模型

## 适用场景

- 复现论文中认知工作区与 RAG 的对比实验
- 研究 LLM 主动记忆管理与无限上下文架构
- 在本地模型上验证有状态记忆的复用效率

## 场景标签

 · 领域:LLM 记忆架构/研究代码

## 证据(README 行号)

> L227: - Local models (Ollama, llama.cpp)

## 星数曲线

```mermaid
xychart-beta
    title "tao-hpu/cognitive-workspace 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 104 --> 106
    line [105, 105]
```

2026-10-18 105 → 2026-10-23 105（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `9398608cc8d5` · [字段定义](../../DATASET.md)*
