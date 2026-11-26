# lgalabru/axel

⭐ 327 · Rust · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/lgalabru/axel) · [官网](https://axel.md) · 个人维护

**终端里的 AI 编码 Agent 编排工具：线程、命名 Agent 与远端主机**

Axel 是面向 Rex 终端的 Agent 编排程序：以线程为单位组织任务，线程以签名事件记录、可跨机器合并续接；支持创建多个命名 Agent，各自持有 Ed25519 密钥、权限、预算与技能集。它通过 Agent Client Protocol 驱动 Claude Code、Codex 等多种编码 Agent harness（内置适配器无需 Node），并提供守卫机制拒绝不可逆命令、按 Agent 限制预算。安装依赖 Rex 终端与所选 harness；提供 curl 脚本、Homebrew、Nix 三种安装方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 线程持久化：签名事件存储，跨机器合并、合盖后继续运行
- 命名 Agent 各自拥有密钥、权限、预算与独立技能集
- 经 ACP 协议驱动 Claude Code、Codex，另支持 OpenCode/Goose/Cursor 等多种 harness
- 守卫拒绝不可逆命令，按 Agent 设置支出预算

## 适用场景

- 在一个终端里同时运行多个编码 Agent 并让它们互相交接（构建+评审）
- 在远程主机上运行 Agent，密钥保留在本机
- 为不同 Agent 分配不同模型与技能分工

## 场景标签

`编码 Agent` `多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L8:  Agent orchestration, designed for Rex.
> L54: ### 🤖 Claude Code, Codex, OpenCode, Goose, Cursor and more
> L57: `codex`, `goose`, `cursor/sonnet`. Axel drives Claude Code and Codex over the Agent Client

## 星数曲线

```mermaid
xychart-beta
    title "lgalabru/axel 星数(近 15 点)"
    x-axis ["2026-11-02", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 197 --> 338
    line [208, 222, 233, 248, 266, 282, 286, 305, 313, 316, 318, 322, 325, 327, 327]
```

2026-11-02 208 → 2026-11-26 327（+119）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 mid · 依据 README sha `983d1c9c4a7a` · [字段定义](../../DATASET.md)*
