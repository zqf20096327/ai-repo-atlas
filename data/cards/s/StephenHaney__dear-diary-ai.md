# StephenHaney/dear-diary-ai

⭐ 106 · TypeScript · MIT · 推送 2026-03-10 · [GitHub](https://github.com/StephenHaney/dear-diary-ai) · [官网](https://deardiary.ai) · 个人维护

**将日记文字实时转化为情绪音乐与动画的 Web 应用**

Magenta/Gray Area ML 音乐黑客松获奖项目：用户在网页中逐字输入日记，VADER.js 对文本做情感分析得出 -1.0 到 +1.0 的分数，再用 Magenta MusicVAE 预训练模型在预制的欢快/悲伤两段旋律之间插值，生成随情绪变化的音乐，同时逐步显现 SVG 树与飞鸟动画。条目经 Google Firestore 持久化，可重放与分享到 Twitter/链接。作者自述 VADER 单维情感分数是局限。技术栈为 Next.js + yarn，附旋律生成与 MIDI 转换说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- VADER.js 逐词情感分析输出 -1.0~+1.0 分数
- MusicVAE 在欢快/悲伤旋律间按情绪插值生成音乐
- Google Firestore 保存条目，支持重放与 Twitter/链接分享
- 输入的标点、大写、删除等操作会改变音乐

## 适用场景

- 通过写日记配即时生成的音乐来记录和觉察情绪
- 以音乐创作方式缓解压力、练习正念
- 把日记与生成的歌曲分享给他人

## 场景标签

 · 领域:创意AI/音乐生成

## 证据(README 行号)

> L17: **Sentiment Analysis**
> L21: We use Google’s Magenta MusicVAE pre-trained model to interpolate between two pre-composed melodies—one happy, one 

## 星数曲线

```mermaid
xychart-beta
    title "StephenHaney/dear-diary-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 105 --> 107
    line [106, 106]
```

2026-10-18 106 → 2026-10-25 106（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `42194c9e0e57` · [字段定义](../../DATASET.md)*
