# TeleAI-UAGI/telemem

⭐ 494 · Python · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/TeleAI-UAGI/telemem) · [官网](https://teleai-uagi.github.io/telemem/) · 组织维护 · 中文 README

**给 Agent 开发者的长期/多模态记忆管理层，可替换 Mem0**

TeleMem 是面向 Agent 的记忆管理基础设施：通过角色感知摘要、LLM 语义聚类去重、FAISS+JSON 双写存储与异步批量写入，为多轮对话、角色扮演和长期信息存储提供记忆提取与语义检索；可作为 Mem0 的 drop-in 替换（import telemem as mem0），兼容其 add()/search() API。另提供视频→帧→描述→向量库的多模态记忆流水线与 ReAct 式视频问答。支持 MCP server（8 个工具），可配置 Ollama/DeepSeek/Moonshot/MiniMax 等多种 OpenAI 兼容后端，默认支持本地 Qwen+FAISS 全离线运行。由 TeleAI-UAGI 组织维护，Apache 2.0 许可，有 arXiv 技术报告。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一行代码 drop-in 替换 Mem0，兼容 add()/search() API
- 按角色自动构建隔离的独立记忆档案（多角色分离）
- 视频→帧提取→描述生成→向量库的自动化多模态记忆流水线与 ReAct 式视频问答
- MCP server 支持（8 个工具，官方 MCP registry 可 uvx telemem 零安装运行）

## 适用场景

- 让多角色虚拟 Agent / 陪伴 AI 在长期交互中保持一致的角色设定
- 为客服、创意副驾等长记忆 AI 助手提供记忆提取与检索
- 对长视频内容做存储、问答与多步推理
- 用本地 Ollama 或 Qwen+FAISS 搭建无云端依赖的记忆系统

## 场景标签

`Agent 记忆` `多模态` · 领域:Agent 开发

## 证据(README 行号)

> L36: TeleMem is an agent memory management layer that can be used as <mark>**a high-performance drop-in replacement for 
> L50: - 🏠 **Fully local by default** — runs end-to-end on your hardware (Qwen + FAISS); no cloud service, no paid tier, n

## 星数曲线

```mermaid
xychart-beta
    title "TeleAI-UAGI/telemem 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 493 --> 495
    line [494, 494]
```

2026-10-18 494 → 2026-10-27 494（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `dbcb70f83e8d` · [字段定义](../../DATASET.md)*
