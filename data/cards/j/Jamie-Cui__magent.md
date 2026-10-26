# Jamie-Cui/magent

⭐ 43 · Emacs Lisp · GPL-3.0 · 推送 2026-09-22 · [GitHub](https://github.com/Jamie-Cui/magent) · [官网](https://jamie-cui.github.io/magent/) · 个人维护

**Emacs Lisp 编写的多智能体 AI 编程助手**

用 Emacs Lisp 实现的 AI 编程 agent，具备多智能体架构：支持子 agent 的 spawn、message、wait、resume、close 生命周期；提供基于权限的工具访问控制与 Elisp 原生的斜杠命令扩展 API（magent-action）。LLM 通信全部委托给 gptel，可使用 gptel 注册的所有后端与模型（Anthropic、OpenAI、Ollama 等）。唯一支持的前端是 agent-shell，经 MELPA 或 Git 安装，要求 Emacs 29.1+ 及 gptel、acp、agent-shell 等依赖，grep 工具需要 ripgrep 或 Git。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 子 agent 生命周期（spawn/message/wait/resume/close）协作架构
- 基于权限的工具访问控制
- magent-action 注册 Elisp 原生斜杠命令，与数据型 SKILL.md 技能互补
- LLM 接入全部委托 gptel，会话内可切换不同后端模型

## 适用场景

- 在 Emacs 内通过 agent-shell 与 AI agent 协作完成项目编码
- 通过 TRAMP 在远程项目上运行 agent 而控制平面留在本地
- 注册自定义 Elisp 斜杠命令扩展 agent 能力

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L9: An Emacs Lisp AI coding agent with multi-agent architecture, permission-based
> L172: Magent delegates all LLM communication to [[https://github.com/karthink/gptel][gptel]]. Configure your provider, m
> L190: The only supported Magent frontend is agent-shell. Magent supplies its own

## 星数曲线

```mermaid
xychart-beta
    title "Jamie-Cui/magent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-26 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9a0ab402a09b` · [字段定义](../../DATASET.md)*
