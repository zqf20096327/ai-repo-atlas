# madroidmaq/mlx-omni-server

⭐ 745 · Python · MIT · 推送 2026-05-09 · [GitHub](https://github.com/madroidmaq/mlx-omni-server) · [官网](https://deepwiki.com/madroidmaq/mlx-omni-server/1-overview) · 个人维护

**Apple Silicon 上的本地推理服务器，兼容 OpenAI 与 Anthropic API**

基于 Apple MLX 框架的本地推理服务器，面向 Apple Silicon（M1/M2/M3/M4）Mac 用户。提供 OpenAI 与 Anthropic 双套兼容端点：聊天补全（工具调用、流式、结构化输出）、TTS、STT、图像生成、嵌入与模型管理；Anthropic 端点支持消息、工具与 thinking 模式。自动发现 HuggingFace 缓存中的 MLX 模型并按需下载加载，现有 OpenAI/Anthropic SDK 可直接接入。通过 pip 安装，需 Python 3.11+ 与 MLX 框架，仅限 Apple Silicon 硬件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 与 Anthropic 双 API 兼容端点
- 覆盖 Chat、TTS、STT、图像生成、嵌入的完整端点集
- MLX 模型自动发现、按需加载与自动下载
- 函数调用、结构化输出与 thinking 模式支持

## 适用场景

- 在 Mac 上本地运行模型并用现有 OpenAI/Anthropic SDK 接入
- 为本地开发提供 OpenAI 兼容 API 服务
- 在无外网环境下做语音转写、语音合成与文本生成

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: *Local AI inference server optimized for Apple Silicon*
> L12: **MLX Omni Server** provides dual API compatibility with both **OpenAI** and **Anthropic APIs**, enabling seamless 
> L20: - 🎯 **Complete AI Suite** - Chat, audio processing, image generation, embeddings

## 星数曲线

```mermaid
xychart-beta
    title "madroidmaq/mlx-omni-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 744 --> 746
    line [745, 745]
```

2026-10-18 745 → 2026-10-30 745（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `266d596b6f0b` · [字段定义](../../DATASET.md)*
