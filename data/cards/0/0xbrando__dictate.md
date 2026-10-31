# 0xbrando/dictate

⭐ 19 · Python · MIT · 推送 2026-10-28 · [GitHub](https://github.com/0xbrando/dictate) · 个人维护

**macOS 本地按键说话听写工具：Apple Silicon 离线语音转文字**

面向 macOS 用户的菜单栏听写应用：按住按键说话，松开后将文字粘贴到光标处。语音识别默认经 Core ML 在 Apple Neural Engine 上运行 Parakeet，可选 Qwen3-ASR、Parakeet MLX、Whisper Large V3 Turbo 等引擎；转写后由本地 LLM 修正语法、加标点，支持 12 种语言互译与多种写作风格。默认全程本地，无 API key，远程端点需显式开启。安装方式为 pip、Homebrew tap 或源码；需 macOS 14+ 与 Apple Silicon，ANE 引擎依赖一个 Swift 辅助二进制（缺失时回退 GPU 引擎）。也提供 OpenAI 兼容 localhost 后端以复用已有 LLM 服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 默认 ANE（Core ML）运行 Parakeet 的本地语音识别，多引擎可切换（Qwen3-ASR/Parakeet/Whisper）
- 本地 LLM 文本清理：语法、标点、8 种写作风格与 12 语言翻译
- 默认全离线：无 API key，远程 URL 被阻断需显式开启
- 可对接 OpenAI 兼容 localhost 服务器（vllm-mlx/LM Studio/Ollama）替代内置模型

## 适用场景

- 在任意应用里按住快捷键语音输入文字
- 让本地 LLM 自动整理口语转写的标点和格式
- 为 Claude Code 等 agent 框架配本地语音输入层

## 场景标签

`语音识别` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L16: - **Local speech recognition** accelerated by Apple Silicon
> L92: **The thing that sets Dictate apart.** Most dictation tools give you raw transcription. Dictate pipes through a loc
> L102: |**ANE / FluidAudio**|varies|25|Default — Parakeet TDT v3 through Core ML on Apple Neural Engine|

## 星数曲线

```mermaid
xychart-beta
    title "0xbrando/dictate 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-31 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `4a335ae160c1` · [字段定义](../../DATASET.md)*
