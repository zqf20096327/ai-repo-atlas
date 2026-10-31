# 0p9b/TLDR

⭐ 23 · JavaScript · MIT · 推送 2026-08-23 · [GitHub](https://github.com/0p9b/TLDR) · [官网](https://0p9b.github.io/TLDR/) · 个人维护

**让 AI 编程助手输出结论先行的极简回复的系统提示词与安装器**

由一个 2,218 字节的系统提示词 TLDR.md 和多代理安装器组成：提示词仅改变代理的散文风格（默认一句、目标三词），不改动工具、推理与安全行为；install.sh 将提示写入七个标准代理配置路径并安装 /tldr 命令，npx 版 bin/install.js 自动检测已装代理（Claude Code、Cursor、Codex、Gemini 等 30+），按代理安装插件、hooks、skills 与可选 MCP shrink。历史基准显示散文 token 减少 60-75%，但 README 声明当前提示词尚未重测。

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

- 2,218 字节系统提示词，仅改散文风格，不改工具与安全
- install.sh 免 Node 写入 7 个标准代理配置路径
- npx 安装器自动检测并适配 30+ AI 编程代理
- 提供 /tldr 斜杠命令在长会话中重新应用规则

## 适用场景

- 让 AI 编程助手的回答去掉寒暄直接给结论
- 一条命令为多个已装代理统一配置极简输出风格
- 减少长会话中的冗余散文 token 消耗

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L19: Terse, high-signal responses for AI coding agents — less filler, same accuracy on tools, code, and safety.
> L26: |**`bin/install.js`** (via `npx`)|Detects installed agents; plugins, hooks, skills, optional MCP shrink|Claude Code
> L81: Node ≥18. Auto-detects agents, installs the right plugin/extension/skills/hooks per agent.

## 星数曲线

```mermaid
xychart-beta
    title "0p9b/TLDR 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `762415130f71` · [字段定义](../../DATASET.md)*
