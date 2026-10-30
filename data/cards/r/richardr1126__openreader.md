# richardr1126/openreader

⭐ 550 · TypeScript · MIT · 推送 2026-10-29 · [GitHub](https://github.com/richardr1126/openreader) · [官网](https://openreader.richardr.dev) · 个人维护

**自托管友好的多格式文档朗读阅读器，支持同步高亮与有声书导出**

基于 Next.js 的文本转语音文档阅读服务器，读取 EPUB、PDF、DOCX、TXT、MD 五种格式，提供逐词同步高亮的跟读播放。关键机制：PP-DocLayoutV3（ONNX）做版面感知 PDF 解析，ONNX Whisper 做词级对齐，后台渐进生成音频并复用缓存；支持多 TTS 提供方（本地 Kokoro 无需 API key、OpenAI 兼容自托管服务及多家云 API）；可导出 M4B/MP3 有声书。提供 macOS/Windows/Linux 桌面应用与 Docker 部署两种形态，后端可选 SQLite/Postgres 与 S3 兼容存储。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五种文档格式的同步跟读朗读
- 多 TTS 提供方：本地 Kokoro 无需 API key，兼容 OpenAI 等云 API
- PP-DocLayoutV3 版面感知 PDF 解析与 ONNX Whisper 词级对齐
- M4B/MP3 有声书导出，复用播放缓存

## 适用场景

- 阅读 EPUB/PDF 等文档时边听边看跟读高亮
- 把文档导出为有声书离线收听
- 家庭或团队自托管部署多人使用的朗读服务

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L13: OpenReader is an open-source, self-host-friendly text-to-speech document reader built with Next.js for **EPUB, PDF,
> L40: - 🎯 **Multi-provider TTS** — Kokoro running locally with no API key, self-hosted OpenAI-compatible servers (Kokoro-

## 星数曲线

```mermaid
xychart-beta
    title "richardr1126/openreader 星数(近 8 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30"]
    y-axis "stars" 540 --> 551
    line [541, 544, 546, 547, 548, 549, 550, 550]
```

2026-10-18 541 → 2026-10-30 550（+9）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `5e104b01318a` · [字段定义](../../DATASET.md)*
