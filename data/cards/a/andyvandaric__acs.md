# andyvandaric/acs

⭐ 21 · PowerShell · 推送 2026-10-15 · [GitHub](https://github.com/andyvandaric/acs) · [官网](https://uikode.com/acs) · 组织维护

**本地自主多 Agent 编排系统：统一管理与调度 AI 编码代理**

以单一 acs 二进制提供的本地 Agent 运行环境与控制台：通过 MCP（stdio JSON-RPC 2.0、27 个核心工具）接入文件系统、浏览器自动化等能力，内置多账户 AI 网关、多提供方负载均衡代理、任务调度器与自动修复 watchdog、看板任务管理、会话与内存检查、自主 bug hunter 等。数据全部留在本地，但需商业许可激活后方可运行，Cockpit 启动于 127.0.0.1:20130。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一 acs CLI 管理服务、网关、MCP 服务器与会话
- MCP 原生集成：27 个核心工具与 stdio JSON-RPC 2.0 服务框架
- 多账户网关与多提供方负载均衡代理
- acs doctor 自检修复与调度器 watchdog

## 适用场景

- 统一管理多个 AI 编码代理的工作区、工具与规则
- 本地跑一套带看板和调度器的 Agent 运行环境
- 聚合多个 AI 提供方账户额度做负载均衡

## 场景标签

`多智能体` `编码 Agent` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L99: |`acs gateway`|Manage multi-account AI gateways|
> L100: |`acs router`|Control multi-provider load-balancing proxy|
> L107: |`acs mcp [list\|add\|remove\|serve]`|Manage Model Context Protocol (MCP) servers and tools|

## 星数曲线

```mermaid
xychart-beta
    title "andyvandaric/acs 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-30"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-30 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f69bfecb7393` · [字段定义](../../DATASET.md)*
