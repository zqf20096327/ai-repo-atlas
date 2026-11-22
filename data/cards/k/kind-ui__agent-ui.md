# kind-ui/agent-ui

⭐ 3 · TypeScript · MIT · 推送 2026-11-21 · [GitHub](https://github.com/kind-ui/agent-ui) · [官网](https://kindui.dev/docs/agent-ui/) · 组织维护

**面向 React/Web Components 的 agent 界面组件库**

提供 56 个用于 AI 聊天与 agent 界面的 UI 组件，覆盖对话流式 markdown、agent 步骤展示、人工确认输入、开发者输出（终端/文件树/测试结果）与会话外壳等。每个组件同时提供 React 版与 Web Components 版。通过 UI SDK 的 createAgent 使 agent 可读取页面组件并执行操作，重要操作需人工确认。组件经 shadcn CLI 复制到用户项目，基于 Tailwind CSS v4 与 --kind-* 主题令牌，附带 AI SDK UIMessage 适配器。需 Tailwind v4，React 组件需 React 19。

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

- 56 个组件，React 与 Web Components 双版本同 props/样式
- UI SDK createAgent 使 agent 可读取组件并执行操作，敏感操作需人工确认
- 流式 markdown 仅解析变更块
- 提供 AI SDK UIMessage 适配器

## 适用场景

- 为 LLM 聊天应用搭建流式对话界面
- 展示 agent 的推理步骤、工具调用与执行计划
- 在 agent 界面中实现人工审批与问题表单交互
- 用 shadcn CLI 将组件复制进自己的项目定制主题

## 场景标签

`聊天机器人` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: AI interface components that people and agents can both use, for React and Web Components, built on UI SDK.
> L18: - **56 components** for AI chat and agent interfaces: conversations and streaming markdown, the steps an agent take
> L21: - **Agent-operable.** An agent connected with UI SDK's `createAgent` reads the same components a person sees and ru


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `f283199d23c2` · [字段定义](../../DATASET.md)*
