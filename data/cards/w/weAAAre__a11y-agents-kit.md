# weAAAre/a11y-agents-kit

⭐ 35 · TypeScript · MIT · 推送 2026-04-20 · [GitHub](https://github.com/weAAAre/a11y-agents-kit) · 组织维护

**为 AI 编程 agent 提供无障碍检查的 MCP 服务器与技能套件**

由无障碍学校 weAAAre 维护的 monorepo，包含 5 个 MCP 服务器：颜色对比度检查（覆盖 WCAG 2.2 最多 5 条成功标准）、西英双语可读性分析（13 个公式）、驱动 macOS VoiceOver/NVDA/无头虚拟屏幕阅读器的审计服务器（各覆盖最多 12 条成功标准），另有 ARIA 模式 agent 技能。通过 npx 安装，兼容 VS Code、Claude Code、Cursor、Codex 等客户端；部分服务器依赖 macOS/VoiceOver 或 Windows/NVDA 环境，且声明不替代人工审计。

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

- 5 个 MCP 服务器覆盖颜色对比、可读性与屏幕阅读器审计
- 屏幕阅读器审计可程序化操作 VoiceOver/NVDA 并记录结构化 WCAG 发现
- 13 种科学验证的可读性公式，支持西班牙语与英语
- 提供 VS Code、Claude Code、Cursor、Codex、Goose 等客户端的接入配置

## 适用场景

- 在 IDE 中让 AI 编程 agent 实时检查配色对比度与可读性
- 在 PR 流程中自动化屏幕阅读器测试并生成 WCAG 报告
- 为 AI agent 安装 ARIA 可访问 UI 模式技能

## 场景标签

 · 领域:开发工具/无障碍测试

## 证据(README 行号)

> L16: This monorepo is weAAAre's open-source contribution: free MCP servers and agent skills that bring accessibility che
> L24: Model Context Protocol servers that give AI coding agents programmatic accessibility tooling.

## 星数曲线

```mermaid
xychart-beta
    title "weAAAre/a11y-agents-kit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 33 --> 36
    line [34, 35, 35]
```

2026-10-18 34 → 2026-10-29 35（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9db96d516cc1` · [字段定义](../../DATASET.md)*
