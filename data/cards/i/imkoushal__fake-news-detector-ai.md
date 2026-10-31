# imkoushal/fake-news-detector-ai

⭐ 14 · Python · NOASSERTION · 推送 2026-08-31 · [GitHub](https://github.com/imkoushal/fake-news-detector-ai) · 个人维护

**面向普通用户的多渠道假新闻检测系统（Web/Telegram/Android）**

VerifAI 通过两层机制检测虚假新闻：一是 5 模型投票集成（LR/RF/SGD/SVC/LightGBM，TF-IDF + 20 个自定义元特征）做文体分析；二是 RAG 管线，经 GNews 获取实时新闻、注入 Groq LLM 提示词交叉核验事实，语音输入经 Groq Whisper 转录。交付形态为 Web 应用、Telegram Bot 与 Capacitor 打包的 Android APK。限制：README 自述随机切分的 94.77% 准确率因数据泄漏偏高，分组切分待做；10 条手写新样本上约 70% 准确率。依赖 Groq/GNews 等外部 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 模型投票集成 + TF-IDF/20 个元特征的文体分析
- GNews 实时新闻 + Groq LLM 的 RAG 事实核验管线
- Web / Telegram Bot（含语音转写）/ Android APK 三渠道交付
- 集成 Google Fact Check、Safe Browsing、80+ 来源信誉库与印度诈骗模式扫描

## 适用场景

- 转发消息到 Telegram Bot 秒级获得事实核查结论
- 在 Web 仪表盘批量分析（最多 50 篇）并对比两篇文章
- 上传音频文件或语音输入进行语音转录后核查

## 场景标签

`RAG` `语音识别` · 领域:知识与检索

## 证据(README 行号)

> L30: 1. **Linguistic Analysis (ML):** A 5-model Voting Ensemble trained on 100,000+ articles detects the *writing style*
> L31: 2. **Factual Verification (RAG):** A Retrieval-Augmented Generation pipeline queries live news via GNews, injects t

## 星数曲线

```mermaid
xychart-beta
    title "imkoushal/fake-news-detector-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `89e2e58eef5c` · [字段定义](../../DATASET.md)*
