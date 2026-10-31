# NitrusAphalion/tessra

⭐ 15 · Rust · MIT · 推送 2026-09-19 · [GitHub](https://github.com/NitrusAphalion/tessra) · [官网](https://github.com/NitrusAphalion/tessra) · 个人维护

**面向 AI agent 协作的版本控制系统，与 git 并行运行**

用 Rust 编写的单一二进制 CLI 版本控制工具，面向编写代码的 AI agent 与 swarm 场景：以 Tree-sitter 将文件拆为函数/类型等单元，使多个 agent 编辑同一文件的不同单元可同时落地；由守护进程在干净副本中运行验证器并对结果签名，仅符合标准（standard）的变更可落地；提供 plan 任务分拆、agent 签名与撤销、context/remember 仓库记忆、通过 MCP（stdio，13 个动词）接入 Claude Code 等 MCP 客户端，并支持与 .git/ 双向桥接导出/导入提交。当前为 pre-release，macOS/Linux 构建尚未在相应平台测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Tree-sitter 语义单元合并：多 agent 编辑同一文件不同单元均可落地
- 守护进程在 scratch 副本中运行验证器并对结果签名（attestation）
- plan 按依赖分拆任务供 agent swarm 并行提议，frontier 逐个落地
- MCP 接口暴露 13 个动词，可接入 Claude Code 等客户端
- 与 .git/ 双向桥接：落地修订可导出为普通 git 提交

## 适用场景

- 多个 AI agent 并行修改同一代码库而避免行级冲突
- 以代码化标准替代逐 diff 人工审查，仅落地通过验证的变更
- 在现有 git checkout 旁并行使用，团队其他成员工作流不变
- 将仓库级记忆（gotcha、约定、决策）随代码保存供下次会话读取

## 场景标签

`多智能体` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5:  The version control system for the era of AI.
> L7: Git records what changed. Tessra records what changed, why , and what is known to be true about the result.
> L8: Built for agents that write code around the clock, and for the humans who decide what to trust.

## 星数曲线

```mermaid
xychart-beta
    title "NitrusAphalion/tessra 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `4c721d8b961f` · [字段定义](../../DATASET.md)*
