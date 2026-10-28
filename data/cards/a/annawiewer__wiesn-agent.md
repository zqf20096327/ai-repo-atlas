# annawiewer/wiesn-agent

⭐ 29 · Python · MIT · 推送 2026-04-12 · [GitHub](https://github.com/annawiewer/wiesn-agent) · 个人维护

**监控 38 个慕尼黑啤酒节帐篷订位门户的 AI 代理，推送空位提醒**

面向啤酒节订位场景的监控与填单工具：定时（默认 30 分钟）扫描 38 个啤酒帐篷订位门户，发现晚市空位后通过 Apprise（ntfy/Telegram 等 130+ 渠道）推送通知，并可用 AI 预填订位表单（从不自动提交）。提供 Web 仪表盘（FastAPI + React）、MCP 服务器（15 个工具，可接入 VS Code Copilot、Claude Desktop、Cursor）与 CLI 三种使用方式。Agent 部分基于 Microsoft Agent Framework，采用 4 个专职 agent 加关键词 triage 路由；无 GITHUB_TOKEN 时聊天退化为关键词响应，监控功能仍可用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 扫描 38 个帐篷门户并经 Apprise 推送 130+ 渠道通知
- MCP 服务器暴露 15 个工具，可接入 Copilot/Claude Desktop/Cursor
- 基于 Microsoft Agent Framework 的 4 专职 agent + 关键词 triage 路由（德英双语）
- AI 预填订位表单但从不自动提交，需人工确认

## 适用场景

- 盯梢啤酒节帐篷晚市空位并及时收到手机推送
- 让 AI 代填订位表单，自己最终点击提交
- 把订位扫描与填单工具接入自己的 AI 助手（MCP）

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L10: AI-powered Oktoberfest reservation monitor — watches 38 beer tent portals, alerts you when slots open, and helps yo
> L234: > **Without `GITHUB_TOKEN`**, the dashboard chat falls back to keyword-based responses (scan, status, matches, por
> L144: ## 🤖 Agent Workflow (Optional — requires GITHUB_TOKEN)

## 星数曲线

```mermaid
xychart-beta
    title "annawiewer/wiesn-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-28 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `6dbff2e668d1` · [字段定义](../../DATASET.md)*
