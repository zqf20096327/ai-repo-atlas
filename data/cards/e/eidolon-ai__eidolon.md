# eidolon-ai/eidolon

⭐ 493 · Python · Apache-2.0 · 推送 2026-05-20 · [GitHub](https://github.com/eidolon-ai/eidolon) · [官网](https://www.eidolonai.com/) · 组织维护

**构建与部署 Agent 服务的开源 SDK**

面向开发者的 Agent 服务 SDK：将 agent 实现为内置 HTTP 服务，部署时无需额外工作；agent 之间通过由各服务 openapi json schema 动态生成的工具进行通信。组件（llm、rag 实现、工具等）模块化可替换，支持使用现成组件或自定义，README 称此举避免厂商锁定。README 本身较简短，详细内容指向官网与 Quickstart 指南；以 PyPI 包分发，由多名贡献者参与维护。

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

- agent 即服务，内置 HTTP 服务器，无需额外部署工作
- agent 间通过 openapi schema 动态生成的工具通信
- llm/rag/工具等组件模块化可替换

## 适用场景

- 以服务形式构建与部署 agent 应用
- 让多个 agent 通过定义良好的接口互相调用
- 替换 LLM 或 RAG 组件以适应不同后端

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L8: Eidolon helps developers **_build_** and **_deploy_** agent-based services.
> L19: With a focus on modularity, Eidolon makes it easy to swap out components. Grab an off the shelf llm, rag impl, tool

## 星数曲线

```mermaid
xychart-beta
    title "eidolon-ai/eidolon 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 492 --> 494
    line [493, 493]
```

2026-10-18 493 → 2026-10-25 493（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `d38d4ca208fb` · [字段定义](../../DATASET.md)*
