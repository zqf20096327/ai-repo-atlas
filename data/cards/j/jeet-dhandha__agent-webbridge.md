# jeet-dhandha/agent-webbridge

⭐ 12 · JavaScript · MIT · 推送 2026-10-22 · [GitHub](https://github.com/jeet-dhandha/agent-webbridge) · [官网](https://jeet-dhandha.github.io/agent-webbridge/) · 个人维护

**让 AI agent 驱动本机已登录 Chrome 的 MCP 服务器**

面向 Claude Code、Cursor 等 MCP 客户端的开源浏览器自动化工具：通过本地 Node 守护进程与 MV3 Chrome 扩展，让 agent 在用户真实登录态的 Chrome 上执行导航、点击、填表、截图、网络抓取等 15 个工具操作。支持多 Chrome 配置文件、每标签页独立 DevTools 并行（profiles × tabs 并发），全部流量仅监听 127.0.0.1，无云端与遥测。提供 npm 全局安装、CLI、Node/Python SDK 与 MCP 注册表条目；平台支持 macOS 与 Windows，Linux 路径已接入但未测试。

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

- 驱动已登录的真实 Chrome，免去无头浏览器重登录/2FA 问题
- per-tab CDP 附件实现多标签并行，基准 5 标签 3.5s vs 串行 9.3s
- 15 个原生工具 + 状态查询，支持多 profile 并发
- 本地运行（127.0.0.1），MIT 开源，含 Node/Python SDK

## 适用场景

- 让 Claude Code/Cursor 等 agent 操作我已登录的网页账号
- 多账号并行抓取或填写网页表单
- 以已认证会话执行社区 recipe（如 Google SERP 提取）

## 场景标签

`浏览器自动化` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L10: > **WebBridge** (`agent-webbridge`): Drive **your real, logged-in Chrome** with Claude Code, Cursor and any MCP cli
> L48: `agent-webbridge` is a tiny Node daemon (one runtime dependency: `ws`) plus a clean-room MV3 Chrome extension. An a
> L137:   AI agent  ──HTTP POST /command──▶  router (127.0.0.1:10086)   routes by "profile"

## 星数曲线

```mermaid
xychart-beta
    title "jeet-dhandha/agent-webbridge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 11 --> 13
    line [12, 12]
```

2026-10-18 12 → 2026-10-29 12（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `9e7390ece54e` · [字段定义](../../DATASET.md)*
