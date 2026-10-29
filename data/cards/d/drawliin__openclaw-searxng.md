# drawliin/openclaw-searxng

⭐ 20 · TypeScript · 推送 2026-10-10 · [GitHub](https://github.com/drawliin/openclaw-searxng) · 个人维护

**OpenClaw 插件：将 web_search 工具接到自托管 SearXNG**

为 OpenClaw agent 框架提供的可选 web_search 工具插件：把搜索请求转发到本机自托管的 SearXNG 实例，由其查询外部搜索引擎，无需付费搜索 API key。包含 TypeScript 插件源码、绑定 127.0.0.1:8080 的 Docker Compose 配置和一个 HTTP 客户端；需 Node.js 24.16+/26.1+、npm 与 Docker，并在 openclaw.json 中注册路径并将工具加入 allowlist。README 声明它不是离线搜索引擎，也不对上游搜索引擎提供隐私保证；返回结果上限 10 条。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过自托管 SearXNG 免 API key 实现 web_search 工具
- 提供绑定 localhost 的 Docker Compose 配置与默认引擎设置
- 工具以 optional 注册，需显式加入 agent 工具 allowlist
- 支持 query/count(1-10)/language/country/freshness 参数

## 适用场景

- 给 OpenClaw agent 增加免费的网页搜索能力
- 不想购买搜索 API 订阅时用自托管实例替代
- 本地开发环境跑通 SearXNG 搜索工具链

## 场景标签

 · 领域:AI agent 工具/搜索集成

## 证据(README 行号)

> L5: An OpenClaw plugin that connects an **optional `web_search` tool** to a self-hosted SearXNG instance. Search request
> L46: The plugin calls `registerTool(..., { optional: true })`, so merely loading it is **not enough**; it must also be a

## 星数曲线

```mermaid
xychart-beta
    title "drawliin/openclaw-searxng 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `973ac6551188` · [字段定义](../../DATASET.md)*
