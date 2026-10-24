# photon-hq/rapid-ai-dev

⭐ 149 · TypeScript · MIT · 推送 2026-03-06 · [GitHub](https://github.com/photon-hq/rapid-ai-dev) · [官网](https://photon.codes) · 组织维护

**AI/Agent 原型开发的 TypeScript 可复用构建块工具包**

面向开发者的 TypeScript 工具包，为 AI 与 agent 原型开发提供可复用构建块：终端优先的开发体验，用于迭代提示词、记忆与控制流；以 ESM 入口点暴露可组合模块，每个模块独立导出路径按需引入。目前目录含一个模块 cli-chat——基于 Ink 的终端聊天 UI，提供消息面板、输入栏与控制器 API（onInput 注册监听、sendMessage 流式输出助手消息）。要求 Node.js 18+ 与 TypeScript 工具链（typescript@^5.9.3 peer 依赖），仓库脚本使用 Bun 管理。

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

- 基于 Ink 的终端聊天 UI 模块（cli-chat），含控制器 API
- 模块以 ESM 入口点导出，可组合按需引入
- TypeScript-first API，消息、事件处理器、控制器均有类型定义
- chat.sendMessage 支持流式输出助手消息

## 适用场景

- 快速搭建 agent 原型的终端聊天界面
- 验证新的 agent 架构、记忆系统与工作流
- 在 CLI 中接入自己的 agent 逻辑并流式展示输出

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: Toolkit for rapid AI and agent prototyping. Rapid gives you reusable building blocks so you can validate new agent a
> L30: |Chat TUI|`@photon-ai/rapid/cli-chat`|Ink-powered terminal chat UI with message panel, input bar, and controller AP

## 星数曲线

```mermaid
xychart-beta
    title "photon-hq/rapid-ai-dev 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 148 --> 150
    line [149, 149]
```

2026-10-18 149 → 2026-10-24 149（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `ef7b455dbf78` · [字段定义](../../DATASET.md)*
