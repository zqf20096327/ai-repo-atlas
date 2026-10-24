# fabriziosalmi/UglyFeed

⭐ 321 · Python · AGPL-3.0 · 推送 2026-10-22 · [GitHub](https://github.com/fabriziosalmi/UglyFeed) · [官网](https://fabriziosalmi.github.io/UglyFeed/) · 个人维护

**用 LLM 抓取、聚合、改写并发布 RSS 订阅源的应用**

面向 RSS 内容处理的应用：从配置的源抓取订阅条目，按相似度聚合，经 LLM API 改写（支持翻译、后置审核过滤），保存为 JSON 并转换为合法 RSS XML，可通过内置 HTTP 服务器、GitHub/GitLab 部署等方式供 RSS 阅读器订阅。提供 Streamlit Web UI 与内容质量评估脚本。支持 OpenAI、Ollama、Groq、Anthropic、Google Gemini 等 API 及任意 OpenAI 兼容服务端。以 Docker 镜像、pip 包或源码分发，AGPL3 许可。README 附滥用风险免责声明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- RSS 抓取、相似度聚合、LLM 改写、XML 输出与 HTTP 服务的完整流水线
- 支持 OpenAI/Ollama/Groq/Anthropic/Gemini 等多种 LLM API 及 OpenAI 兼容服务端
- Streamlit Web UI 配置与一键顺序执行脚本
- 改写后的 XML 可部署到 GitHub/GitLab CDN 供阅读器订阅

## 适用场景

- 把我关注的多源 RSS 聚合成一个经 LLM 改写摘要的个性化订阅源
- 将国际资讯自动翻译成母语后通过 RSS 阅读
- 聚合并汇总品牌相关报道供营销团队跟踪

## 场景标签

`网页抓取` `AI 写作` · 领域:效率与自动化

## 证据(README 行号)

> L3: UglyFeed is a **simple** application designed to **retrieve**, **aggregate**, **filter**, **rewrite**, **evaluate** 
> L11: - ✨ Rewrite content using LLM API

## 星数曲线

```mermaid
xychart-beta
    title "fabriziosalmi/UglyFeed 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 320 --> 322
    line [321, 321]
```

2026-10-18 321 → 2026-10-24 321（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `35001b46bc1c` · [字段定义](../../DATASET.md)*
