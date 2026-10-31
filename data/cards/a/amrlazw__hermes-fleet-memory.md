# amrlazw/hermes-fleet-memory

⭐ 15 · Python · MIT · 推送 2026-09-24 · [GitHub](https://github.com/amrlazw/hermes-fleet-memory) · 个人维护

**多实例 AI agent 舰队的跨设备共享向量记忆与执行网格**

面向运行多个 Hermes Agent 实例（VPS Telegram 机器人、工作笔记本、个人工作站）的开发者，提供跨设备共享的分布式向量记忆层：记忆存于 384 维向量数据库，检索按需通过 FastMCP 工具调用（fleet_memory_search），不做系统提示词常驻注入；用 UUID5 槽位原地更新加 LWW 时间戳防止重复漂移；以 FLEET_HARD_DOMAIN 在主机环境层强制 work/personal/shared 三域隔离，并经反向 WSTunnel 穿透 NAT 执行远端任务。后端需自建 Qdrant 集群（可用免费层），提供向导式初始化与 Claude Desktop/Code、Cursor 等客户端接入配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按需 FastMCP 向量检索，零常驻提示词注入
- UUID5 槽位原地覆盖 + LWW 时间戳的确定性状态解析
- 主机环境层强制的 work/personal/shared 三域防火墙
- 反向 WSTunnel NAT 穿透与跨节点任务队列（SQLite WAL + Ed25519 签名回执）

## 适用场景

- 让部署在不同设备上的多个 AI agent 共享同一份记忆
- 隔离工作与个人数据，防止企业机密跨域泄漏
- 通过 Telegram 机器人远程查看或操控 NAT 后的家庭工作站
- 无 GPU 的 VPS 上让 agent 把 GPU 任务委派给家用主机执行

## 场景标签

`Agent 记忆` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L69: *You now have all 12 FastMCP tools active for on-demand vector memory retrieval and execution directly inside your 
> L150:  Memories reside in a central 384-dimensional vector database. Retrieval occurs strictly **on-demand** via FastMCP

## 星数曲线

```mermaid
xychart-beta
    title "amrlazw/hermes-fleet-memory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `0fe7cc82c430` · [字段定义](../../DATASET.md)*
