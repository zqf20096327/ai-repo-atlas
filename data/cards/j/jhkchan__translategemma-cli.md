# jhkchan/translategemma-cli

⭐ 22 · Python · MIT · 推送 2026-01-16 · [GitHub](https://github.com/jhkchan/translategemma-cli) · 个人维护 · 中文 README

**本地运行 Google TranslateGemma 翻译模型的命令行工具**

面向需要本地翻译的用户：封装 TranslateGemma 模型（4b/12b/27b），支持 55 种语言与可配置语言对（默认粤语↔英语）。推理后端可选本地 MLX（Apple Silicon）、PyTorch（CUDA/CPU）、vLLM 或 Ollama；首次运行下载模型并做 4-bit 量化转换。提供交互式 REPL、自动语种检测、direct/explain 两种输出模式与单次命令行翻译。限制：TranslateGemma 无专用 yue 语言码，粤语翻译用 zh-Hant-HK 替代；不同模型尺寸有相应内存要求。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多后端支持：本地 MLX/PyTorch、vLLM、Ollama
- 首次运行自动下载模型并 4-bit 量化（27b 约 54GB→15GB）
- 交互式 REPL，含自动语种检测与 /to、/mode、/backend 等命令
- 支持 TranslateGemma 全部 55 种语言，默认粤语↔英语

## 适用场景

- 在 Apple Silicon Mac 上离线做粤语与英语互译
- 通过命令行或 REPL 在 55 种语言间本地翻译文本
- 复用已有的 vLLM 或 Ollama 服务作为翻译推理后端

## 场景标签

 · 领域:自然语言处理/机器翻译

## 证据(README 行号)

> L3: Local translation powered by TranslateGemma, supporting 55 languages with configurable language pairs (default: Cant
> L9: - **Multiple backends** - Local (MLX/PyTorch), vLLM, or Ollama

## 星数曲线

```mermaid
xychart-beta
    title "jhkchan/translategemma-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `84678bac4883` · [字段定义](../../DATASET.md)*
