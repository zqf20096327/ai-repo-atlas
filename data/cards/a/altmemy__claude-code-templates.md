# altmemy/claude-code-templates

⭐ 25 · Shell · 推送 2026-03-26 · [GitHub](https://github.com/altmemy/claude-code-templates) · 个人维护 · 中文 README

**面向 Claude Code 的三套项目模板，内置 agents/skills/rules/hooks**

为 Claude Code 提供三种技术栈的生产级项目模板：React/Next.js 前端、Spring Boot 后端、Flutter 跨平台应用。每个模板包含 7 个专职 AI agent（主工程师、代码审查、安全、性能、测试、DevOps 等，分别指定 Sonnet/Opus 模型与写入/只读模式）、5 个按需加载的技能文档、5 条路径级编码规则和 4 个自动化 hook（自动格式化、拦截危险命令、会话上下文注入、停止前编译校验）。使用方式为 clone 或下载对应文件夹后在该目录运行 claude。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种技术栈模板：Next.js 16 / Spring Boot 4 / Flutter 3.41
- 每个模板内置 7 个指定模型与权限模式的专职 agent
- 4 个自动化 hook：格式化、危险命令拦截、会话上下文、停止前编译校验
- 路径级规则与含完整代码示例的技能文档

## 适用场景

- 用 Claude Code 快速起一个带预配置 agent 的前端/后端/移动项目
- 团队统一 Claude Code 的编码规范与安全约束
- 让 Claude 在隔离 worktree 中执行构建、测试与审查任务

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L8: Production-grade project templates for Claude Code, each packed with **7 specialized AI agents**, **5 reusable skill
> L10: Pick a template, clone the folder, and let Claude Code build your app.

## 星数曲线

```mermaid
xychart-beta
    title "altmemy/claude-code-templates 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `bb6ad4a7070c` · [字段定义](../../DATASET.md)*
