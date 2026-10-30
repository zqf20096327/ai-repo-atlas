# Wael-Rd/gns3-mcp-server

⭐ 27 · Python · MIT · 推送 2026-01-06 · [GitHub](https://github.com/Wael-Rd/gns3-mcp-server) · [官网](https://github.com/Wael-Rd/gns3-mcp-server) · 个人维护

**让 AI 客户端通过 MCP 操控 GNS3 网络模拟的 42 工具服务器**

基于 FastMCP 的 Python MCP 服务器，把 GNS3 REST API 封装为 42 个 MCP 工具，供 Gemini CLI 等 MCP 客户端调用，实现自然语言创建拓扑、配置设备、抓包、快照与批量操作。内置 15+ 配置模板（OSPF/BGP/VLAN/NAT/SSH 等），支持认证、SSL 与令牌鉴权。前置要求为本地运行的 GNS3 Server（默认 localhost:3080）与 Python 3.10+，通过 git clone 源码安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 42 个 MCP 工具覆盖 GNS3 项目、节点、链路、快照、抓包与绘图
- 15+ 预置配置模板（OSPF/EIGRP/BGP/VLAN/NAT/ACL/QoS 等）
- 自然语言驱动拓扑创建、VLAN 配置与故障诊断示例
- 支持认证、SSL/TLS 与速率限制

## 适用场景

- 用自然语言让 AI 搭建企业 WAN 或 CCNA 实验拓扑
- 批量下发路由器 SSH 等配置并做拓扑校验
- 网络课程自动建实验环境、安全研究做受控测试环境

## 场景标签

 · 领域:网络工程/自动化

## 证据(README 行号)

> L9: > **The Complete AI-Powered GNS3 Network Simulation Platform**
> L362: │   Gemini CLI    │◄──►│  GNS3 MCP Server │◄──►│  GNS3 Server    │

## 星数曲线

```mermaid
xychart-beta
    title "Wael-Rd/gns3-mcp-server 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 25 --> 28
    line [26, 27, 27]
```

2026-10-18 26 → 2026-10-30 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `e2152cf2d20f` · [字段定义](../../DATASET.md)*
