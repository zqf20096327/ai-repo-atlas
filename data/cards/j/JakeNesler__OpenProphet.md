# JakeNesler/OpenProphet

⭐ 114 · JavaScript · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/JakeNesler/OpenProphet) · 个人维护

**自主 AI 股票/期权交易代理，含 Web 仪表盘与 MCP 工具**

Node.js 代理系统在心跳循环上调度 OpenCode CLI（Claude 模型）驱动 AI 交易代理：按市场阶段定时唤醒，调用 MCP 工具查账户、扫描新闻、分析并下单，结果经 SSE 流式推送到 3737 端口的 Web 仪表盘；Go 后端对接 Alpaca 多账户（含纸面交易）。提供权限门控（资产类别、订单上限、日亏损熔断）、订单幂等与对账、Gemini 新闻清洗与本地向量检索等。运行需 Go、C 工具链、Node.js、OpenCode CLI 与 Alpaca 账户，并自行编译 Go 后端；README 声明为实验性研究项目，作者另有 openprophet.io 付费配置服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 分阶段心跳调度（盘前 15m 至收盘 1h）驱动自主代理循环
- 45+ MCP 交易工具，可独立接入 Claude Code/Cursor 等 MCP 客户端
- 多层护栏：工具封锁、资产类别门控、maxOrderValue、日亏损熔断、订单幂等与启动对账
- 8 标签页移动端仪表盘，SSE 实时流式输出

## 适用场景

- 纸面交易账户上运行全自动 AI 交易代理并实时监控
- 把 45+ 交易工具接入 Claude Code/Cursor 做手动交易
- 多 Alpaca 账户管理与热切换

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L27: OpenProphet is a fully autonomous trading harness that runs an AI agent on a heartbeat loop. The agent wakes up on 
> L39: 2. OpenCode subprocess spawns with Claude model + MCP tools
> L40: 3. Agent calls tools: check account, scan news, analyze setups, place orders

## 星数曲线

```mermaid
xychart-beta
    title "JakeNesler/OpenProphet 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 112 --> 115
    line [113, 114, 114]
```

2026-10-18 113 → 2026-10-29 114（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `35a3a4ab33b5` · [字段定义](../../DATASET.md)*
