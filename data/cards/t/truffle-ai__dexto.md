# truffle-ai/dexto

⭐ 661 · TypeScript · NOASSERTION · 推送 2026-11-19 · [GitHub](https://github.com/truffle-ai/dexto) · [官网](https://dexto.ai) · 组织维护

**开发者用 YAML 编排 LLM agent 的 harness 与 CLI/SDK 工具包**

Dexto 定位为 agent harness/编排层，以 YAML 配置定义 agent（模型、MCP 服务器、存储、权限），提供会话持久化、记忆、子 agent 派生、human-in-the-loop 审批与 REST/SSE API。内置一个可直接使用的 coding agent，支持 CLI、headless、Discord/Telegram 等运行方式，并可嵌入 Discord/Telegram。通过 @dexto/core SDK 以 TypeScript 编程方式构建 agent。运行需 Node.js 20+ 与已配置的模型 API key 或云端账户/额度；许可证为 Elastic License 2.0，默认收集匿名遥测，可通过环境变量关闭。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YAML 配置定义 agent，模型/工具切换无需改代码
- 接入 Model Context Protocol，内置 MCP 管理器（30+ 工具）
- 持久会话/记忆、子 agent 派生、分级权限审批
- 提供 CLI、headless 模式与 @dexto/core SDK 及 REST/SSE API

## 适用场景

- 在终端运行编码 agent 进行代码构建与重构
- 用自己的 YAML 配置搭建领域 agent 并嵌入应用
- 通过 MCP 连接浏览器、文件系统、API 等工具
- 本地运行模型以保留数据在本机

## 场景标签

`编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L47: Dexto is an **agent harness**—the orchestration layer that turns LLMs into reliable, stateful agents that can take 
> L60: - **Configuration-driven**: Define agents in YAML. Swap models and tools without touching code.

## 星数曲线

```mermaid
xychart-beta
    title "truffle-ai/dexto 星数(近 7 点)"
    x-axis ["2026-10-22", "2026-10-30", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-24"]
    y-axis "stars" 656 --> 662
    line [657, 659, 657, 659, 660, 661, 661]
```

2026-10-22 657 → 2026-11-24 661（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `c62d659784ad` · [字段定义](../../DATASET.md)*
