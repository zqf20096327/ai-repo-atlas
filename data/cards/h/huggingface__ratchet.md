# huggingface/ratchet

⭐ 772 · Rust · MIT · 推送 2026-09-24 · [GitHub](https://github.com/huggingface/ratchet) · 组织维护

**浏览器/原生跨平台 ML 推理工具包，GPU 加速**

面向 Web 优先场景的跨平台机器学习开发工具包，目标是在浏览器与原生环境提供 GPU 加速推理。设计原则为仅推理、仅 WebGPU/CPU 后端、支持量化、惰性计算与原地操作。提供 JavaScript API（异步加载模型并使用 IndexedDB 缓存），Rust crate 与 CLI 尚未发布。支持模型包括 Whisper、Phi 2 & 3、Moondream，计划支持 Gemini 2 2B。项目处于活跃开发阶段，可通过 Hugging Face Spaces 体验。

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

- JavaScript API：异步模型加载 + IndexedDB 缓存 + 进度回调
- 仅推理设计，后端限定 WebGPU/CPU，支持量化
- 支持 Whisper、Phi 2 & 3、Moondream 模型

## 适用场景

- 在网页应用中直接运行语音转录或语言模型推理
- 为现有生产应用集成浏览器端 GPU 加速的 AI 功能
- 通过 Hugging Face Spaces 在线体验浏览器内模型推理

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: A web-first, cross-platform ML developer toolkit
> L34: We want a toolkit for developers to make integrating performant AI functionality into existing production applicati

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/ratchet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 771 --> 773
    line [772, 772]
```

2026-10-18 772 → 2026-10-26 772（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `b35f30f3cc7b` · [字段定义](../../DATASET.md)*
