# xtekky/gpt4free

⭐ 66,893 · Python · GPL-3.0 · 推送 2026-10-18 · [GitHub](https://github.com/xtekky/gpt4free) · [官网](https://t.me/g4f_channel) · 组织维护

**给开发者的多提供方 LLM 聚合接入库，附 GUI 与 OpenAI 兼容 API**

社区项目，聚合多个可访问的提供方适配器，统一提供 Python 同步/异步客户端、浏览器 JS 客户端、本地 Web GUI，以及 FastAPI 实现的 OpenAI 兼容 REST API（Interference API）。支持图像/音频/视频媒体生成、本地推理后端接入，并内置 MCP 服务器（web_search/web_scrape/image_generation 三个工具，可接入 Claude Desktop）。部分提供方依赖 Chrome/Chromium 浏览器自动化或 cookies/HAR 凭据；Python 3.10+，提供 pip、Docker（full/slim）与 Windows exe 安装方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.7 天,年发版 100,268 位贡献者
- 涨星:近 1 天 **+5**(自 20261016 起算)
- 安装:pypi 包 `g4f` 月下载 71,487
- 平台:WINDOWS / MACOS / LINUX · 协议:OPENAI-API / MCP

## 能力要点

- Python/JS 客户端、本地 GUI 与 OpenAI 兼容 REST API 多形态接入
- 多提供方适配器，含媒体生成与本地推理后端
- 内置 MCP 服务器（stdio/HTTP 两种模式）暴露 web_search、web_scrape、image_generation
- 支持 x86_64 与 arm64 的 Docker full/slim 镜像

## 适用场景

- 用统一客户端切换多个 LLM 提供方
- 本地跑一个 OpenAI 兼容 API 供现有工具链调用
- 给 AI 助手配置 MCP 工具做搜索、抓取与图像生成

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L17: GPT4Free (g4f) is a community-driven project that aggregates multiple accessible providers and interfaces to make w
> L27: - FastAPI-based OpenAI-compatible API (Interference API).
> L251: - GPT4Free integrates many providers including (but not limited to) OpenAI-compatible endpoints, PerplexityLabs, G

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `220069f772b1` · [字段定义](../../DATASET.md)*
