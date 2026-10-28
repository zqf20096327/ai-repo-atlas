# corespeed-io/zypher-agent

⭐ 331 · TypeScript · Apache-2.0 · 推送 2026-07-30 · [GitHub](https://github.com/corespeed-io/zypher-agent) · [官网](https://zypher.corespeed.io) · 组织维护

**面向开发者的 Deno/TypeScript AI agent 构建框架**

用 Deno/TypeScript 编写的 AI agent 框架，以响应式循环让 LLM 动态决定下一步操作，而非固定工作流。提供基于 Git 的检查点管理、可扩展工具系统（文件操作/搜索/终端命令）、原生 MCP 服务器支持（含 OAuth 认证）、多模型统一接口（Anthropic Claude 与 OpenAI GPT）及后置推理拦截器。声称生产可用：可配置超时、并发保护与错误处理。通过 JSR 安装，npm 支持尚未提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 响应式 agent 循环，LLM 动态决定执行步骤
- Git 检查点：追踪、审查与回滚 agent 变更
- 原生 MCP 服务器支持（含 OAuth 认证）
- 多模型统一接口（Anthropic Claude / OpenAI GPT）

## 适用场景

- 在应用中嵌入可自主决策的 AI agent
- 为 agent 构建文件操作、搜索与终端工具集
- 通过 MCP 接入外部工具服务器

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L10: - **Agent, Not Workflow**: Reactive loop where the agent dynamically decides
> L18: - **Multi-Provider Support**: Works with Anthropic Claude and OpenAI GPT models

## 星数曲线

```mermaid
xychart-beta
    title "corespeed-io/zypher-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 330 --> 332
    line [331, 331]
```

2026-10-18 331 → 2026-10-28 331（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `af151439ee68` · [字段定义](../../DATASET.md)*
