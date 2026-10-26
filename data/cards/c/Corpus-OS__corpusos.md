# Corpus-OS/corpusos

⭐ 205 · Python · Apache-2.0 · 推送 2026-05-08 · [GitHub](https://github.com/Corpus-OS/corpusos) · [官网](https://corpusos.com) · 组织维护

**标准化 LLM/向量/图/嵌入基础设施的开源协议套件与 SDK**

Corpus OS 是一套厂商中立的协议套件与参考 SDK，覆盖 LLM、Embedding、Vector、Graph 四个基础设施领域，目标是让应用框架（LangChain/LlamaIndex/AutoGen/CrewAI/Semantic Kernel/MCP）通过统一协议访问任意后端。机制包括：规范 JSON wire envelope、统一错误分类（带重试提示）、SIEM 安全指标、deadline 传播、thin/standalone 两种模式、3,330+ 一致性测试与 CLI 验证命令。Apache-2.0 开源，另含商业的 CORPUS Router 与官方生产适配器（可选）。仅 async，Python ≥3.10。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四领域（LLM/Embedding/Vector/Graph）统一协议与 wire envelope
- 统一错误分类与机器可操作的重试提示（retry_after_ms 等）
- thin/standalone 双模式：自带断路器/限流/缓存或接入外部控制面
- CLI 一致性验证（corpus-sdk verify）与认证流程

## 适用场景

- 多后端 LLM/向量库/图数据库集成时统一错误与观测
- 平台团队用一套协议、错误分类和指标覆盖全部 AI 流量
- 后端厂商实现一次适配并通过一致性测试对接各框架

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L14: Reference implementation of the **Corpus OS** — a **wire-first, vendor-neutral** SDK for interoperable AI framework
> L53: Corpus OS is **not** a replacement for LangChain, LlamaIndex, Semantic Kernel, CrewAI, AutoGen, or MCP. Use those f
> L68: - **App developers** — Keep using your framework of choice. Talk to all backends through Corpus OS protocols. Swap 

## 星数曲线

```mermaid
xychart-beta
    title "Corpus-OS/corpusos 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 204 --> 206
    line [205, 205]
```

2026-10-18 205 → 2026-10-26 205（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `0e7699ad69dd` · [字段定义](../../DATASET.md)*
