# brendmung/AbodeLLM

⭐ 28 · 推送 2026-10-20 · [GitHub](https://github.com/brendmung/AbodeLLM) · 个人维护

**Android 端离线运行本地 LLM 的 AI 聊天助手**

面向 Android 设备的离线 AI 助手应用：模型推理全部在本机完成，聊天无需联网，提示词与对话不上传。支持 LLaMA 3.2、SmolLM、Gemma、Qwen3、DeepSeek R1 Distill 等多个模型家族及其尺寸变体，部分模型支持视觉与音频输入。内置 Expert Mode，可调节 temperature、top-k/top-p、KV-cache 与 token 上限，并支持导入外部 GGUF 格式模型。通过 Releases 下载 APK 安装，需 Android 9+、3GB 内存（推荐 6GB+）、1GB 存储空间。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 完全设备端推理，聊天无需联网
- 支持 10 余个模型家族，含视觉/音频多模态变体
- Expert Mode 可调 temperature/top-k/top-p/KV-cache/token 限制
- 可导入外部 GGUF 格式模型（含投影器）

## 适用场景

- 在无网络环境下用手机与本地模型对话
- 隐私敏感场景下让对话数据不出设备
- 按需下载不同尺寸与多模态能力的本地模型

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L6: AbodeLLM is an offline AI assistant built for Android devices, powered by various compact language models. It runs e
> L10: - **Offline AI Processing**: Chat without internet access.
> L11: - **Privacy First**: All prompts and conversations are processed on-device.

## 星数曲线

```mermaid
xychart-beta
    title "brendmung/AbodeLLM 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 26 --> 29
    line [27, 28, 28]
```

2026-10-18 27 → 2026-10-31 28（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `f08515378035` · [字段定义](../../DATASET.md)*
