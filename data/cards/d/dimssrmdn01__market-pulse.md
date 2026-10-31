# dimssrmdn01/market-pulse

⭐ 14 · Python · 推送 2026-10-26 · [GitHub](https://github.com/dimssrmdn01/market-pulse) · [官网](https://dimss-market-pulse.streamlit.app/) · 个人维护

**双语宏观与金融市场仪表盘：行情追踪、FOMC 分析与 AI 鹰鸽评分**

面向金融观察者的 Streamlit 仪表盘，覆盖加密、外汇、股票实时行情、FOMC 会议日程、CPI/NFP 日历、Fed Wire RSS 与 Fed Funds 期货对 FOMC 决议的历史回测。AI 部分包括：对 FOMC 声明文本输出 -100 到 +100 鹰鸽评分（Groq API 上的 LLM）、关键词启发式鹰鸽标签、AI 市场复盘叙述。界面支持印尼语/英语切换；大部分功能无需 API key，新闻与 AI 功能需 Groq 与 Finnhub key。作者声明为教育与作品集项目，非投资建议。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 对 FOMC 声明输出 -100~+100 鹰鸽评分与解释
- Fed Funds 期货对 FOMC 决议的历史回测
- 多资产 6 个月滚动相关性热力图
- 印尼语/英语双语界面，核心功能零 API key 可用

## 适用场景

- 跟踪加密、外汇、股票与美联储政策日程
- 回测期货市场对 FOMC 决议的隐含预测准确率
- 粘贴 Fed 文本获取鹰鸽倾向评分

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L13: **Market Pulse** is a comprehensive, bilingual (ID/EN) financial dashboard designed to track crypto, forex, and sto
> L34: Powered by Llama-3.1 via Groq. Paste any FOMC statement or Fed speech excerpt to receive a -100 to +100 hawkish–dov

## 星数曲线

```mermaid
xychart-beta
    title "dimssrmdn01/market-pulse 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `0407dc3c38d7` · [字段定义](../../DATASET.md)*
