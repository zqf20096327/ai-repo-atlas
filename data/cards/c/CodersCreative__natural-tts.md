# CodersCreative/natural-tts

⭐ 26 · Rust · MIT · 推送 2025-12-29 · [GitHub](https://github.com/CodersCreative/natural-tts) · 个人维护

**Rust 语音合成 crate：统一封装多种 TTS 引擎便于程序内调用**

面向 Rust 开发者的 Text-To-Speech 库，通过统一 API 封装多种 TTS 引擎：Parler TTS、Google Gtts、TTS-RS、MSEdge TTS、MetaVoice 与 Coqui TTS（Coqui 目前标注为测试特性）。README 为各引擎提供初始化与朗读的 Rust 代码示例，通过 Cargo 以 crate 形式引入项目使用。待办项包括新增 Piper TTS 支持与移除 pyo3 依赖，表明部分引擎经由 Python 绑定接入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 统一 Rust API 封装 6 种 TTS 引擎
- 各引擎附初始化与朗读的代码示例
- 跨 Linux/Windows/macOS 平台标注
- 计划新增 Piper TTS 支持并移除 pyo3 依赖

## 适用场景

- 在 Rust 程序中集成语音合成输出
- 按需切换不同 TTS 引擎而不用改业务代码
- 快速试验多个 TTS 引擎的合成效果

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L5: #### Natural TTS (natural-tts) is a rust crate for easily implementing Text-To-Speech into your rust programs.
> L11: ### Available TTS Engines / AIs:

## 星数曲线

```mermaid
xychart-beta
    title "CodersCreative/natural-tts 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-26 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `48988a782fe2` · [字段定义](../../DATASET.md)*
