# elephantclock/private-email-agent

⭐ 3 · Kotlin · NOASSERTION · 推送 2026-10-21 · [GitHub](https://github.com/elephantclock/private-email-agent) · [官网](https://elephantclock.github.io/private-email-agent/) · 个人维护

**安卓端侧 AI 邮件代理：分类、摘要并起草回复**

面向 Android 的端侧邮件代理应用：通过 ML Kit GenAI API 调用 Gemini Nano（运行于手机 NPU/AICore）完成邮件重要性分类、线程摘要、回复起草、重写、校对与离线翻译；基于头部的规则引擎先行处理大部分邮件，AI 仅处理规则无法判定的部分。支持任意 IMAP/SMTP 账户与 Gmail，无服务器端，邮件不离开手机。可折叠屏适配（Flex mode 等 4 种布局）。需 Gemini Nano 支持的机型才有完整 AI 功能，其余机型仅规则排序。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 端侧运行 Gemini Nano（ML Kit GenAI：Prompt/Summarization/Rewriting/Proofreading），邮件不上传服务器
- 规则优先策略：头部规则（SPF/DKIM/DMARC、列表头等）处理大部分邮件，AI 仅兜底
- IMAP/SMTP 通用接入，服务器设置自动发现；任何修正自动转为规则
- 为 Galaxy Z Fold7 折叠屏设计，4 种屏幕形态布局适配

## 适用场景

- 在手机上本地完成邮件分类、摘要与回复起草
- 自动把营销邮件归入 Discarded 文件夹并每日摘要审阅
- 用自然语言描述自定义文件夹（如合作伙伴甄别）让 AI 按描述分拣
- 离线翻译外文邮件

## 场景标签

 · 领域:效率工具/邮件

## 证据(README 行号)

> L7: PEA (Private Email Agent) classifies, summarises and drafts replies to your email on your phone. It runs on the phon
> L70: - **On-device AI:** Gemini Nano through the ML Kit GenAI APIs (Prompt, Summarization, Rewriting, Proofreading), run

## 星数曲线

```mermaid
xychart-beta
    title "elephantclock/private-email-agent 星数(近 2 点)"
    x-axis ["2026-10-28", "2026-11-27"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-28 3 → 2026-11-27 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `9873b1e0ef8d` · [字段定义](../../DATASET.md)*
