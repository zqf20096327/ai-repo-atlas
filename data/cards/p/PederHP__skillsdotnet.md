# PederHP/skillsdotnet

⭐ 15 · C# · 推送 2026-05-09 · [GitHub](https://github.com/PederHP/skillsdotnet) · 个人维护

**面向 C# MCP SDK 的 Agent Skills 实现库**

为 C# MCP SDK 实现 agentskills.io 规范的库：将 SKILL.md 目录形式的技能通过 skill:// URI 约定发布为 MCP 资源，实现渐进式披露（frontmatter 摘要、按需加载全文与支撑文件）。服务端可注册技能目录或 ~/.claude/skills 等 vendor 快捷方式；客户端提供技能发现、清单读取、下载与同步。SkillCatalog 与 Microsoft.Extensions.AI 集成，向模型提供 load_skill/unload_skill 工具及技能依赖按需连接回调。API 声明为实验性、可能变动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- skill:// URI 约定将 SKILL.md 技能发布为 MCP 资源，支持渐进式披露
- SkillCatalog 提供 load_skill/unload_skill 工具与 IChatClient 集成
- 技能可在 frontmatter 声明 MCP 服务器依赖并按需连接
- 提供 Claude skills 目录等 vendor 注册快捷方式

## 适用场景

- 在 C# MCP 服务器上发布与分发 Agent 技能
- 在 MCP 客户端中发现、下载与同步技能目录
- 为聊天模型按需加载/卸载技能以控制上下文占用

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L6: Agent skills (agentskills.io) for the C# MCP SDK.
> L10: Skills provide "context-as-progressive-disclosure" via `SKILL.md` files. This library uses a `skill://` URI convent

## 星数曲线

```mermaid
xychart-beta
    title "PederHP/skillsdotnet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `d24a691a777b` · [字段定义](../../DATASET.md)*
