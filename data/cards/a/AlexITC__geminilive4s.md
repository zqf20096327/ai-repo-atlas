# AlexITC/geminilive4s

⭐ 20 · Scala · MIT · 推送 2026-03-18 · [GitHub](https://github.com/AlexITC/geminilive4s) · [官网](https://alexitc.com/blog/2025-08-25-introducing-geminilive4s/) · 个人维护

**Scala 库：封装 Gemini Live API 实现实时语音对话**

为 Scala 提供的 Gemini Live API（音频）封装库，基于 google-genai SDK 构建，以 fs2 流形式读取麦克风音频输入并产出 Gemini 音频输出流。支持 Automatic Function Calling，允许 Gemini 调用 Scala 函数；默认封装保持简单，同时允许覆盖任意 google-genai 设置。通过 build.sbt 添加依赖安装，附有可用 scala-cli 直接运行的示例程序。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 google-genai SDK 的 Scala 封装，可覆盖任意底层设置
- 以 fs2 流实现音频输入/输出的实时对话
- 支持 Automatic Function Calling，Gemini 可调用 Scala 函数
- 提供麦克风到扬声器的最小示例与 scala-cli 可运行示例

## 适用场景

- 在 Scala 应用中接入 Gemini 实时语音对话
- 构建可通过自然语言调用 Scala 函数的语音助手
- 用 scala-cli 快速试用 Gemini Live 音频能力

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L3: A library for integrating real-time, conversational AI voice with Scala and the Google Gemini Live API.
> L7: The project's goal is to provide a Scala-friendly wrapper over google-genai SDK, being simple enough to get started 

## 星数曲线

```mermaid
xychart-beta
    title "AlexITC/geminilive4s 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `ee9f5f44ae83` · [字段定义](../../DATASET.md)*
