# MoaidHathot/Zakira.Imprint

⭐ 23 · C# · MIT · 推送 2026-06-11 · [GitHub](https://github.com/MoaidHathot/Zakira.Imprint) · 个人维护

**通过 NuGet 包分发 AI Skills 与 MCP 配置的 .NET 工具链**

面向 .NET/.NET 库作者的分发方案：将 AI Skills（SKILLS.md 等文件）与 MCP server 配置打包进 NuGet 包，消费方 dotnet build 时由 MSBuild 任务引擎（Zakira.Imprint.Sdk）自动复制到各 AI agent 的原生目录（.github/、.claude/、.cursor/ 等 8 种），并合并 mcp.json；dotnet clean 时按统一 manifest 只删除受管文件，保留用户自配 server。作者可用 ImprintEnabledByDefault 控制 opt-in/opt-out，SDK 在 pack 时自动生成 .targets，无需手写 MSBuild。限制：仅限 NuGet/.NET 生态，SDK 处于 1.0.0-preview 版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | `idea` | |

## 能力要点

- dotnet build/clean 时自动复制与清理 Skills，支持并行多项目构建
- 同时面向 Copilot/Claude/Cursor/Roo/OpenCode/Windsurf/agents/Kiro 8 类 agent
- MCP server 片段自动合并进各 agent 的 mcp.json，clean 时仅删受管条目
- SDK 在 pack 时自动生成 .targets，无需手动 MSBuild 编写

## 适用场景

- 组织通过 NuGet 包统一下发编码规范类 AI Skills
- 库作者随 DLL 一起分发框架使用指南给 AI 助手
- 把团队共享的 MCP server 配置随包安装到各成员的 agent

## 场景标签

 · 领域:.NET 开发工具/AI agent 配置分发

## 证据(README 行号)

> L11: Imprint is a pattern for distributing AI Skills (those `SKILLS.md` files for GitHub Copilot, Claude, Cursor, Roo Co
> L17: 5. **MCP Server Injection**: Packages can inject MCP (Model Context Protocol) server configurations into each agent
> L176: All Imprint skill packages depend on **Zakira.Imprint.Sdk**, which provides the MSBuild task engine. Package autho

## 星数曲线

```mermaid
xychart-beta
    title "MoaidHathot/Zakira.Imprint 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `87fcc599d7ab` · [字段定义](../../DATASET.md)*
