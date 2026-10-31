# lennyerik/crawl4ai-proxy

⭐ 34 · Go · 推送 2025-11-20 · [GitHub](https://github.com/lennyerik/crawl4ai-proxy) · 个人维护

**让 OpenWebUI 对接 crawl4ai 的 Docker 代理服务**

一个简单的代理服务器，以 Docker 容器形式运行，使 OpenWebUI 实例能够与 crawl4ai 实例交互，将 OpenWebUI 的网页搜索功能接入 crawl4ai 抓取能力，无需付费 API 服务。使用方式为：通过 compose.yml 部署 ghcr.io 镜像，运行 docker compose up -d 后，在 OpenWebUI 管理面板的 Web Search 设置中将 Web Loader Engine 设为 external，并填入代理地址与任意 API Key。面向自部署 OpenWebUI 与 crawl4ai 的用户。

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

- 以 Docker 容器方式运行，提供 ghcr.io 官方镜像
- 通过 external Web Loader 配置接入 OpenWebUI 网页搜索
- 避免为网页加载功能付费使用 API 服务

## 适用场景

- 自部署 OpenWebUI 时用 crawl4ai 替代外部网页加载 API
- 加速 OpenWebUI 的网页搜索内容抓取

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L1: # crawl4ai OpenWebUI proxy
> L2: This simple proxy server can be run in a docker container to let an OpenWebUI instance interact with a crawl4ai inst
> L3: This makes the OpenWebUI's web search feature a lot faster and way more usable without paying for an API service. 🎉

## 星数曲线

```mermaid
xychart-beta
    title "lennyerik/crawl4ai-proxy 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 32 --> 35
    line [33, 34, 34]
```

2026-10-18 33 → 2026-10-31 34（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4afe58a2ac4f` · [字段定义](../../DATASET.md)*
