# freu-ai/freu-cli

⭐ 31 · Python · AGPL-3.0 · 推送 2026-05-17 · [GitHub](https://github.com/freu-ai/freu-cli) · [官网](https://www.freu.ai/) · 组织维护

**把浏览器操作录制编译成可复用技能命令的 CLI，降低 agent token 开销**

面向 AI agent 开发者的浏览器自动化工具：用户在浏览器中正常操作一次，Chrome 扩展捕获事件，freu-cli learn 调用 LLM（经 LiteLLM 路由，默认 gpt-5.1，支持 OpenAI/Anthropic/Google/xAI/MiniMax）将原始事件编译为语义 DSL 的 SKILL.md 与 JSON 命令；运行时 agent 直接执行预编译命令，跳过 DOM 视觉推理。采用星座式（constellation）DOM 定位，捕获元素及祖先、邻居、语义锚点，页面 CSS 类名或布局变化后技能仍可用。支持按 SKILL.md 约定目录接入 Claude Code、Codex CLI、Cursor、OpenClaw、Hermes 等 agent。限制：依赖 Chrome 扩展与 LLM API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 浏览器会话一次性录制，编译为语义 DSL 技能命令（SKILL.md + JSON）
- 星座式 DOM 定位：元素+祖先+邻居+语义锚点，类名重命名/页面重排后技能保持可用
- LLM 经 LiteLLM 路由，支持 OpenAI/Anthropic/Google/xAI/MiniMax 等多提供商
- 技能可放入 Claude Code、Codex CLI、Cursor、OpenClaw、Hermes 的 skills 目录直接调用

## 适用场景

- 把重复的网页操作（如给 GitHub 仓库点星）固化成 agent 可复用命令
- 降低 agent 反复解析 DOM 的 token 与推理开销
- 让 agent 从网页提取数据（如价格）作为命令输出

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L10: Instead of forcing your agent to act as a Just-In-Time (JIT) interpreter that parses the DOM on every single run, F
> L182: Once you've learned a skill, drop it into your agent's skills directory

## 星数曲线

```mermaid
xychart-beta
    title "freu-ai/freu-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-28 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `3f6d0412d119` · [字段定义](../../DATASET.md)*
