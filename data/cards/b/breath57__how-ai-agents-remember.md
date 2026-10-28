# breath57/how-ai-agents-remember

⭐ 45 · 推送 2026-06-17 · [GitHub](https://github.com/breath57/how-ai-agents-remember) · 个人维护 · 中文 README

**5 个开源 AI Agent 记忆系统的源码级逆向分析文集**

对 OpenClaw、Hermes Agent、nanobot、NullClaw、OpenFang 五个开源 Agent 项目的记忆系统做源码级分析，每个项目 7-10 篇文档，覆盖架构总览、数据模型、存储与检索、生命周期管理和在自有技术栈中重建的复刻指南。提供横向对比表（语言、存储方式、向量搜索、知识图谱、记忆衰减等维度）、复杂度光谱图与阅读路线，并提炼 6 条通用设计规律。架构图用 Mermaid 绘制，MIT 许可，接受 PR 补充新项目分析。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 个项目、4 种语言（TypeScript/Python/Zig/Rust）的记忆系统逐行分析
- 每项目含架构图、数据模型、检索管线与复刻指南
- 横向对比表覆盖存储/向量搜索/知识图谱/记忆衰减/LLM 整合等维度
- 提炼 6 条通用规律（双时钟、检索难于存储、优雅降级等）

## 适用场景

- 为自研 Agent 选型并设计记忆系统架构
- 学习不同复杂度层级（2 个 Markdown 到 9 阶段检索管线）的记忆实现
- 按复刻指南在 LangGraph/Python 中重建记忆系统

## 场景标签

`Agent 记忆` `教程课程` · 领域:Agent 开发

## 证据(README 行号)

> L3:  逆向工程 5 个火爆的、基于 AI Agent 的开源 Bot 项目，源码级拆解记忆系统的每一个细节。
> L16: 本文档深度分析了以下 5 个基于 AI Agent 的开源 Bot 项目的记忆系统实现：
> L48: > 这不是又一份"AI Agent 综述"。分析这 5 个项目的每一行记忆相关代码，画出了每一条数据流，记录了每一个设计取舍。

## 星数曲线

```mermaid
xychart-beta
    title "breath57/how-ai-agents-remember 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-28 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `fe7fbae87055` · [字段定义](../../DATASET.md)*
