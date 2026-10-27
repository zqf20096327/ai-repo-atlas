# MonadWorks/agentify

⭐ 42 · TypeScript · MIT · 推送 2026-03-16 · [GitHub](https://github.com/MonadWorks/agentify) · 组织维护

**把 OpenAPI 规范编译为 9 种 AI agent 接口格式的 CLI 工具**

面向 API 开发者的 agent 接口编译器：读取 OpenAPI/Swagger 规范（URL 或文件），解析为中间表示 AgentifyIR，经可插拔 emitter 生成最多 9 种输出——MCP Server（含 Dockerfile）、CLAUDE.md、AGENTS.md、.cursorrules、Skills、llms.txt、GEMINI.md、A2A Card 及可发起真实 API 调用的 CLI。生成物经安全扫描（输入净化、提示注入检测）。README 自述处于早期阶段，在 Notion、Stripe、GitHub 等 API 上测试通过。以 npm 包形式提供，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单一 OpenAPI 规范生成 9 种 agent 接口格式
- AgentifyIR 中间表示 + 可插拔 emitter 架构
- 生成物内置安全扫描（输入净化、提示注入模式检测、代码扫描）
- 在 13 至 1093 端点的真实 API 上测试通过

## 适用场景

- 让 Claude、Cursor、Copilot 等 agent 直接调用我的 API
- 一条命令生成并保持 MCP Server 与各类 agent 说明文件同步
- 为大型 API 平台批量生成 agent 工具接口

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L15: Agentify reads your OpenAPI spec and writes them all.
> L81: Agentify parses your spec into an intermediate representation (**AgentifyIR**), then runs pluggable emitters to pro

## 星数曲线

```mermaid
xychart-beta
    title "MonadWorks/agentify 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-27 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `bd9657b8d08d` · [字段定义](../../DATASET.md)*
