# Corvidae-Coding-Projects/OpenClaudia

⭐ 97 · Rust · MIT · 推送 2026-10-18 · [GitHub](https://github.com/Corvidae-Coding-Projects/OpenClaudia) · 组织维护

**Rust 编写的开源 agentic coding harness，多前端多模型适配**

实验性 Rust agent harness，提供多前端（全屏 TUI、行式 REPL、one-shot、HTTP 代理、ACP server、loop 模式）与多家 provider 适配器（Anthropic/OpenAI/Google/DeepSeek/Qwen/Z.AI/Kimi/MiniMax/Ollama 等）。工具面覆盖 bash、文件编辑、LSP、Git worktree、Cron 调度、MCP 资源、类型化技术记忆（memory_* 工具集）等。README 明确声明未达生产可用：审计发现可达性、隔离、取消、持久化等多处缺陷，勿用于敏感仓库或无人值守破坏性操作。通过 cargo 从源码构建，浏览器功能需显式启用 feature。项目配置位于 .openclaudia/config.yaml。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 10 家 provider 适配器，含 OpenAI 兼容端点与 Ollama 本地运行
- 6 种前端形态：全屏 TUI、REPL、one-shot、HTTP 代理、ACP server、loop 模式
- 类型化技术记忆体系：memory_* 工具集含引用绑定、冲突处理、导出导入
- Git worktree 隔离操作与 UTC Cron 持久调度

## 适用场景

- 需要多模型切换的命令行编码 agent 环境
- 在隔离 git worktree 中执行 agent 代码修改
- 定时触发带审批机制的 agent 任务

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: OpenClaudia is an experimental Rust agent harness with multiple frontends,
> L22: - Provider adapters for Anthropic, OpenAI, Google, DeepSeek, Qwen, Z.AI, Kimi,

## 星数曲线

```mermaid
xychart-beta
    title "Corvidae-Coding-Projects/OpenClaudia 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 95 --> 98
    line [96, 97, 97]
```

2026-10-18 96 → 2026-10-26 97（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `76cbbe709a2a` · [字段定义](../../DATASET.md)*
