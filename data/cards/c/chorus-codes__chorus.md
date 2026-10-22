# chorus-codes/chorus

⭐ 534 · TypeScript · Apache-2.0 · 推送 2026-08-13 · [GitHub](https://github.com/chorus-codes/chorus) · [官网](https://chorus.codes) · 组织维护

**多 LLM 交叉评审工具：多厂商 AI 并行审查代码后才放行**

本地运行的 Node.js 工具，协调 2-4 个不同厂商的 AI CLI（Claude Code、Codex、Gemini CLI 等）并行评审同一代码变更或架构决策，只在评审者达成一致时给出放行判定；也可通过 OpenRouter API key 按量付费。以 MCP server 形式注册进各 AI CLI/IDE，暴露 9 个工具，内置 code-review、red-green 等 YAML 模板与多种评审 persona，提供三档权限沙箱（Strict/Workspace/Full）。代码不经新厂商，评审消耗已有订阅额度。要求 Node 20+ 且至少一个受支持的 AI CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多厂商 AI 并行评审，一致才放行、分歧则重试
- 通过既有 AI 订阅驱动 CLI，评审不额外按 token 付费
- 以 MCP server 注册进 Claude Code/Codex/Cursor 等，暴露 9 个工具
- YAML 自定义评审模板与 10+ 种评审 persona，三档权限沙箱

## 适用场景

- 合并前让多个不同厂商的 AI 交叉审查 diff
- TDD 中让写测试与写代码的 AI 互相不可见
- 对大型架构决策收集多个模型的不同视角

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L7: 2–3 *different* AI tools review the same change in parallel, only green-lighting when they agree. Runs on your exist
> L91: `chorus init` registers Chorus as an MCP server with every CLI / IDE it detects (Claude Code, Codex, Gemini CLI, Cu
> L261: **The unique thing:** your code never goes to a new vendor. Chorus just orchestrates the AI tools you already use.

## 星数曲线

```mermaid
xychart-beta
    title "chorus-codes/chorus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-21"]
    y-axis "stars" 533 --> 535
    line [534, 534]
```

2026-10-18 534 → 2026-10-21 534（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `d02485d16f0a` · [字段定义](../../DATASET.md)*
