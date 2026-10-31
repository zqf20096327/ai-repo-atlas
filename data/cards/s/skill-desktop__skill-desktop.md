# skill-desktop/skill-desktop

⭐ 25 · TypeScript · MIT · 推送 2026-05-23 · [GitHub](https://github.com/skill-desktop/skill-desktop) · [官网](https://skill-desktop.com) · 组织维护 · 中文 README

**桌面端 AI agent 技能管理平台：集中管理与同步 SKILL.md 技能**

基于 Tauri(Rust)+React 的原生桌面应用，按 Anthropic 的 Agent Skills 标准集中管理技能：技能存于 ~/.skill_desktop/ 中央库，通过符号链接同步到 Claude Code、Cursor、Codex、Gemini CLI、OpenCode、Windsurf 等工具的技能目录。功能含目录树与实时同步、技能创建向导、项目级 Workspace 隔离、从 GitHub/MCP Registry 导入、权限风险分析与代码扫描。提供 AppImage，Homebrew/Winget 标注 coming soon。

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

- 中央技能库 + 符号链接同步到多个 AI 工具目录
- 自动检测已安装的 AI 工具（Claude Code/Cursor/Codex/Gemini CLI/OpenCode/Windsurf）
- 技能权限声明与自动代码安全风险扫描
- 从 GitHub、Glama、MCP.so、MCPServers.org、Smithery 导入并可转换 MCP 工具为技能

## 适用场景

- 我需要把同一批技能分发到多个 AI 编码工具而不重复拷贝
- 为不同项目/agent 维护隔离的技能组合
- 导入社区技能前审查权限与安全风险

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L7:  Manage, organize, and distribute your AI agent skills following the Agent Skills standard.
> L52: ### AI Tool Sync — One library, every AI agent
> L55: - **Auto-detect installed tools** - Claude Code, Cursor, Codex, Gemini CLI, OpenCode, Windsurf, and the cross-tool 

## 星数曲线

```mermaid
xychart-beta
    title "skill-desktop/skill-desktop 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-31 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `560888df9b0f` · [字段定义](../../DATASET.md)*
