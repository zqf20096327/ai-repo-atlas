# ongridio/ongrid

⭐ 1,294 · Go · AGPL-3.0 · 推送 2026-11-19 · [GitHub](https://github.com/ongridio/ongrid) · [官网](https://ongrid.cloud) · 组织维护 · 中文 README

**从 Slack/Telegram 等聊天渠道诊断并处置基础设施故障的运维 AI Agent**

以 Go 编写、自托管的运维 AI Agent 系统：通过 Coordinator + 专家子代理（SRE/网络/DB）结构响应运维提问与告警，执行根因分析（遍历拓扑、关联指标/日志/追踪、定位到源码行）、远程只读巡检（bash 沙箱 + 26+ 工具）、浏览器 SSH，并支持审批与写操作门控。内置 Prometheus + Loki + Tempo + Grafana 可观测栈，支持 MCP 服务器注册、知识库 RAG 索引与工作流编排，从 Slack、Telegram、Lark、钉钉、企业微信等 IM 双向交互。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 告警触发自动调查：生成 RCA worker 并将原因写回聊天
- 根因分析沿拓扑关联 m/l/t 并锚定到源码行
- Bring your own model：Anthropic/OpenAI/GLM/DeepSeek/Gemini/Kimi 热切换
- 零入站端口架构：edge 主动外拨，所有调用留审计

## 适用场景

- 值班时在群里让 Agent 自动调查告警并给出根因报告
- 给服务器上的 Agent 配置只读巡检工具与审批门控
- 将 runbook、事故历史、代码仓库索引进知识库供人和 Agent 共同检索

## 场景标签

`RAG` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: > **An ops AI Agent that understands your infrastructure, finds the root cause, and fixes it — right from Slack or T
> L33: - 🤖 **Coordinator + Specialist agents** — coordinator dispatches to SRE / network / DB sub-agents
> L40: - 🧠 **Bring your own model** — Anthropic / OpenAI / GLM / DeepSeek / Gemini / Kimi, hot routing

## 星数曲线

```mermaid
xychart-beta
    title "ongridio/ongrid 星数(近 23 点)"
    x-axis ["2026-10-21", "2026-10-22", "2026-10-23", "2026-10-24", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-21", "2026-11-22", "2026-11-23"]
    y-axis "stars" 1181 --> 1304
    line [1191, 1203, 1215, 1219, 1222, 1236, 1239, 1240, 1243, 1244, 1245, 1219, 1267, 1272, 1275, 1277, 1278, 1279, 1282, 1284, 1291, 1294, 1294]
```

2026-10-21 1,191 → 2026-11-23 1,294（+103）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `13490c66e678` · [字段定义](../../DATASET.md)*
