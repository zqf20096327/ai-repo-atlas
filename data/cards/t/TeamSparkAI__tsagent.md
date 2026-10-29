# TeamSparkAI/tsagent

⭐ 24 · TypeScript · MIT · 推送 2026-05-24 · [GitHub](https://github.com/TeamSparkAI/tsagent) · [官网](https://www.teamspark.ai/tsagent) · 组织维护

**TypeScript AI agent 平台：构建、编排、部署 agent 全流程工具链**

面向开发者的开源 TypeScript 平台，覆盖 AI agent 的构建、测试、运行与编排：桌面应用 Foundry 提供无代码创建，另有 CLI、A2A 协议服务器、ACP 服务器（供 Zed 等代码编辑器接入）、多个 MCP 服务器及可嵌入应用的 @tsagent/core 库。支持 OpenAI、Anthropic、Google、AWS Bedrock、Ollama 等提供方，通过 MCP 接入工具、A2A 协议串联 agent。密钥支持 1Password 引用与 .env 分级加载。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Foundry 桌面应用 + CLI + npm 包组成的多组件平台
- A2A 协议编排 agent，ACP 服务器接入代码编辑器
- 多个 MCP 服务器：编排、工具导出（Meta MCP）、agent 管理
- 密钥支持 1Password 引用与 .env 分级加载，凭据不明文记录

## 适用场景

- 用无代码桌面应用快速创建和调试 AI agent
- 通过 A2A 协议将多个 agent 串联成工作流
- 把 agent 暴露为 A2A/ACP/MCP 服务供其他系统调用
- 用 TypeScript API 把 agent 嵌入自己的应用

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L8: **TsAgent** is an open-source TypeScript-first platform for building, testing, running, and orchestrating AI agents.
> L27: |**Core API**|`@tsagent/core`|TypeScript Library|TypeScript agent framework for building, testing, and running agen

## 星数曲线

```mermaid
xychart-beta
    title "TeamSparkAI/tsagent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `e77aa5c4b4f2` · [字段定义](../../DATASET.md)*
