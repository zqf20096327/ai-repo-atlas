# Skull-boy/Finley

⭐ 23 · Python · MIT · 推送 2026-10-11 · [GitHub](https://github.com/Skull-boy/Finley) · 个人维护

**Telegram 上的 AI 金融助理：实时行情、基本面与主动提醒**

Telegram 原生 AI 金融助手：以 Gemini 为模型层，接入 Finnhub、yfinance、SEC EDGAR 实时数据，提供实时报价、市场总览、财报日历、公司基本面与 SEC 文件检索、多公司对比、观察清单与价格提醒、按用户时区的晨报简报；支持语音转录、PDF 分析与图表图像识别。语义记忆用 Qdrant（BM25 稀疏+稠密 RRF 混合检索，MongoDB 兜底），Gemini 多密钥轮换扩展免费额度，全部组件可在免费套餐上运行；本地部署需 Docker 启动数据库并配置 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Gemini 多密钥轮换网关，429 限速冷却与重试退避
- Qdrant 混合检索语义记忆（稀疏+稠密 RRF 融合，MongoDB 兜底）
- 实时行情/基本面/SEC 文件/财报日历/分析师评级等数据能力
- 语音转录、PDF 分析、金融图表模式识别的多模态输入

## 适用场景

- 在 Telegram 里查询股票行情、基本面和 SEC 文件
- 跟踪观察清单并接收价格提醒与个性化晨报
- 发送语音或 PDF 研报让 AI 分析并提取要点

## 场景标签

`AI 助手` `金融量化` · 领域:对话与助手

## 证据(README 行号)

> L5: Finley is a Telegram-native AI assistant that pairs Gemini with real-time data from Finnhub, yfinance, and SEC EDGAR
> L142: ## 📊 What Finley Can Do

## 星数曲线

```mermaid
xychart-beta
    title "Skull-boy/Finley 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 21 --> 24
    line [22, 23, 23]
```

2026-10-18 22 → 2026-10-30 23（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `aaaf9ecf97c0` · [字段定义](../../DATASET.md)*
