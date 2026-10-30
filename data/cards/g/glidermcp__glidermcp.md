# glidermcp/glidermcp

⭐ 18 · MIT · 推送 2026-10-29 · [GitHub](https://github.com/glidermcp/glidermcp) · [官网](https://glidermcp.com) · 组织维护

**面向编码 agent 的本地 C#/.NET 代码分析 MCP 工具集**

GliderMCP 是一组通过 MCP 协议接入编码 agent 的本地代码工具：Glider 提供 C#/.NET 导航、诊断、编辑与重构，TGlider/Scout/JGlider 分别覆盖 TypeScript/JavaScript、仓库搜索与只读 Java 分析，另有知识共享的 Keep 与运行时取证的 GliderTrace。本仓库提供 Claude Code 与 Codex 的插件、技能与配置模板，产品服务器实现不在其中。Glider 系列要求 .NET 10 SDK，TGlider/JGlider 要求 Node.js 24+，JGlider 另需 JDK 21+；非商业用途免费，商业用途当前免费。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 个产品分别覆盖 C#/.NET、TypeScript/JavaScript、仓库搜索、Java、知识共享与运行时取证
- 提供 Claude Code 与 Codex 的插件（插件捆绑技能与 MCP 连接）
- 服务器本地处理代码，返回内容由 MCP 客户端控制
- 支持仅为已有手动连接安装技能、保留原配置

## 适用场景

- 让 Claude Code 或 Codex 等编码 agent 直接导航和重构 C#/.NET 代码
- 在本地对 TypeScript/JavaScript 项目做代码分析
- 通过仓库级搜索和运行时证据辅助 agent 理解工程

## 场景标签

 · 领域:开发工具/MCP 服务器

## 证据(README 行号)

> L3: Local tools for coding agents. Start with **Glider** to navigate, analyze, edit, and refactor C#/.NET code through M
> L22: This repository provides plugins for Claude Code and Codex:

## 星数曲线

```mermaid
xychart-beta
    title "glidermcp/glidermcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `35cad48b7f99` · [字段定义](../../DATASET.md)*
