# jgmontoya/shaka

⭐ 28 · TypeScript · MIT · 推送 2026-10-20 · [GitHub](https://github.com/jgmontoya/shaka) · 个人维护

**给 AI 编程助手的本地共享上下文/记忆/工作流/安全钩子框架**

面向在真实项目中使用 AI 编程助手（Claude Code、Codex、opencode、Pi）的开发者的本地框架，以 provider 中立方式提供共享上下文注入、markdown 技能与命令、可链式编排的工作流、记忆搜索、MCP 工具暴露和命令安全校验钩子。机制上通过各 provider 的 session/tool 钩子运行：会话开始加载上下文，会话结束写记忆，执行前拦截校验 bash 命令与文件路径。工具定义统一存放，经 MCP server 或原生插件暴露给各 provider。基于 Bun 运行时，从源码安装，需至少装有一个受支持的助手。

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

- 跨 Claude Code/Codex/opencode/Pi 统一注入上下文、工具与安全规则
- 会话钩子机制：加载上下文、写入记忆、执行前安全校验命令
- MCP 工具（含 provider 无关推理与记忆搜索）统一暴露给各助手
- customizations/ 目录覆盖 system/ 默认值且升级不触碰用户文件

## 适用场景

- 让多个 AI 编程助手共享同一套指令、记忆与安全规则
- 切换助手工具时保留项目上下文与工作约定
- 在助手执行 shell 命令前按安全模式拦截危险操作
- 用 markdown 技能与命令模板沉淀团队的可复用工作流

## 场景标签

`Agent 框架` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: Shaka is a local, provider-agnostic framework for shaping how AI coding assistants work. It adds shared context, reu
> L5: It is built for developers who use AI assistants on real projects and want those assistants to remember preferences,

## 星数曲线

```mermaid
xychart-beta
    title "jgmontoya/shaka 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-28 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `78e5af5d439d` · [字段定义](../../DATASET.md)*
