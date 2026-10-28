# Sajadapp/Youtube-Trend-Analyzer

⭐ 41 · Python · 推送 2026-09-14 · [GitHub](https://github.com/Sajadapp/Youtube-Trend-Analyzer) · 个人维护

**监控 YouTube 趋势并用 LLM 分析、推送 Telegram 的异步机器人**

异步 Python 机器人：通过 YouTube RSS 与 Data API v3 双通道抓取趋势视频，提取病毒式传播指标，用 Gemini/DeepSeek 分析爆款钩子、情绪与内容策略，并将 HTML 分析卡片经 Telegram 长轮询机器人推送（波斯语界面）。使用 SQLite 本地缓存跳过已处理视频并追踪播放速度与配额状态；配置经 pydantic-settings 与 .env 管理，支持单次与定时轮询两种运行模式。面向希望自动获取 YouTube 趋势分析报告的内容创作者或运营者，需自备 YouTube API key、LLM key 与 Telegram bot token。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- RSS 优先、YouTube Data API v3 兜底的双抓取引擎
- Gemini/DeepSeek 分析爆款钩子、情绪与内容策略
- 多层解析器从 LLM 回复中恢复合法 JSON
- SQLite 缓存去重并追踪播放速度与 API 配额

## 适用场景

- 我想定时收到 YouTube 热门视频的 AI 策略分析报告
- 我想追踪自己领域视频的播放增速并分析爆款原因
- 通过 Telegram 自动接收格式化的趋势分析卡片

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L3: An asynchronous, production-ready Python framework that monitors YouTube video trends in real-time, extracts viral m
> L12: - **🧠 Fault-Tolerant LLM Analysis:** Gemini / DeepSeek analysis of viral hooks, sentiment, and content strategy.

## 星数曲线

```mermaid
xychart-beta
    title "Sajadapp/Youtube-Trend-Analyzer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-28 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `0b53ed597852` · [字段定义](../../DATASET.md)*
