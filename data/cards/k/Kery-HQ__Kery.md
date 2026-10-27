# Kery-HQ/Kery

⭐ 25 · TypeScript · Apache-2.0 · 推送 2026-08-25 · [GitHub](https://github.com/Kery-HQ/Kery) · [官网](https://www.kery.dev) · 组织维护

**用 AI agent 自动测试 Web 应用并生成截图证据**

面向 Web 开发者的自主测试平台：BFS 爬取应用生成路由/表单地图，路径规划 agent 生成步骤，Navigator agent 驱动真实 Playwright 浏览器执行流程，验证 agent 将每条声明判定为 verified/contradicted 并配带标注框与期望-实际说明的截图证据；Triage agent 去重、过滤误报并按类型/严重度分类输出 bug。无需编写选择器或脚本，支持认证流程，提供 MCP server（可从 Claude Code/Cursor 调用）、TypeScript SDK、REST API 与 SSE。LLM 可配 Anthropic/OpenRouter/OpenAI/Gemini 或任意 OpenAI 兼容端点，各 agent 角色可独立配置并按次跟踪 token 成本。安装途径包括 npx keryai 向导（生成 docker-compose 并启动服务）、手动 docker compose 或本地 Node 20+ + PostgreSQL + Redis 开发运行，另有托管云服务 app.kery.dev。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 声明级判定 verified/contradicted/not testable，附标注框与期望-实际截图证据
- BFS 爬取建图 + Navigator/Review/Verification/Triage 多 agent 流水线
- MCP server 提供 kery_scan 等 20+ 工具，可从 Claude Code/Cursor 等 IDE 内运行
- 支持 Anthropic/OpenRouter/OpenAI/Gemini 及任意 OpenAI 兼容端点，各 agent 角色独立配置
- agent 记忆：跨运行学习导航路径、记录误报与忽略区域

## 适用场景

- 提交 PR 后让 agent 自动跑通关键流程并拿到截图级验证结果
- 在 Claude Code/Cursor 里通过 MCP 直接触发扫描、测试与 bug 分诊
- 自动发现视觉/功能/UX 三类 bug 并按严重度分级
- 给已上线的 Web 应用做全站路由健康盘点

## 场景标签

`浏览器自动化` `多智能体` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L7:  AI agents that test your web app and prove what works — with annotated screenshot evidence.
> L15: Point Kery at your web app, pick an LLM provider, and let it loose. It drives a real browser through your flows, gr
> L63: **4. Verify** — A Verification Agent grades every claim against the recorded trace: **verified** needs an observed 

## 星数曲线

```mermaid
xychart-beta
    title "Kery-HQ/Kery 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `c76f1ea04737` · [字段定义](../../DATASET.md)*
