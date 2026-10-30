# onfire7777/universal-ai-skills-library

⭐ 16 · Python · MIT · 推送 2026-09-11 · [GitHub](https://github.com/onfire7777/universal-ai-skills-library) · [官网](https://github.com/onfire7777/universal-ai-skills-library/wiki) · 个人维护

**为多款 AI 客户端提供共享技能库与按需路由加载的技能系统**

由 1,812 个技能目录、Go 编写的 skill-router CLI 和单一来源的注册表生成器组成的三层体系：各 AI 客户端（Codex、Claude、Cursor、OpenCode 等）通过紧凑适配器接入，对用户提示做确定性预检路由，按需仅加载一个匹配技能，避免向每个客户端复制完整语料。可选的 Universal AI Stack（Windows）提供本地 OpenAI 兼容路由、Kimi/OpenRouter 回退、经 llama.cpp 运行的 Qwen3-Coder 本地回退与共享记忆。MIT 许可，含安装脚本、校验与发布审计。

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

- 1,812 个技能共享语料 + skill-router Go CLI 按需加载
- 确定性预检路由，不调用额外 LLM API
- 为 14+ 客户端提供 skill-root / repo-instruction / hosted 三类适配器
- 可选 Universal AI Stack：本地模型路由、回退与共享记忆

## 适用场景

- 让多个 AI 编码客户端共享同一技能库而无需重复复制
- 通过用户提示钩子自动选择并加载匹配技能
- 搭建带本地模型回退与共享记忆的本地 AI 栈

## 场景标签

`Agent 框架` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L12: Universal AI Skills Library is a router-first skill system for local and CLI AI
> L21: instructions or a tiny wrapper that calls `skill-router` only when a real user
> L62: 1. **Router** — `skill-router-cli/` (Go). Scores prompts, runs deterministic
> L43: - compact adapters for Codex, Claude, Cursor, Gemini, OpenCode, Hermes Agent,

## 星数曲线

```mermaid
xychart-beta
    title "onfire7777/universal-ai-skills-library 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b47818ac215a` · [字段定义](../../DATASET.md)*
