# pisze-programy/openWhisper

⭐ 10 · Swift · Apache-2.0 · 推送 2026-09-02 · [GitHub](https://github.com/pisze-programy/openWhisper) · 个人维护

**macOS/iOS 端本地语音转文字应用，免隐私顾虑的听写与翻译工具**

macOS 菜单栏应用（iOS 端开发中），按住全局快捷键即可在任意应用中语音听写并自动粘贴。本地运行 Parakeet TDT 0.6B v3 模型完成语音识别（macOS 经 FluidAudio，iOS 转 Core ML 在 GPU/CPU 上运行），支持 25 种欧洲语言并带标点与数字规范化。可选接入 OpenRouter 进行 AI 格式改写（正式/随意/极简/简短）与翻译；历史按日分组、本地存储。安装方式为 Xcode 打开工程运行或脚本构建 DMG。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地 STT：Parakeet TDT 0.6B v3，支持 25 种欧洲语言
- 全局快捷键听写并自动粘贴到前台应用
- 可选 OpenRouter 接入实现 AI 格式化与翻译
- iOS 端完全离线模型（~480 MB）

## 适用场景

- 在任意应用中用快捷键快速语音输入文字
- 不希望语音数据上传云端的本地听写
- 将语音转文字后自动翻译成目标语言

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L89: |STT (macOS)|Parakeet TDT 0.6B v3 via FluidAudio|
> L90: |STT (iOS)|Parakeet TDT 0.6B v3 -> Core ML via parakeet-coreml-ios (vendored at `Packages/`)|
> L91: |AI formatting & translation|OpenRouter (optional, needs API key)|

## 星数曲线

```mermaid
xychart-beta
    title "pisze-programy/openWhisper 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-27"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-26 10 → 2026-11-27 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `a02ae65fbf41` · [字段定义](../../DATASET.md)*
