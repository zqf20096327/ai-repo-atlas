# truespar/paddock

⭐ 139 · Rust · NOASSERTION · 推送 2026-10-24 · [GitHub](https://github.com/truespar/paddock) · 组织维护

**Rust 原生推理服务器：NVIDIA 与 Apple Silicon 上运行开源模型**

用 Rust 编写的原生 AI 推理服务器，调度器、分页 KV cache、内存管理与 CUDA/Metal 内核均在仓库内实现，非封装其他引擎。提供 OpenAI 与 Anthropic 兼容 API，支持 GGUF 与 safetensors 权重及 FP8/NVFP4/MXFP4/Q8/Q4 等量化，覆盖文本、视觉、语音转写、说话人分离、嵌入、重排、表格预测、SAM 3 分割与 OCR 等模型。附带 Web Studio 用于下载、管理、并排比较模型。发行两个二进制（manager 与 runner），NVIDIA 平台仅需驱动；macOS 原生应用为预发布状态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | `idea` | |

## 能力要点

- 调度器、分页 KV cache 与 CUDA/Metal 内核均在仓库内原生实现
- OpenAI/Anthropic 兼容 API，含 Responses、Realtime WebSocket、MCP 端点
- GGUF + safetensors，FP8/NVFP4/MXFP4/Q8_0/Q4_K_XL 等量化，逐张量分发
- 内置 Web Studio：模型管理、并排比较（可与 OpenRouter 等云端端点对比）

## 适用场景

- 在单张 NVIDIA GPU 或 Apple Silicon 上自托管开源模型服务
- 以 OpenAI 兼容 API 支撑多个 agent 会话的长上下文高共享前缀负载
- 在 Studio 中并排比较本地模型与云端模型的表现
- 运行语音转写、表格预测、图像分割等多模态模型

## 场景标签

`推理引擎` `多模态` · 领域:感知与多模态

## 证据(README 行号)

> L11: AI inference server written in Rust, for NVIDIA GPUs and for Apple Silicon, with an OpenAI and
> L14: It is a native engine and NOT A WRAPPER - the scheduler, the paged KV cache, the memory
> L163: **Serving.** Paged KV cache, continuous batching with chunked prefill, radix

## 星数曲线

```mermaid
xychart-beta
    title "truespar/paddock 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 134 --> 140
    line [135, 138, 139]
```

2026-10-18 135 → 2026-10-25 139（+4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `5a4055a44a8f` · [字段定义](../../DATASET.md)*
