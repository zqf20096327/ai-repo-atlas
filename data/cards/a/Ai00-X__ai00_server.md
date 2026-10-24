# Ai00-X/ai00_server

⭐ 621 · Rust · MIT · 推送 2026-06-09 · [GitHub](https://github.com/Ai00-X/ai00_server) · [官网](https://ai00-x.github.io/ai00_server/) · 组织维护 · 中文 README

**基于 Vulkan 的 RWKV 推理 API 服务器，兼容 OpenAI 接口**

基于 web-rwkv 引擎的 RWKV 语言模型推理 API 服务器，面向需要自建 LLM 服务的开发者。通过 Vulkan 实现并行并发批量推理，可在支持 Vulkan 的 GPU（含 AMD 显卡与核显）上加速，无需 PyTorch/CUDA 运行环境。API 输入输出遵循 OpenAI 规范，提供 chat/completions/embeddings 等端点与开箱即用的 WebUI（端口 65530）。支持 int8/NF4 量化、LoRA、BNF 约束采样，仅接受 .st（Safetensors）格式模型，.pth 需转换。提供预编译可执行文件，也可从 Rust 源码编译。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Vulkan 的并行并发批量推理，不依赖 CUDA/PyTorch
- API 兼容 OpenAI ChatGPT 接口规范（chat/completions/embeddings）
- BNF 采样可约束输出格式（如指定字段的 JSON）
- 支持 int8/NF4 量化、LoRA 与热切换的 tuned initial states

## 适用场景

- 在 AMD 显卡或核显上本地部署 RWKV 模型服务
- 用 OpenAI 兼容接口接入现有客户端调用本地 RWKV
- 约束模型输出固定 JSON/markdown 格式

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L14: `AI00 RWKV Server` is an inference API server for the `RWKV` language model based upon the `web-rwkv` inference eng
> L131: The API service starts at port 65530, and the data input and output format follow the Openai API specification.

## 星数曲线

```mermaid
xychart-beta
    title "Ai00-X/ai00_server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 620 --> 622
    line [621, 621]
```

2026-10-18 621 → 2026-10-24 621（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `b41824eeaafd` · [字段定义](../../DATASET.md)*
