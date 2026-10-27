# call518/MCP-OpenStack-Ops

⭐ 45 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/call518/MCP-OpenStack-Ops) · [官网](https://deepwiki.com/call518/MCP-OpenStack-Ops) · 个人维护

**面向 AI agent 的 OpenStack 运维 MCP 服务器（90+ 只读优先工具）**

基于 FastMCP 与 OpenStack SDK 构建的 MCP (Model Context Protocol) 服务器，向 Claude、Open WebUI 等 MCP 客户端暴露 90+ 个 OpenStack 项目管理与监控工具，覆盖 Nova 计算、Neutron 网络、存储、镜像、身份、Heat 与 Octavia 负载均衡。关键安全机制：默认锁定单项目作用域（每个工具校验 OS_PROJECT_NAME 资源归属），修改类 set_* 工具仅在 ALLOW_MODIFY_OPERATIONS=true 时注册，默认部署只读。官方测试目标为 OpenStack Epoxy (2025.1) 与 Dalmatian (2024.2)，旧版本需自行调整 openstacksdk 版本并重建 Docker 镜像。提供 stdio 与 streamable-http 两种传输。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 90+ 个项目作用域工具，覆盖计算/网络/存储/镜像/身份/Heat/Octavia
- 默认只读：set_* 工具仅在 ALLOW_MODIFY_OPERATIONS=true 时注册
- 批量与过滤式操作（实例/卷/网络/镜像/快照/密钥对）
- stdio 与 streamable-http 双传输，支持 Docker 部署与代理/堡垒机场景

## 适用场景

- 让 Claude 等 MCP 客户端直接查询和运维我的 OpenStack 项目
- 通过 AI agent 批量启停实例、管理卷与网络（需显式开启写权限）
- 监控 OpenStack 服务状态、资源利用率与配额

## 场景标签

 · 领域:云计算/DevOps 工具

## 证据(README 行号)

> L3: > **MCP OpenStack Operations Server**: A comprehensive MCP (Model Context Protocol) server providing OpenStack proje
> L22: - ✅ **Project-Scoped Operations**: Every tool enforces the configured `OS_PROJECT_NAME`, validating resource owners
> L24: - ✅ **90+ Purpose-Built Tools**: Broad coverage across compute, networking, storage, images, identity, Heat, and Oc

## 星数曲线

```mermaid
xychart-beta
    title "call518/MCP-OpenStack-Ops 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-27 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `80739839f4c7` · [字段定义](../../DATASET.md)*
