# Pushkinist/rMLX

⭐ 16 · Rust · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/Pushkinist/rMLX) · 个人维护

**Apple Silicon 上的 Rust 单二进制 MLX 推理服务器，OpenAI/Anthropic 兼容 API**

面向 Apple Silicon（M 系列，仅 Metal）的本地 LLM 推理后端：用 Rust 实现、无 Python 运行时、不读 GGUF，只加载 MLX 格式（mlx-community safetensors 布局）模型，通过 OpenAI /v1 与 Anthropic /v1/messages 兼容 HTTP API 提供文本生成、图像/音频输入、TTS、嵌入与工具调用；支持多权重量化格式与多种 KV cache 量化、投机解码、前缀缓存与多模型注册表。需先安装 Homebrew 的 MLX/mlx-c 后从源码构建（脚本/Homebrew tap/cargo 三种途径）。限制：无训练/LoRA 融合，无 MLX 转换命令，无 CUDA/ROCm/x86 路径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 与 Anthropic 兼容 HTTP API，覆盖文本/图像/音频输入、TTS、嵌入、工具调用
- 多种权重量化（2-8bit、mxfp4/8、nvfp4、ternary 等）与多族 KV cache 量化、SSD 分层
- 投机解码（MTP/DFlash/EAGLE-3）与自动前缀缓存
- 单二进制 Rust 构建，链接 Homebrew MLX，无 Python、无 GGUF

## 适用场景

- 在 Mac 上本地运行 MLX 格式模型并供 OpenAI/Anthropic API 客户端调用
- 本地跑 Whisper 转写或 Qwen3-TTS 语音输出
- 按需加载/卸载多个模型做本地多模型服务

## 场景标签

`推理引擎` `模型量化` · 领域:训练与推理

## 证据(README 行号)

> L16: A native, no-Python local LLM server for Apple Silicon. It serves
> L17: MLX-format models over OpenAI- and Anthropic-compatible HTTP APIs, so any
> L18: client of those APIs can use it as a local backend. One

## 星数曲线

```mermaid
xychart-beta
    title "Pushkinist/rMLX 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `505db5667c14` · [字段定义](../../DATASET.md)*
