# tinyhumansai/tinyjuice

⭐ 21 · Rust · GPL-3.0 · 推送 2026-10-26 · [GitHub](https://github.com/tinyhumansai/tinyjuice) · [官网](https://crates.io/crates/tinyjuice) · 组织维护

**面向终端重度 agent 的 token 压缩库：压缩工具输出进模型上下文**

Rust 编写的 token 压缩库，部署在工具输出与模型上下文之间：对日志、diff、JSON、搜索结果、HTML、源码等内容按类型走不同压缩路径，丢弃部分会显式标记，CCR 缓存默认保存原始内容并附带检索 footer 供按需恢复。支持 full/light/off/auto 的 agent 级策略、命令感知规则、可选的 LLM 摘要阶段（默认关闭、OnDemand 模式），并为 Codex CLI 与 Claude Code 提供 hook 安装器。README 明确尚未发布压缩率声明。以 crates.io 库与 cargo 安装的 CLI 形式提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- JSON/代码/日志/搜索/diff/HTML 的分内容类型压缩路径
- CCR 缓存保存原始内容并附 juice_retrieve 恢复 footer
- full/light/off/auto 的 agent 级压缩策略
- tinyjuice install 为 Codex CLI 与 Claude Code 安装 hook

## 适用场景

- 压缩 coding agent 的工具输出以节省模型上下文
- 在保留可恢复原始内容的前提下精简大型日志与 diff
- 为不同 agent 按策略粒度配置压缩行为

## 场景标签

 · 领域:LLM 基础设施/上下文管理

## 证据(README 行号)

> L8: **TinyJuice is token compression for terminal-heavy agents.** It sits between
> L47: Hosts use `tinyjuice-bus` for its wire contract and the separate

## 星数曲线

```mermaid
xychart-beta
    title "tinyhumansai/tinyjuice 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `2e8057f66dee` · [字段定义](../../DATASET.md)*
