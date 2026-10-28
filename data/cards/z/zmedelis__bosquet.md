# zmedelis/bosquet

⭐ 381 · Clojure · EPL-1.0 · 推送 2026-09-30 · [GitHub](https://github.com/zmedelis/bosquet) · [官网](https://zmedelis.github.io/bosquet/) · 个人维护

**Clojure 的 LLM 应用构建工具库：提示模板、Agent 与记忆管理**

面向 Clojure 开发者的 LLM 应用构建库，提供 LLM 与工具服务管理、基于 Selmer 的提示模板、基于 Pathom 图处理机的提示链式组合、Agent 与外部 API 交互抽象、LLM 记忆处理及调用响应缓存等能力。通过 Clojure CLI 运行，密钥存于 secrets.edn、配置存于 config.edn；支持 openai 与 ollama 模型的对话工具调用。文档标注为 WIP。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | EPL-1.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 基于 Selmer 的提示模板与基于 Pathom 的提示链式组合
- Agent 与工具定义抽象，对接外部 API
- LLM 记忆处理与调用响应缓存
- 提供 CLI 生成命令与 API key 管理

## 适用场景

- 用 Clojure 构建 LLM 应用时管理提示模板与链式生成
- 为 AI 应用接入工具调用与外部 API
- 在上下文窗口受限场景下做 LLM 记忆管理

## 场景标签

`提示工程` `Agent 记忆` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7: Bosquet provides instruments to work with those AI application concepts:
> L11: - Prompt chaining and composition via a powerful Pathom graph processing machine

## 星数曲线

```mermaid
xychart-beta
    title "zmedelis/bosquet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 380 --> 382
    line [381, 381]
```

2026-10-18 381 → 2026-10-28 381（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `09cf4ee1c151` · [字段定义](../../DATASET.md)*
