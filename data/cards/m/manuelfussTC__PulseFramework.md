# manuelfussTC/PulseFramework

⭐ 28 · TypeScript · MIT · 推送 2026-01-15 · [GitHub](https://github.com/manuelfussTC/PulseFramework) · [官网](https://manuel-fuss.de/pulse) · 个人维护

**面向 Cursor 的受控 AI 编程框架：CLI + MCP 服务器与安全护栏**

PULSE 是一套 AI 辅助开发的方法论与工具包，包含 pulse CLI（13 条命令）与 MCP 服务器（10 个 pulse_* 工具），自动接入 Cursor IDE；另生成 AGENTS.md 兼容 Windsurf、Copilot、Cline。核心机制为 5 项护栏（30 分钟检查点规则、删除/推送确认、密钥扫描、定期 Git 提交）与 5 种循环检测模式（修复链、回摆、文件churn 等），并提供升级工作流（pulse_escalate）与知识沉淀（pulse_learn）。安装方式为 git clone 后 npm 构建，要求项目为单一 Git 仓库。

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

- CLI 13 条命令 + MCP 服务器 10 个工具，自动接入 Cursor IDE
- 5 项护栏：30 分钟规则、删除/推送确认、密钥检测、定期 Git checkpoint
- 5 种循环检测模式识别修复链、回摆与文件churn
- 生成 AGENTS.md 支持 Windsurf、Copilot、Cline 等

## 适用场景

- 在 Cursor 中给 AI agent 加装检查点与安全护栏
- 检测 AI 编码陷入修复循环并触发升级流程
- 防止 API 密钥等敏感信息被提交推送

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L8: **PULSE** is a complete toolkit for controlled AI-assisted software development: methodology, CLI commands, MCP serv
> L187: |**CLI** (`pulse`)|13 commands for prompts, checkpoints, safeguards, escalation|
> L188: |**MCP Server** (`pulse_*`)|10 tools for automatic Cursor IDE integration|

## 星数曲线

```mermaid
xychart-beta
    title "manuelfussTC/PulseFramework 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-31 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `e9cdda11945f` · [字段定义](../../DATASET.md)*
