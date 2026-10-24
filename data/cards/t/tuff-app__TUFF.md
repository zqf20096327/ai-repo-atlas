# tuff-app/TUFF

⭐ 61 · Swift · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/tuff-app/TUFF) · [官网](https://tuff-app.github.io/) · 个人维护

**Apple Silicon Mac 本地 LLM 聊天应用，可从 SSD 流式运行超大 MoE 模型**

SwiftUI 桌面应用加自研 Swift/Metal 推理引擎，在 Apple Silicon Mac 上本地运行 Qwen、Gemma、GPT-OSS 等语言模型。核心机制：将 MoE 模型的专家保留在 SSD 上，每个 token 仅读取所需专家，使 16 GB 内存的 MacBook 可运行 111 GB 的模型。功能含聊天（推理/Markdown/附件）、Web 与本地文件夹搜索（默认关闭）、内置基准测试与排行榜、本地 OpenAI 兼容服务器及 tuff 命令行。限 Apple Silicon、macOS 15+，未公证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MoE 专家从 SSD 流式读取，16 GB 内存可运行 111 GB 模型
- 自研 Swift/Metal 推理引擎，非 MLX 或 llama.cpp
- 本地 OpenAI 兼容 Background API 服务器与 tuff CLI
- 内置基准测试并可分享至排行榜

## 适用场景

- 在小内存 Mac 上本地运行超大参数 MoE 模型
- 离线聊天，数据不出本机（除非开启 Web 搜索）
- 给本地 agent 提供兼容 OpenAI API 的推理服务

## 场景标签

`聊天机器人` `推理引擎` `模型评测` · 领域:对话与助手

## 证据(README 行号)

> L15: TUFF runs language models on Apple Silicon Macs. The app is SwiftUI and the
> L19: **Qwen3.8 Flash Next is a 111 GB model, and TUFF runs it on a 16 GB MacBook
> L20: Air.** TUFF keeps a mixture-of-experts model's experts on the SSD and reads
> L51: - **Chat** with reasoning, Markdown, math, and image and file attachments.


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `5deda4a12275` · [字段定义](../../DATASET.md)*
