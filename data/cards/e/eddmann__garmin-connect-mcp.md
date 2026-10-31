# eddmann/garmin-connect-mcp

⭐ 65 · Python · MIT · 推送 2026-05-20 · [GitHub](https://github.com/eddmann/garmin-connect-mcp) · 个人维护

**让 LLM 通过 MCP 访问 Garmin Connect 健康与运动数据的服务器**

基于 Model Context Protocol 的 Garmin Connect 集成服务器：提供 22 个工具（活动查询与分析、健康指标、睡眠、心率、训练分析、体重管理、设备与装备等 8 类）、3 个 MCP 资源（运动员档案、训练就绪度、每日健康）和 6 个提示模板。通过 OAuth 令牌认证并支持 MFA，令牌存于 ~/.garminconnect/ 自动刷新。用户在 Claude 等 LLM 客户端中以自然语言查询 Garmin 数据。需 Python 3.12+（uv）或 Docker 运行，明确声明与 Garmin 公司无隶属关系。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 22 个工具覆盖活动、健康、训练、体重等 8 个类别
- OAuth 令牌认证与 MFA 支持，令牌持久化自动刷新
- 3 个 MCP 资源自动提供持续上下文（档案/就绪度/每日健康）
- 6 个提示模板支持常见查询（训练分析、睡眠报告、健康概览）

## 适用场景

- 在 Claude 中用自然语言查询我的跑步记录与睡眠数据
- 对比近期训练表现、查看 VO2 max 趋势与训练就绪度
- 记录体重、身体成分与血压等健康数据

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L5: A Model Context Protocol (MCP) server for Garmin Connect integration. Access your activities, health data, training 
> L13: This MCP server provides 22 tools to interact with your Garmin Connect account, organized into 8 categories:

## 星数曲线

```mermaid
xychart-beta
    title "eddmann/garmin-connect-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 63 --> 66
    line [64, 65, 65]
```

2026-10-18 64 → 2026-10-31 65（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `99c88b04a2c2` · [字段定义](../../DATASET.md)*
