# ChrisVip001/joyczl-agent

⭐ 102 · Rust · MIT · 推送 2026-10-30 · [GitHub](https://github.com/ChrisVip001/joyczl-agent) · 个人维护 · 中文 README

**本地优先的个人 AI 助手：Rust 核心+多端网关**

代号 Joy 的本地优先个人助手：Rust 负责代理循环、记忆（FTS5 语义事实/情景/技能）、工具与 state.db 状态管理，TypeScript 提供浏览器/聊天网关与仪表盘，Python 仅作轻量 SDK。客户端通过 JSON-RPC over stdio 连接唯一 app-server 进程。内置 11 个工具加 MCP 服务器支持，预适配 12 个 LLM 提供商可随时切换，含确定性评测与每轮 trace/用量记录。运行需 DeepSeek 等提供商的 API key，密钥存 OS keychain 或回退本地文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Rust 拥有代理循环/记忆/工具/状态，模块目标 <500 行
- 预适配 12 个 LLM 提供商，/model 命令即时切换
- FTS5 记忆（CJK 支持）+ 检索门控 + 图式规划
- 确定性评测门禁发布、每轮 trace 与 token 用量落库

## 适用场景

- 在自己机器上运行带持久记忆的个人 AI 助手
- 通过 Telegram/Discord/微信/飞书网关与助手对话
- 接入 MCP 服务器扩展工具能力

## 场景标签

`Agent 框架` `AI 助手` `Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: > A local-first personal assistant: Rust owns logic and state, TypeScript
> L45: - **Converse** on the terminal, in the dashboard, or through chat gateways

## 星数曲线

```mermaid
xychart-beta
    title "ChrisVip001/joyczl-agent 星数(近 3 点)"
    x-axis ["2026-10-29", "2026-10-30", "2026-10-31"]
    y-axis "stars" 100 --> 103
    line [101, 102, 102]
```

2026-10-29 101 → 2026-10-31 102（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `9633e5a9ef50` · [字段定义](../../DATASET.md)*
