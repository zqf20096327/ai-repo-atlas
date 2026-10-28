# tinchak0207/aggregate-search

⭐ 19 · Python · MIT · 推送 2026-08-25 · [GitHub](https://github.com/tinchak0207/aggregate-search) · 个人维护 · 中文 README

**聚合 B站/GitHub/Reddit/网页等多平台搜索的命令行工具，带可选 AI 摘要**

Python 编写的跨平台聚合搜索工具：并行检索 B站（自动 WBI 签名、免登录）、GitHub、Reddit（arctic-shift 历史存档）、Bing 开放网页等默认源，可选接入 Tavily、Telegram、小红书（需配置 Key 或会话）。附独立 Reddit 挖掘器（意图/态度/趋势/高频短语分析）。AI 部分为可选功能：--transcribe 用 yt-dlp 提取 B站 AI 字幕/弹幕并经 Groq 或任意 OpenAI 兼容服务生成摘要，未配置时跳过。通过 git clone 源码加 pip 安装依赖运行，输出 Markdown/JSON。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- B站/GitHub/Reddit/开放网页四源免登录免 Key 直接可用
- Reddit 独立挖掘器：意图分类、态度极性、时间趋势、高频 n-gram
- --transcribe 提取 B站 AI 字幕/弹幕并接入 LLM 生成要点摘要
- 凭据经环境变量/本地配置解耦，支持 Markdown 与 JSON 输出

## 适用场景

- 一条命令同时搜索视频、代码仓、网页与社区讨论
- 调研产品时挖掘 Reddit 板块的用户声音与态度分布
- 把 B站搜索结果转成字幕全文与 LLM 摘要阅读

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L3: > 🚀 一站式跨平台智能聚合搜索引擎。支持 B 站、GitHub、开放网页、Reddit、Tavily AI、小红书、Telegram 等多源聚合，免登录优先、广度优先。
> L12: - 🎬 **视频转文字（yt-dlp 开源方案）**：`--transcribe` 自动提取B站官方 AI 字幕/弹幕，接入 LLM 生成要点摘要（Groq 免费推理），链接直接变结构化文字。
> L76:  - 未配置时跳过摘要，字幕照常输出。

## 星数曲线

```mermaid
xychart-beta
    title "tinchak0207/aggregate-search 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `40efe0dae0de` · [字段定义](../../DATASET.md)*
