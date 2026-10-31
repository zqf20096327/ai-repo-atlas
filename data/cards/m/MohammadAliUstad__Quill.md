# MohammadAliUstad/Quill

⭐ 18 · Kotlin · Apache-2.0 · 推送 2026-10-07 · [GitHub](https://github.com/MohammadAliUstad/Quill) · 组织维护

**Android 原生 EPUB 阅读器，内置防剧透的 AI 阅读问答助手**

用 Kotlin 与 Jetpack Compose 构建的原生 Android EPUB 阅读应用，阅读引擎基于 Readium SDK。内置 AI 伴读角色 Aira：电子书在设备端切块并用 bge-small-en-v1.5（ONNX Runtime）嵌入，存入 Room 与 FTS4 索引；提问时以向量+关键词混合检索（RRF 融合）并限制在已读章节内防剧透，相关片段经 Firebase Cloud Functions 调用 Gemini 生成回答、配图与朗读。限制：生成侧依赖 Firebase Blaze 计划与 Google 模型；Quill Pro 订阅限制每日 5/50 次提问。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 设备端索引与混合检索（bge-small + FTS4，RRF 融合）
- 防剧透锁：检索限定在读者当前进度内的章节
- 支持 Project Gutenberg 六万本与 Standard Ebooks 免费书源、EPUB 导入
- 段落转油画风插图、文字转语音、阅读统计与提醒

## 适用场景

- 在手机上阅读并就书中内容提问、解释难句、追踪角色
- 生成段落配图并保存到逐书画廊
- 从 Project Gutenberg / Standard Ebooks 下载免费公版书

## 场景标签

`文档问答` `语音合成` `图像生成` · 领域:内容生成

## 证据(README 行号)

> L18: Quill reimagines what a reading app can be. It pairs a carefully crafted EPUB reader with **Aira**, an AI reading c
> L141: Aira combines **on-device retrieval** with **server-side generation**. Your book is indexed on the phone; only the

## 星数曲线

```mermaid
xychart-beta
    title "MohammadAliUstad/Quill 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-31 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `13cd45265b1e` · [字段定义](../../DATASET.md)*
