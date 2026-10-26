# GatekeeperZA/RKLLM-API-Server

⭐ 27 · Python · MIT · 推送 2026-08-25 · [GitHub](https://github.com/GatekeeperZA/RKLLM-API-Server) · [官网](https://github.com/GatekeeperZA/RKLLM-API-Server#readme) · 个人维护

**Rockchip NPU 上的 OpenAI 兼容 LLM 推理服务器，面向 Orange Pi**

为 RK3588/RK3576 NPU 单板机（如 Orange Pi 5 Plus）提供的 OpenAI 兼容 API 服务器：通过 ctypes 绑定 librkllmrt.so 直接调用 NPU 运行 .rkllm 模型，提供 /v1/chat/completions 等端点，作为 Open WebUI 的后端使用，实现无云依赖的本地推理。支持流式输出、KV 缓存增量与预热、RAG 检测与提示重组、Qwen3 类推理模型 <think> 解析、双模型视觉语言架构、Ollama API 兼容层、LoRA 运行时加载与 Prometheus 监控。限制：NPU 单次仅能加载一个模型，服务强制单 gunicorn worker，并发生成返回 503（排队等待默认 30 秒）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ctypes 直连 librkllmrt.so 在 RK3588/RK3576 NPU 上运行 .rkllm 模型
- OpenAI 兼容端点 + Anthropic Messages shim + Ollama API 兼容层
- KV 缓存增量模式与提示缓存预加载（多轮只预填充新消息）
- 双模型 VL 架构：文本模型与视觉模型同时加载，图像请求自动路由

## 适用场景

- 在 Orange Pi 5 Plus 等单板机上为 Open WebUI 提供本地 LLM 后端
- 家庭网络内私有运行 LLM，不依赖云服务
- 为 Home Assistant Assist 提供对话代理后端
- 在 NPU 上同时运行文本与视觉语言模型进行图文问答

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: **OpenAI-compatible API server for Rockchip NPU (RK3588/RK3576) running RKLLM models, designed as a drop-in backend 
> L16: - **Direct NPU access** via ctypes binding to `librkllmrt.so` (no subprocess overhead)
> L124: │  Open WebUI  │ ◄──────────────── │   api.py (Flask + gunicorn)      │

## 星数曲线

```mermaid
xychart-beta
    title "GatekeeperZA/RKLLM-API-Server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-26 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `b7b2a55d4424` · [字段定义](../../DATASET.md)*
