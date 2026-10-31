# jayeshmahapatra/TranslateOCRApp

⭐ 14 · Kotlin · MIT · 推送 2026-06-05 · [GitHub](https://github.com/jayeshmahapatra/TranslateOCRApp) · 个人维护

**安卓拍照取词翻译应用：离线 OCR 瑞典语/德语译英文**

Android 应用，使用相机拍摄含瑞典语或德语文本的图片，基于 Google ML Kit 完成 OCR 文字提取、语言识别与翻译，将英文译文模糊覆盖回原图显示；CameraX 负责相机功能。首次使用需联网下载翻译模型，之后模型存储在本地。可通过 releases 下载 APK 或用 Android Studio 自行构建。同时是一篇博客教程的配套仓库。

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

- Google ML Kit 驱动的 OCR、语言识别与翻译流程
- 翻译模型下载后本地存储，支持离线翻译
- 将译文模糊覆盖原始文字叠加显示在图片上

## 适用场景

- 拍下瑞典语/德语标牌海报，直接看到英文译文
- 出国旅行时离线理解外文印刷文本

## 场景标签

`OCR` · 领域:感知与多模态

## 证据(README 行号)

> L3: TranslateOCRApp is an Android application that allows users to click pictures of Swedish and German text and transla
> L4: them into english. The app leverages Google ML-Kit for ML functionalities like OCR, Language identification and Tran

## 星数曲线

```mermaid
xychart-beta
    title "jayeshmahapatra/TranslateOCRApp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `1025218c054d` · [字段定义](../../DATASET.md)*
