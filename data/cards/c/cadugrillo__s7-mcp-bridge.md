# cadugrillo/s7-mcp-bridge

⭐ 27 · TypeScript · MIT · 推送 2026-03-20 · [GitHub](https://github.com/cadugrillo/s7-mcp-bridge) · 个人维护

**连接 AI 代理与西门子 S7 PLC 的 MCP 服务器**

面向工业自动化的 MCP Server，通过西门子 PLC Web API 将 S7-1500/S7-1200 接入 AI 代理，使其能监控和控制工业设备。提供约 20 个工具：用户认证与权限读取、PLC 连通性检查、变量读写（Boolean/Number/String）、CPU 运行模式与系统时间管理、报警浏览与确认、诊断缓冲区浏览、CPU 备份等。通过环境变量配置多台 PLC（IP/名称/端口/传输方式 stdio 或 http-stream），支持 Node.js 源码运行与 Docker 容器部署，并给出 Claude Desktop 接入配置。

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

- 覆盖 PLC 变量读写、报警确认、诊断缓冲区浏览、CPU 备份等约 20 个工具
- 通过环境变量配置多台 PLC（IP/名称/端口）
- 支持 http-stream 与 stdio 两种传输方式，http-stream 模式带状态页
- 提供 Docker 镜像与 Claude Desktop 接入配置

## 适用场景

- 让 Claude 等 AI 代理直接读写西门子 S7 PLC 变量
- 通过代理浏览和确认工业设备报警与诊断信息
- 在 MCP 编排中统一管理多台 PLC 设备

## 场景标签

 · 领域:工业自动化/AI 基础设施

## 证据(README 行号)

> L3: **S7 MCP Bridge** is a MCP Server that connects AI agents to Siemens industrial PLCs (specifically S7-1500 and S7-12
> L104: ### 🖥️ Connecting with Claude Desktop

## 星数曲线

```mermaid
xychart-beta
    title "cadugrillo/s7-mcp-bridge 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26"]
    y-axis "stars" 25 --> 28
    line [26, 27, 27]
```

2026-10-18 26 → 2026-10-26 27（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c73869ae15bd` · [字段定义](../../DATASET.md)*
