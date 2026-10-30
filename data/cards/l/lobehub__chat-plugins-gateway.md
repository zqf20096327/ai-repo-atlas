# lobehub/chat-plugins-gateway

⭐ 25 · TypeScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/lobehub/chat-plugins-gateway) · [官网](http://chat-plugins-gateway.lobehub.com) · 组织维护 · 中文 README

**LobeChat 插件网关后端服务：运行插件 Function Calling**

LobeHub 维护的后端网关服务，为 LobeChat 插件生态提供统一的执行入口：主 API POST /api/v1/runner 以 Vercel Edge Function 形式部署，接收插件名与参数并返回执行结果；从 LobeChat Plugins 仓库拉取插件索引（可通过 PLUGINS_INDEX_URL 环境变量自定义）。提供 PROD/DEV 两个公开实例，支持一键部署到 Vercel 自托管，本地开发使用 Bun 运行 git clone 后 bun install / bun dev。面向 LobeChat 插件生态的开发者与自托管用户。

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

- POST /api/v1/runner 以 Edge Function 运行 LobeChat 插件并返回结果
- 支持一键部署到 Vercel，可自定义插件索引 URL
- 与 LobeChat 插件索引、插件 SDK、插件模板构成配套生态

## 适用场景

- 自托管 LobeChat 插件网关以私有化运行插件
- 为 LobeChat 插件开发调试提供执行入口
- 自定义插件索引源运行自有插件列表

## 场景标签

 · 领域:LLM 基础设施/插件网关

## 证据(README 行号)

> L28: LobeChat Plugins Gateway is a backend service that provides a gateway for LobeChat plugins. We use vercel to deploy
> L94: - [@lobehub/chat-plugins-gateway][chat-plugins-gateway]: The LobeChat Plugins Gateway is a backend service that pro

## 星数曲线

```mermaid
xychart-beta
    title "lobehub/chat-plugins-gateway 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `460d21e3847f` · [字段定义](../../DATASET.md)*
