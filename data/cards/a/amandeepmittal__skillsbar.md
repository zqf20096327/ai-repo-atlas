# amandeepmittal/skillsbar

⭐ 28 · Swift · Apache-2.0 · 推送 2026-09-10 · [GitHub](https://github.com/amandeepmittal/skillsbar) · [官网](https://amanhimself.dev/skillsbar/) · 个人维护

**macOS 菜单栏应用：浏览管理 Claude Code/Codex/pi 的技能与代理**

面向使用 Claude Code、Codex、pi 的 macOS 开发者的菜单栏应用：在统一界面中按标签页浏览、搜索、固定这些工具的技能、插件、collections 与 sub-agents，支持 Command Palette、使用统计热力图、技能健康检查（frontmatter 校验、重复触发等）、跨来源自定义分组、项目级指令文件（CLAUDE.md/AGENTS.md 等）检测，并通过 FSEvents 实现目录变更自动刷新。以 zip 安装包分发，未签名构建需手动移除 quarantine 标志。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一浏览 Claude Code、Codex、pi 的技能/插件/代理，支持跨来源 Collections
- 记录三端技能调用统计（30d/7d/全期）并输出每日热力图与排行
- 技能健康检查：无效 frontmatter、缺失描述、重复触发等一键清理
- FSEvents 目录监听，技能增删时自动刷新

## 适用场景

- 在一处查看和整理分散在多个 AI 编码工具里的技能与代理
- 检查技能文件的 frontmatter 等常见问题并批量清理
- 查看各技能的实际调用频率以决定保留哪些

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5:  A macOS menu bar app for browsing and managing your Claude Code, Codex, and pi skills, project skills, plugins, col
> L37: - **Tabbed browsing** - separate tabs for Claude Code, Codex, pi, and Collections with count badges
> L52: - **Usage stats** - tracks Claude Code, Codex CLI, Codex Desktop, and pi skill invocations in app-owned history, wi

## 星数曲线

```mermaid
xychart-beta
    title "amandeepmittal/skillsbar 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 26 --> 29
    line [27, 28, 28]
```

2026-10-18 27 → 2026-10-28 28（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `3b60db234a66` · [字段定义](../../DATASET.md)*
