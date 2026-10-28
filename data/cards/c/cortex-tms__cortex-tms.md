# cortex-tms/cortex-tms

⭐ 180 · MDX · MIT · 推送 2026-10-26 · [GitHub](https://github.com/cortex-tms/cortex-tms) · [官网](https://cortex-tms.org/) · 个人维护

**为 AI 编码代理生成并校验项目治理文档的 CLI 工具**

面向使用 AI 编码代理的开发者的 npm CLI 工具：按 HOT/WARM/COLD 分层脚手架生成 PATTERNS.md、CLAUDE.md、ARCHITECTURE.md 等治理文档，提供结构校验、基于 git 时间戳的文档过期检测（v4.0，不做语义分析）、任务归档、迁移与交互式仪表盘。另含 AI 驱动的语义校验命令 review、git pre-commit 钩子，以及只读 MCP 服务器，可将治理文档作为资源暴露给 Claude Desktop、Cursor 等 MCP 客户端。提供 CI/CD 校验模板与 node/python/go 治理预设包。明确声明不做 token 优化、不替代代码评审。

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

- 分层脚手架生成治理文档（HOT/WARM/COLD 三层结构）
- 基于 git 时间戳的文档过期检测（v4.0，可配置阈值与排除规则）
- 只读 MCP 服务器向 MCP 客户端暴露 13 类治理文档资源
- pre-commit 钩子与 GitHub Actions 校验模板

## 适用场景

- 让 AI 编码代理遵循项目自有规范而非训练数据中的惯例
- 在 CI 中自动检测治理文档相对代码变更是否过期
- 通过 MCP 把项目治理文档接入 Claude Desktop 或 Cursor

## 场景标签

 · 领域:开发者工具/AI 代理治理

## 证据(README 行号)

> L17: Cortex TMS scaffolds and validates governance documentation for AI coding agents. As AI models get more powerful an
> L215: Start a read-only MCP (Model Context Protocol) server that exposes your TMS governance docs as resources to any AI

## 星数曲线

```mermaid
xychart-beta
    title "cortex-tms/cortex-tms 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 179 --> 181
    line [180, 180]
```

2026-10-18 180 → 2026-10-28 180（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `4e35b34a159e` · [字段定义](../../DATASET.md)*
