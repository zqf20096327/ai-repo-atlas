# JCodesMore/fix-claude-code

⭐ 22 · MIT · 推送 2026-08-15 · [GitHub](https://github.com/JCodesMore/fix-claude-code) · [官网](https://dsc.gg/jcodesmore) · 个人维护

**交互式 Claude Code 插件：一键检测并优化性能配置**

面向 Claude Code 用户的交互式插件，运行 /fixclaude 命令启动向导：读取 ~/.claude/settings.json 检测当前配置，合并 8 项性能相关设置（如 EFFORT_LEVEL、MAX_THINKING_TOKENS、禁用遥测等），并通过 /schedule 创建云端定时任务维持 5 小时滚动限流窗口活跃；可选安装 Claude HUD、Context7、Playwright 等配套插件。插件为单一 skill、无代码依赖，经插件市场或手动命令安装，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取并合并 settings.json 的 8 项性能设置，保留原有配置
- 通过 /schedule 云端例程维持限流窗口活跃
- 可选自动安装 Context7/Playwright MCP 及配套插件
- 单一交互式 skill，无代码依赖

## 适用场景

- 不想手动翻配置文件，用向导一键优化 Claude Code 性能
- 缓解 5 小时滚动限流窗口的中断问题
- 顺带装上状态面板、浏览器控制等配套插件

## 场景标签

 · 领域:AI 开发者工具

## 证据(README 行号)

> L5: An interactive Claude Code plugin that fixes and optimizes your Claude Code performance. Sourced from dozens of comm
> L21: |`/fixclaude`|Interactive performance wizard -- detects current settings, applies 8 proven fixes, and optionally in
> L93: The plugin is a single interactive skill with no code dependencies. It reads your current `~/.claude/settings.json`

## 星数曲线

```mermaid
xychart-beta
    title "JCodesMore/fix-claude-code 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `9eb6e25e427f` · [字段定义](../../DATASET.md)*
