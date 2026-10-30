# cryptopoly/ChaosEngineAI

⭐ 25 · Python · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/cryptopoly/ChaosEngineAI) · [官网](https://chaosengineai.com) · 个人维护

**本地开源权重模型的桌面运行台：发现/运行/对话/测速/生成图像视频**

面向发烧用户的本地 AI 工作站：Tauri+React 桌面壳搭配 Python 后端，驱动 llama.cpp GGUF、Apple MLX 与可选 vLLM 后端，在一个窗口内完成模型发现下载、Hugging Face 检查点转 MLX、暖池加载、OpenAI 兼容本地 API 服务、聊天（含工具调用与 MCP 客户端）、基准测试（吞吐/困惑度/任务准确率）以及 Stable Diffusion 图像与 DiT 视频生成。提供 DFlash/DDTree/MTPLX/TensorFold 投机解码与 TriAttention/TurboQuant KV 缓存压缩，支持插件系统与 LoRA 微调。README 自称开发中，预期存在粗糙边缘与版本间破坏性变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 单一应用覆盖发现/转换/服务/聊天/基准/图像视频生成全流程
- DFlash/DDTree/MTPLX/TensorFold 投机解码与 TriAttention/TurboQuant 缓存压缩
- OpenAI 兼容本地服务端与远程 provider 回退
- 内置 web 搜索/计算器/代码执行/文件读取 agent 工具与 stdio MCP 客户端

## 适用场景

- 在本机一站式管理和运行开源权重模型并对外提供 OpenAI 兼容 API
- 对比不同量化/缓存策略/投机解码配置下的吞吐与质量
- 本地生成 Stable Diffusion 图像与 DiT 视频模型视频
- 让模型在对话中调用工具与本地 MCP 服务器

## 场景标签

`推理引擎` `模型评测` `图像生成` `视频生成` · 领域:评测与运维

## 证据(README 行号)

> L21: ChaosEngineAI is a desktop control plane for running large language models locally. It pairs a fast Tauri + React s
> L40: - 🚀 **Server** mode exposing an OpenAI-compatible REST API for your other tools
> L85: - `llama.cpp` GGUF, Apple MLX, optional vLLM, plus remote OpenAI-compatible providers as fallbacks

## 星数曲线

```mermaid
xychart-beta
    title "cryptopoly/ChaosEngineAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `b6a51d6e0c2e` · [字段定义](../../DATASET.md)*
