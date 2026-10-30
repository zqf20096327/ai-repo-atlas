# Kabi10/cursor-rules

⭐ 22 · JavaScript · MIT · 推送 2026-07-01 · [GitHub](https://github.com/Kabi10/cursor-rules) · [官网](https://www.npmjs.com/package/cursor-compose) · 个人维护

**扫描项目依赖并自动生成 AI 编辑器规则文件**

面向使用 Cursor、Copilot、Codex、Claude Code 等 AI 编辑器的开发者的 CLI 工具：一条 npx 命令扫描 package.json、requirements.txt、pubspec.yaml 等依赖文件，识别 Next.js、FastAPI、Flutter 等技术栈，从模块化构件生成规则文件——可输出跨编辑器通用的 AGENTS.md 或 Cursor 原生 .cursor/rules/*.mdc。生成内容置于受管标记之间，重新生成保留用户自加内容。需要 Node.js 18+，无需安装与配置文件。

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

- 读取 package.json/requirements.txt/pubspec.yaml 检测技术栈并生成规则
- 输出可移植 AGENTS.md 或 Cursor .mdc，支持 --all 一次生成两种
- AGENTS.md 受管标记外的手工内容在重新生成时保留
- 提供 saas/ecommerce/claude-code/agentic 等可选模块

## 适用场景

- 为新项目自动生成匹配实际技术栈的 AI 编辑器规则
- 用一份 AGENTS.md 在 Cursor/Copilot/Codex/Claude Code 间通用
- CI 中以 -y 非交互模式批量生成规则文件

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: One command scans your project, detects your frameworks, and writes a tailored rules file. Output a portable **`AGEN
> L22: `cursor-compose` reads your **real dependencies** (`package.json`, `requirements.txt`, `pubspec.yaml`) and composes

## 星数曲线

```mermaid
xychart-beta
    title "Kabi10/cursor-rules 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `cb3b21819c3e` · [字段定义](../../DATASET.md)*
