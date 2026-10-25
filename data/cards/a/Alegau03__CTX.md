# Alegau03/CTX

⭐ 144 · Rust · 推送 2026-05-11 · [GitHub](https://github.com/Alegau03/CTX) · 个人维护

**面向 OpenCode 等 AI 编码代理的本地上下文运行时**

用 Rust 实现的单二进制本地运行时层，安装于 OpenCode 等 AI 编码代理之下：索引仓库、将 AGENTS.md/CLAUDE.md 等指令导入图内存并按任务检索、通过 read-cache 与 digest/outline 模式压缩文件重读、裁剪日志与 diff、生成紧凑任务包，并以本地 MCP 工具（stdio 与 localhost HTTP JSON-RPC）和 /ctx-* 斜杠命令暴露能力；full profile 附带右侧栏实时 Dashboard。默认 local-only、无强制网络调用，敏感附件默认阻断。提供 Cargo/npm/brew/安装脚本/Release 归档多种安装途径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 图内存替代整份 AGENTS.md 逐轮加载，按任务检索指令
- read-cache 压缩与 delta-aware 索引复用未变更文件
- 本地 stdio MCP 与 localhost HTTP JSON-RPC 运行时
- full profile 提供右侧栏实时 token 节省 Dashboard

## 适用场景

- 降低 AI 编码代理的 token 消耗与文件重读成本
- 将项目规则沉淀为可检索的图内存与可复用经验
- 裁剪冗长 shell 日志与 diff，仅保留根因相关内容

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L21: > CTX is a local context runtime for OpenCode and AI coding agents. It keeps repository knowledge, reusable rules, 
> L34: CTX is a local runtime layer for OpenCode. It indexes the repository, stores reusable guidance as graph memory, exp
> L218: |MCP|local stdio MCP plus localhost HTTP JSON-RPC runtime|

## 星数曲线

```mermaid
xychart-beta
    title "Alegau03/CTX 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 143 --> 145
    line [144, 144]
```

2026-10-18 144 → 2026-10-25 144（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `429484257563` · [字段定义](../../DATASET.md)*
