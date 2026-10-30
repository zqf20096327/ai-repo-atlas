# priyankark/phonepi-mcp

⭐ 38 · TypeScript · MIT · 推送 2026-09-11 · [GitHub](https://github.com/priyankark/phonepi-mcp) · [官网](https://www.phonepimcp.com/) · 个人维护

**让 AI 助手远程操控手机的 MCP 服务器与配套应用**

由 MCP 服务器与手机配套应用组成的项目：通过 Model Context Protocol 让 Cursor、Claude Desktop 等 MCP 客户端以自然语言执行 23+ 种手机操作，包括联系人与短信管理、通话发起、剪贴板共享、通知、电池状态、定时提醒与远程查找手机。服务器本地自托管，应用与服务器经由本地网络或 VPN 连接，无第三方远程服务器；Android 1.0.1+ 支持后台连接，iOS 需保持应用前台。详细文档在 phonepimcp.com。

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

- 23+ 种手机直接操作（短信/通话/联系人/剪贴板/通知/电池等）
- 服务器本地自托管，应用与服务器经本地网络或 VPN 连接
- Android 支持后台服务并在网络切换后自动重连
- 短信采用手机端确认发送机制，composer 启动不代表送达

## 适用场景

- 通过 Cursor/Claude Desktop 用自然语言操作手机
- 跨设备共享剪贴板与内容
- 远程查看电池状态、定位查找手机
- 让 AI 助手管理联系人、提醒与定时器

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L1: # PhonePi MCP: Turn your phone into a toolbox for AI assistants using Model Context Protocol
> L3: A powerful MCP server and companion app that allows you to manage and control your phone remotely using natural lang

## 星数曲线

```mermaid
xychart-beta
    title "priyankark/phonepi-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-30"]
    y-axis "stars" 36 --> 39
    line [38, 37, 38]
```

2026-10-18 38 → 2026-10-30 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `75f481e214ff` · [字段定义](../../DATASET.md)*
