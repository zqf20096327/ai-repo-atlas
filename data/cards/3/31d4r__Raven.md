# 31d4r/Raven

⭐ 197 · Swift · MIT · 推送 2026-04-07 · [GitHub](https://github.com/31d4r/Raven) · 个人维护

**macOS/iOS 本地文档问答应用：上传文件后提问，全程设备内处理**

面向 Apple 平台用户的文档对话应用：上传图片、PDF、音频、视频等文件，应用进行文本提取、音频转录与视频文字提取，随后基于项目内容回答问题并生成摘要。AI 处理全部通过 Apple Foundation Models 在本地完成，数据不离开设备，AI 功能无需联网。要求 macOS 26 Tahoe 及以上、Xcode 26 构建，依赖 Vision/Speech/PDFKit 等系统框架与 GRDB.swift。项目自述处于活跃开发阶段，同时在 App Store 提供发布版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 支持图片、PDF、音频、视频的文本提取与音频转录
- 基于项目内容的问答与上下文分析
- 全部 AI 处理通过 Apple Foundation Models 在设备本地完成
- 提供 dmg/app 安装包或源码构建两种获取方式

## 适用场景

- 把文档集中到项目中提问和获取摘要
- 在不上传云端的前提下对敏感文档做问答
- 从音频和视频文件中提取文字并提问

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L14: Raven is an AI assistant app for macOS / iOS that transforms documents into interactive content. Upload files and g
> L16: **🔒 Privacy First**: All processing happens locally using Apple Foundation Models. Nothing is sent to servers or cl

## 星数曲线

```mermaid
xychart-beta
    title "31d4r/Raven 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 196 --> 198
    line [197, 197]
```

2026-10-18 197 → 2026-10-26 197（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `5f8f4d7ef28b` · [字段定义](../../DATASET.md)*
