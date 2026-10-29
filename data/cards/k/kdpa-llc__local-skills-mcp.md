# kdpa-llc/local-skills-mcp

⭐ 40 · TypeScript · MIT · 推送 2026-10-04 · [GitHub](https://github.com/kdpa-llc/local-skills-mcp) · 组织维护

**让任意 MCP 客户端加载本地 SKILL.md 技能的 MCP 服务器**

一个通用 MCP 服务器，使任意 MCP 兼容客户端（Claude Code/Desktop、Cline、Continue.dev、自定义 agent）按需读取本地文件系统中的专家技能。技能为带 YAML frontmatter 的 SKILL.md 文件；初始仅加载名称与描述（约 50 tokens/技能），调用 get_skill 时加载全文，支持热重载与多目录聚合（内置、~/.claude/skills、./skills、$SKILLS_DIR）。提供三个工具：get_skill、validate_skill、evaluate_skill。要求 Node.js 22+，可离线运行。

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

- 懒加载技能：初始仅载入名称/描述（约 50 tokens/技能），全文按需获取
- 多目录自动聚合与优先级覆盖（内置 → 全局 → 项目 → 自定义路径）
- 热重载：技能新增/编辑/删除无需重启
- 三个工具：get_skill / validate_skill / evaluate_skill，内置 skill-creator 技能辅助生成技能

## 适用场景

- 在多个 MCP 客户端间复用同一套本地技能
- 让 AI 通过对话按需加载专家级提示词技能
- 验证 SKILL.md 格式并评估技能触发可靠性

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L34: A **universal** Model Context Protocol (MCP) server that enables **any LLM or AI agent** to access expert skills fr
> L49: - **🌐 Universal** - Works with any MCP client (Claude Code/Desktop, Cline, Continue.dev, custom agents)
> L55: - **✨ Focused API** - Three tools: `get_skill` to load one, `validate_skill` to check a SKILL.md, `evaluate_skill` 

## 星数曲线

```mermaid
xychart-beta
    title "kdpa-llc/local-skills-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-29 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `bd26b3760871` · [字段定义](../../DATASET.md)*
