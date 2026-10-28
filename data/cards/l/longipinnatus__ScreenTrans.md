# longipinnatus/ScreenTrans

⭐ 24 · Kotlin · GPL-3.0 · 推送 2026-06-01 · [GitHub](https://github.com/longipinnatus/ScreenTrans) · 个人维护 · 中文 README

**Android 屏幕实时 OCR 翻译工具，可接入自定义 LLM API**

面向 Android 用户的屏幕翻译应用：截取屏幕后用内置 PaddleOCR 轻量化模型（简/繁中、英、日，可加载自定义 ONNX 模型）识别文字，再经 OpenAI API 协议接口调用大模型翻译，默认预置 DeepSeek 参数。支持竖排文本、区域选择与全屏两种模式、流式输出、自定义 Prompt 与术语表、Token 用量统计、按尺寸与正则过滤文本、悬浮层覆盖显示与自动复制。项目自述尚处早期阶段，通过悬浮球操作，需悬浮窗与屏幕录制权限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 内置 PaddleOCR 轻量化模型，支持加载自定义 ONNX 模型
- 经 OpenAI API 协议接入自定义 Endpoint，默认预置 DeepSeek 参数
- 支持中日文竖排文本识别与流式输出
- 可自定义翻译 Prompt、术语表并按正则过滤无关文本

## 适用场景

- 玩外文游戏或阅读外文漫画时实时翻译屏幕文字
- 通过自定义 API Endpoint 与 Prompt 适配不同翻译场景
- 统计 API Token 用量以估算成本

## 场景标签

`OCR` · 领域:感知与多模态

## 证据(README 行号)

> L7: 一款支持自定义大模型 API 接口的开源 Android 屏幕 OCR 实时翻译工具。
> L22: * **多模型支持**：内置 PaddleOCR 轻量化 OCR 模型（支持简/繁中、英、日），并支持加载自定义 PaddleOCR ONNX 模型，满足高精度识别或特定语言适配需求（正在适配中）。
> L26: * **标准 API 接入**：支持 OpenAI API 协议接口，兼容自定义 Endpoint。

## 星数曲线

```mermaid
xychart-beta
    title "longipinnatus/ScreenTrans 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-28 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `3301ed3247fa` · [字段定义](../../DATASET.md)*
