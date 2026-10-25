# matrixorigin/Astra

⭐ 35 · Rust · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/matrixorigin/Astra) · 组织维护 · 中文 README

**面向企业的自托管 agent 运行时：治理上下文到执行的完整链路**

Astra 是一个用 Rust/TypeScript 实现的自托管长时 agent 运行时，形态为单一二进制（CLI/TUI/Server）加 Web 仪表盘和 TypeScript SDK。核心机制：Context Pipeline 组装模型请求并可 EXPLAIN ANALYZE 审查（论文称可减少 31% token）；策略与 provider 准入绑定身份和权限；Server 调度而由用户环境中的 Runner 执行工具调用；所有尝试、配置变更与检查点均版本化、可 diff 与回放。支持 BYOK 接入任意模型端点，可选集成 Jev 判断层。声明 1.0 前接口可能变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- EXPLAIN ANALYZE 展示上下文来源、预算与执行计时
- Server/Runner 分离：工具调用在用户自有环境执行，Server 无环境访问权
- 尝试、检查点与配置变更全版本化，可 diff、回放、回滚
- 单一二进制提供 CLI、TUI、Server 与 Web 仪表盘，BYOK 接入任意模型端点

## 适用场景

- 多用户、多应用共享 agent 时做统一治理与审计
- 在私有仓库与内网中运行受控的 agent 工作流
- 审查模型每次请求收到的上下文与执行证据

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L19: Astra is a self-hosted runtime for long-running agent Work. Every model
> L21: leaves evidence you can inspect, diff, and roll back, and execution runs
> L92: |**System of record**|The Codex task and workspace|An append-only session event stream assembled from plugins|Durab

## 星数曲线

```mermaid
xychart-beta
    title "matrixorigin/Astra 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-25 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0491f6bda599` · [字段定义](../../DATASET.md)*
