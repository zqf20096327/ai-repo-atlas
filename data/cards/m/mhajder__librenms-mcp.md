# mhajder/librenms-mcp

⭐ 42 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/mhajder/librenms-mcp) · [官网](https://pypi.org/project/librenms-mcp/) · 个人维护

**让 AI agent 通过 MCP 查询和管理 LibreNMS 网络监控的服务器**

基于 Python 的 Model Context Protocol 服务器，将 LibreNMS 网络监控系统的设备、端口、告警、日志、计费、BGP/OSPF/VRF、ARP/FDB、传感器、服务与 Oxidized 配置备份等功能以 MCP 工具形式暴露给 AI agent，支持读写操作与只读模式。提供分页（默认每页 100 条）以防撑爆 LLM 上下文，图表以 MCP 图像（PNG）返回。需 Python 3.11-3.15 与 LibreNMS API token，可通过 PyPI、源码或 Docker 部署。

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

- 覆盖设备/端口/告警/日志/计费/路由/传感器等百余个 MCP 工具
- 只读模式、速率限制与 API 安全配置
- 列表工具统一分页（默认 100 条/页）防 LLM 上下文过载
- 图表以 PNG MCP 图像返回，兼容 Claude 等 MCP 客户端

## 适用场景

- 网络运维团队用 AI agent 查询设备状态与告警
- 通过对话自动管理 LibreNMS 设备组与告警规则
- 让 agent 检索 Oxidized 设备配置与网络拓扑

## 场景标签

 · 领域:网络运维/LLM 基础设施

## 证据(README 行号)

> L3: **Let AI agents query and manage LibreNMS network monitoring through the Model Context Protocol**
> L15: LibreNMS MCP Server is a Python-based Model Context Protocol (MCP) server designed to provide advanced, programmabl
> L322: To prevent overloading LLM contexts when querying large LibreNMS production instances, all list, search, and log t

## 星数曲线

```mermaid
xychart-beta
    title "mhajder/librenms-mcp 星数(近 2 点)"
    x-axis ["2026-10-19", "2026-10-29"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-19 42 → 2026-10-29 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ae06586cd086` · [字段定义](../../DATASET.md)*
