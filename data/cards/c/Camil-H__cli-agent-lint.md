# Camil-H/cli-agent-lint

⭐ 58 · Go · MIT · 推送 2026-05-08 · [GitHub](https://github.com/Camil-H/cli-agent-lint) · 个人维护

**审计 CLI 工具对 AI agent 就绪度的静态/主动检查与评分工具**

用 Go 编写的命令行审计工具：对目标 CLI 运行 34 项检查，覆盖流程安全（无 TTY 阻塞、退出码可靠）、令牌效率（JSON 输出、--quiet）、自描述（--help 可学习）、自动化安全（--yes、--dry-run、拒绝路径穿越）与可预测性五类，输出 A–F 字母评分卡。检查分被动（仅分析 --help）与主动（构造输入实际执行目标 CLI，可用 --no-probe 关闭）两种方式。面向需要让 agent 驱动 CLI 的开发者，提供 go install、Homebrew、apt 与二进制多种安装途径。

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

- 34 项检查分 5 类，输出 A–F 字母评分卡
- 被动/主动两种检查方法，--no-probe 仅运行无副作用检查
- 主动检查会以子进程执行目标 CLI，审计不受信 CLI 时建议 --no-probe 或容器隔离
- 支持 text/json 输出、按类别/严重度过滤、可配置超时

## 适用场景

- 发布 CLI 前检查其对自主 agent 的可用性
- 评估第三方 CLI 是否适合接入 agent 工作流
- CI 中对 CLI 做 agent 就绪度回归检查

## 场景标签

 · 领域:开发者工具/静态分析

## 证据(README 行号)

> L3: Audit CLI tools for AI agent-readiness. Runs 34 checks across 5 categories and produces a letter-grade scorecard tel
> L61: Every check targets a specific property that matters when an AI agent drives a CLI non-interactively. Checks are or

## 星数曲线

```mermaid
xychart-beta
    title "Camil-H/cli-agent-lint 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 57 --> 59
    line [58, 58]
```

2026-10-18 58 → 2026-10-28 58（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `7a3408850a2b` · [字段定义](../../DATASET.md)*
