# GenseeAI/gensee-crate

⭐ 125 · Rust · Apache-2.0 · 推送 2026-09-07 · [GitHub](https://github.com/GenseeAI/gensee-crate) · [官网](https://crate-docs.gensee.ai/) · 组织维护

**自主 AI agent 的安全与控制层：策略约束、审查与恢复**

面向运行 AI agent（Codex、Claude Code、Cursor、GitHub Copilot、Antigravity 等）的用户，提供本地策略执行（允许/询问/阻断工具动作、保护敏感路径）、按请求分组的 Review Queue、基于 macOS Endpoint Security 的越界漂移检测、Git 变更前恢复点，以及对 agent 配置（指令/hooks/MCP/权限）的审计。Team 版面向自托管 Linux 环境，提供 tclone 事务性工作区分叉、能力租约与凭证代理。CLI 经 curl 脚本安装，macOS 提供签名桌面应用。项目状态为 alpha，执行强度依赖具体集成与运行环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 本地策略允许/询问/阻断工具动作并保护敏感路径
- Review Queue 按请求聚合审查、暴露越界漂移与失败验证
- macOS Endpoint Security 独立观察文件变更以对比声明意图
- Team 版 tclone 事务性工作区分叉与短期能力租约

## 适用场景

- 让 AI agent 在 Mac 上自主干活同时保持审查与恢复能力
- 审计 agent 的配置（hooks/MCP/权限）是否被篡改
- 团队在自托管 Linux 上以隔离分叉方式运行并人工决定合并或丢弃

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L5:  Gensee Crate is an open-source safety and control layer for autonomous AI.
> L39: - **Set boundaries before risky actions.** Local policy can allow, ask, or block
> L80: - A **Review Queue** that groups work by request and shows what needs attention.

## 星数曲线

```mermaid
xychart-beta
    title "GenseeAI/gensee-crate 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24"]
    y-axis "stars" 123 --> 126
    line [124, 125, 125]
```

2026-10-18 124 → 2026-10-24 125（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `4c8fc196b2aa` · [字段定义](../../DATASET.md)*
