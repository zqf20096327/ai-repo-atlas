# KolosalAI/kolosal-server

⭐ 15 · C++ · Apache-2.0 · 推送 2026-01-02 · [GitHub](https://github.com/KolosalAI/kolosal-server) · [官网](https://kolosal.ai) · 组织维护

**本地运行 LLM 的 C++ 推理服务器，提供 OpenAI 兼容 API**

基于 llama.cpp 构建的跨平台（Windows/Linux/macOS）LLM 推理服务器，提供 OpenAI 兼容的 chat completions 端点（含流式 SSE 响应）、多模型同时加载与管理、惰性加载、API key 认证与限流、TPS/TTFT 实时指标。内置 FAISS 向量库（可选 Qdrant 后端）支持 RAG 检索，支持 CUDA/Vulkan GPU 加速。主要面向自建本地推理服务的开发者，安装以源码编译为主（CMake），无现成包管理器分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 兼容 API 端点，含流式 SSE 响应
- 多模型同时加载、惰性加载与动态 engine 管理
- 内置 FAISS 向量库（可选 Qdrant 后端）支持 RAG 检索
- API key 认证、限流与 TPS/TTFT 实时指标

## 适用场景

- 在自有设备上离线运行 GGUF 模型并通过 OpenAI 兼容 API 调用
- 同一服务器上加载管理多个模型并监控推理性能
- 以本地服务替代云端 API 做开发与测试

## 场景标签

`推理引擎` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L3: A high-performance inference server for large language models with OpenAI-compatible API endpoints. Now available fo
> L14: - 🚀 **Fast Inference**: Built with llama.cpp for optimized model inference

## 星数曲线

```mermaid
xychart-beta
    title "KolosalAI/kolosal-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b5983a265a72` · [字段定义](../../DATASET.md)*
