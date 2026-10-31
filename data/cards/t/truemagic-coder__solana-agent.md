# truemagic-coder/solana-agent

⭐ 15 · Python · MIT · 推送 2026-05-13 · [GitHub](https://github.com/truemagic-coder/solana-agent) · [官网](https://solana-agent.com/) · 组织维护

**托管 Solana Agent 平台的 Python 客户端 SDK：接入托管聊天与钱包**

面向托管 Solana Agent 平台的公共 SDK，Python 包形式发布。功能包括：每个客户端实例一个 agent 的托管聊天、托管钱包流程（privy_user_id 获取、私钥导出、钱包轮换）、托管账户与计费 API、优先服务层级、托管记忆（7 天/30 天 TTL 层级）、付费 hosted search 实时网络与 X 结果，以及通过 Streamable HTTP MCP 服务器接入外部工具。提供 CLI（uvx 运行）与钱包冒烟测试命令，支持 Python 3.13-3.14，MIT 许可。

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

- 托管聊天与托管钱包（私钥导出、钱包轮换）流程
- MCP 插件支持：经 Streamable HTTP 接入外部工具
- 托管记忆（work/project 两种 TTL 层级）与优先服务层级
- CLI 冒烟测试：USDC 转账、token 数学、技术分析、swap、trigger、earn 等检查项

## 适用场景

- 在自己的 Python 应用中调用 Solana Agent 托管平台的聊天与钱包能力
- 通过 MCP 工具扩展托管 agent 的可调用能力
- 上线前用 CLI 冒烟命令验证托管聊天、记忆与交易链路

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L11: Public SDK for the hosted Solana Agent platform.
> L18: - MCP plugin support for external tools.

## 星数曲线

```mermaid
xychart-beta
    title "truemagic-coder/solana-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `179f96aac208` · [字段定义](../../DATASET.md)*
