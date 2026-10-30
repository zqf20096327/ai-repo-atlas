# shadowrootdev/awesome-agent-skills-mcp

⭐ 27 · TypeScript · MIT · 推送 2026-04-13 · [GitHub](https://github.com/shadowrootdev/awesome-agent-skills-mcp) · [官网](https://www.npmjs.com/package/awesome-agent-skills-mcp) · 个人维护

**MCP server：向 AI 助手分发 100+ 策展 agent 技能**

一个 Model Context Protocol 服务器，从 VoltAgent awesome-agent-skills 仓库自动拉取并提供 100+ 由 Anthropic、Vercel、Trail of Bits、Hugging Face 等组织贡献的 AI agent 技能，通过 list_skills/get_skill/invoke_skill/refresh_skills 四个 MCP 工具暴露给 Claude、GitHub Copilot、OpenCode 等 MCP 客户端。支持 JSON 缓存、可配置同步间隔与环境变量，基于 TypeScript/Zod 构建。面向使用 MCP 客户端的开发者，需 Node.js >= 20，可 npx 直接运行。

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

- 提供 100+ 来自多个组织的策展技能，覆盖文档处理、安全审计、ML 工作流等
- 四个 MCP 工具：list_skills / get_skill / invoke_skill / refresh_skills
- 兼容 MCP 2024-11-05 规范，支持 Claude、GitHub Copilot、OpenCode 等客户端
- 从 VoltAgent 仓库自动同步（默认 60 分钟间隔）并以 JSON 缓存加速启动

## 适用场景

- 在 Claude 或 GitHub Copilot 中调用现成技能（如代码审查、React 最佳实践）
- 为 MCP 客户端批量接入文档处理、安全分析等专家技能
- 浏览和检索可用 agent 技能目录并按需调用

## 场景标签

`精选清单` · 领域:学习与行业

## 证据(README 行号)

> L14: > **A Model Context Protocol (MCP) server that provides access to 100+ curated AI agent skills from the VoltAgent A
> L33: - **Multi-Client Support** - Works with Claude, GitHub Copilot, OpenCode, and any MCP-compatible client
> L196: The server exposes four MCP tools:

## 星数曲线

```mermaid
xychart-beta
    title "shadowrootdev/awesome-agent-skills-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-30"]
    y-axis "stars" 25 --> 28
    line [26, 27, 27]
```

2026-10-18 26 → 2026-10-30 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `3aa1f9b0ccd4` · [字段定义](../../DATASET.md)*
