# KnockOutEZ/wigolo

⭐ 5,566 · TypeScript · NOASSERTION · 推送 2026-11-25 · [GitHub](https://github.com/KnockOutEZ/wigolo) · [官网](https://wigolo.app) · 个人维护

**为 AI agent 提供本地网页搜索抓取的 MCP 服务器**

wigolo 以 MCP 服务器、REST API 与 TypeScript/Python SDK 形式，为 AI agent 提供统一的网页工具面：多引擎搜索（18 个直连适配器、排序融合与设备端重排）、分级别路由的 fetch（反爬时升级到无头浏览器）、crawl、结构化 extract、本地 cache、find_similar，以及 research 与 agent 两个合成类工具。搜索/抓取/抓取/抽取/缓存/相似查找完全无需 API key，数据留存于 ~/.wigolo/；research/agent 类工具可选接入 LLM key（含 ollama 本地路径）。需 Node ≥ 20，约 1.5 GB 磁盘，npx wigolo init 一键安装并可自动接线各编码 agent。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 十类工具经 MCP、REST（含 OpenAPI 契约）、CLI 交互 shell 与 SDK 多表面暴露
- 搜索/抓取/抽取/缓存/相似查找完全免 key，重排与嵌入在设备端运行
- init 命令可一次接线 claude-code、cursor、windsurf 等 9 种编码 agent 的 MCP 配置
- 结果带逐字节定位摘录、引用 ID 与可解释评分，弱结果自标记为 junk

## 适用场景

- 给编码 agent（Claude Code/Cursor 等）接入本地网页搜索与抓取
- 自托管 agent 通过 REST 或 SDK 调用网页工具
- 对指定站点做去样板的多页爬取与结构化数据抽取
- 无云依赖环境下让 agent 生成带引用的研究报告

## 场景标签

`网页抓取` `语义搜索` · 领域:效率与自动化

## 证据(README 行号)

> L32: wigolo gives an AI agent one surface for everything web-related: **search, fetch, crawl, extract, cache, find-simil
> L45: - **Supported agents** — `--agents` takes any of `claude-code` · `cursor` · `codex` · `gemini-cli` · `opencode` · `
> L46: - **Any other setup** — any MCP client, agent framework, or self-hosted agent registers `npx -y wigolo` in its own 

## 星数曲线

```mermaid
xychart-beta
    title "KnockOutEZ/wigolo 星数(近 26 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 5494 --> 5572
    line [5502, 5500, 5502, 5503, 5507, 5509, 5508, 5511, 5516, 5500, 5533, 5536, 5539, 5540, 5541, 5543, 5544, 5548, 5554, 5557, 5560, 5559, 5558, 5560, 5561, 5566]
```

2026-10-24 5,502 → 2026-11-26 5,566（+64）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 mid · 依据 README sha `54d654eeff16` · [字段定义](../../DATASET.md)*
