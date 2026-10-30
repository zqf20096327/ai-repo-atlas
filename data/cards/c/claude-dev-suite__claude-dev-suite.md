# claude-dev-suite/claude-dev-suite

⭐ 46 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/claude-dev-suite/claude-dev-suite) · 组织维护

**为 AI 编程助手生成项目配置的工具箱：agents、skills、MCP、规则**

面向使用 AI 编程助手的开发者：向导读取项目 manifests 检测技术栈（React、Spring Boot、Unity、Android 等），从统一的 agents/skills/MCP servers 目录生成各助手自己的配置文件（AGENTS.md、.claude/、.cursor/rules/ 等），一次安装可输出到 Claude Code、Copilot、Cursor、Gemini CLI、Codex CLI、Cline、Kimi Code 七种助手。提供桌面安装包（Windows/macOS/Linux）、npx 仅装 skills、git clone 全工具箱三种方式；MCP servers 与 dashboard 需 Node.js 20+，写入文件可提交且覆盖前备份。Task Orchestrator 与 dashboard 聊天仅限 Claude Code（基于 Claude Agent SDK）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取 package.xml/pom.xml 等 manifests 自动检测技术栈并预选 agents/MCP
- 一次安装为 7 种 AI 编程助手生成各自格式的配置
- 安装时打印各助手不支持的能力差异而非掩盖
- 桌面安装包、npx skills、源码三种安装途径

## 适用场景

- 为项目里的多个 AI 编程助手统一生成 agents、skills 与 MCP 配置
- 团队共享可提交的助手配置，新成员 clone 后即得相同设置
- 为检测到的技术栈按需加载框架文档与领域专家 agent

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L9: **Point it at a repo and it configures your AI coding assistant for that stack** — specialized agents, framework ski
> L64: - **Multi-Assistant Output** - Generate configuration for **Claude Code, GitHub Copilot, Cursor, Gemini CLI, Codex 

## 星数曲线

```mermaid
xychart-beta
    title "claude-dev-suite/claude-dev-suite 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23", "2026-10-28", "2026-10-30"]
    y-axis "stars" 41 --> 47
    line [42, 43, 45, 46, 46]
```

2026-10-18 42 → 2026-10-30 46（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `d50ed862f9e1` · [字段定义](../../DATASET.md)*
