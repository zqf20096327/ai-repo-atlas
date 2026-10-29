# arvindand/agent-skills

⭐ 17 · Python · MIT · 推送 2026-10-04 · [GitHub](https://github.com/arvindand/agent-skills) · [官网](https://arvindand.hashnode.dev/why-i-reach-for-skills-before-mcp) · 个人维护

**面向 AI 编程助手的可移植技能包：文档查询、GitHub 操作等**

为 Claude Code、GitHub Copilot、OpenCode、Cursor 等 AI 编程助手提供的技能（SKILL.md）集合，含 5 个技能：context7 库文档查询、github-navigator 的 gh CLI 操作、maven-tools 的 JVM 依赖情报（经 MCP server）、skill-crafting 技能创建与校验、ui-ux-design 界面设计。技能按渐进增强设计：规范字段跨平台可用，Claude Code 专属扩展（context forking、hooks）仅在 Claude Code 中生效。安装方式为 Claude Code 插件市场或复制到技能目录。

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

- 5 个技能：文档查询、GitHub 操作、JVM 依赖情报、技能创建、UI/UX 设计
- 渐进增强设计：规范字段跨平台，Claude Code 扩展按需生效
- 技能按提示自动激活，无需手动调用
- 含 Skills 与 MCP 取舍的设计说明及混合模式示例

## 适用场景

- 让 AI 编程助手在编码时获取最新库文档
- 通过对话执行 GitHub 操作与代码库分析
- JVM 项目的版本升级规划与 CVE 扫描
- 创建和校验自己的 agent 技能

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: Portable skills for AI coding assistants. Primarily tested with Claude Code and leverages Claude Code-specific featu
> L31: Works with Claude Code, GitHub Copilot, OpenCode, Cursor, and VS Code with Copilot.

## 星数曲线

```mermaid
xychart-beta
    title "arvindand/agent-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-29 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `0333c40ed6fd` · [字段定义](../../DATASET.md)*
