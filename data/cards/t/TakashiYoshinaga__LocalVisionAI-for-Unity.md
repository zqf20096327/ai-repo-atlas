# TakashiYoshinaga/LocalVisionAI-for-Unity

⭐ 13 · C# · MIT · 推送 2026-09-21 · [GitHub](https://github.com/TakashiYoshinaga/LocalVisionAI-for-Unity) · [官网](https://takashiyoshinaga.github.io/portfolio/) · 个人维护 · 中文 README

**Unity 离线视觉 AI 示例：安卓端用 Gemma 描述照片并问答**

面向 Unity 开发者的 Android 示例工程：将 Gemma 4 E2B（约 2.6 GB，另行下载）打包进 APK，通过 Google LiteRT-LM 在设备本地推理，提供相机图像描述、指定目标的文字/数字提取（替代固定 ROI 的 OCR 思路）与纯文本问答。包含 AR Foundation 与 WebCamTexture 两个示例工程及三个场景；构建目标仅限 Android ARM64（API 29+），可在 macOS/Windows Unity Editor 内直接运行。模型加载占用逾 2.5 GB 内存，推理需数秒至数十秒，答案不流式输出、文本场景无对话历史。

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

- 模型打包进 APK，完全离线，图像与提示不离开设备
- 自然语言指定目标替代固定 ROI 的文字/数字提取
- 可复用的 Packages/LiteRtLmUnity 包，可拷贝到其他 Unity 工程
- 构建时模型自动切分为 1 GiB 块放入 StreamingAssets，首启校验 SHA-256

## 适用场景

- 开发离线运行的安卓相机图像描述应用
- 在 AR 应用中用自然语言指定目标提取文字与数字
- 在 Unity Editor（macOS/Windows）内不接设备直接测试本地 LLM 推理

## 场景标签

`OCR` `多模态` · 领域:感知与多模态

## 证据(README 行号)

> L5: A **fully offline** Unity sample that analyzes Android camera images with Gemma. It uses Google's LiteRT-LM, with th
> L15: |Main features|Camera-image description, targeted text and number extraction, text-only Q&A|

## 星数曲线

```mermaid
xychart-beta
    title "TakashiYoshinaga/LocalVisionAI-for-Unity 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `9375774d7bc1` · [字段定义](../../DATASET.md)*
