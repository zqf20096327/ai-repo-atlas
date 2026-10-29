# zxcloli666/House-Research

⭐ 23 · TypeScript · MIT · 推送 2026-08-11 · [GitHub](https://github.com/zxcloli666/House-Research) · 个人维护 · 中文 README

**自动化房产挂牌监控：抓取 Avito/ЦИАН 并由 AI 分析推送 Telegram**

用 Deno 编写的房产监控系统：定时抓取 Avito（HTML 解析，独立 avito-parser 分支）与 ЦИАН（非官方 API，需代理 cookie），将挂牌数据存入 Deno KV，再用 AI 生成「划算/溢价」评级（考虑价格、基础设施、照片），拼合图片并按主题以 HTML 消息发布到 Telegram。文本分析走任意 OpenAI 兼容端点（OpenRouter/Together/Groq/自建 vLLM/Ollama），Gemini 单独用于多模态任务，支持多 API key 日限额自动轮换。提供 ghcr.io 容器与 Docker Compose 部署，配置分为 .env 与 conf/conf.yml 两个文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Avito HTML 解析 + ЦИАН 非官方 API 双数据源
- AI 生成划算/溢价评级，综合价格、基础设施与照片
- 任意 OpenAI 兼容端点 + Gemini 多模态（PDF/照片/搜索 grounding）
- 多 API key 日限额自动切换；ghcr.io 容器 + Docker Compose 部署

## 适用场景

- 自动监控 Avito/ЦИАН 房产挂牌并推送到 Telegram
- 让 AI 筛选划算房源，减少手动盯盘
- 在自有 VPS 上以 Docker 部署长期运行

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L9: > **House Research** — комплексная система, которая автоматически 📡 собирает объявления о недвижимости, анализирует 
> L16: |🤖 **ИИ‑оценка**|Генерация рейтинга «выгодно / переплата» с учётом цены, инфраструктуры и фото.|
> L54: Текстовый чат ходит в любой OpenAI-совместимый endpoint (OpenRouter,

## 星数曲线

```mermaid
xychart-beta
    title "zxcloli666/House-Research 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `606296de4b95` · [字段定义](../../DATASET.md)*
