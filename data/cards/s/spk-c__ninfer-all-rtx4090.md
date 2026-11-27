# spk-c/ninfer-all-rtx4090

⭐ 3 · C++ · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/spk-c/ninfer-all-rtx4090) · [官网](https://spk-c.github.io/ninfer-all-rtx4090/) · 个人维护

**RTX 4090 专用本地 LLM 推理引擎，Windows 便携版**

面向 NVIDIA RTX 4090（24 GB，SM89）的 C++/CUDA 本地 LLM 推理引擎，由 NInfer-all 独立分叉维护，提供便携 Windows 二进制，无需本地编译 CUDA。支持 OpenAI 与 Anthropic 兼容 API、CLI 启动配置、DFlash2/MTP 投机解码、GGUF 转换的 .ninfer 量化工件、量化 KV 缓存与前缀缓存；内置只读浏览器监控面板展示 GPU 传感器、吞吐与 KV 占用。模型支持继承自上游，并非所有模型都能放入 24 GB 显存；Apache-2.0 许可，再分发的 CUDA 库遵循 NVIDIA 条款。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-24g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 原生 sm_89 CUDA 13.4 内核与便携 Windows 构建，免本地编译
- OpenAI/Anthropic 兼容 API 及模型专用启动配置
- DFlash2、MTP 投机解码与 GGUF 衍生的 IQ3_S/IQ4_XS 量化工件
- 内置只读浏览器监控面板：GPU 传感器、吞吐、DFlash2 接受率、KV 占用

## 适用场景

- 在单张 RTX 4090 上本地部署量化 27B 级模型并开放兼容 API
- 为本地编码 Agent 与聊天客户端提供 127.0.0.1 本地推理后端
- 在浏览器中监控本地推理吞吐、显存与请求状态
- 在 RTX 4090 上复现长上下文解码吞吐基准

## 场景标签

`推理引擎` `模型量化` `LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L3: **Run local large language models on NVIDIA GeForce RTX 4090 (24 GB) with native Ada Lovelace SM89 CUDA kernels, a p
> L24: |Local LLM serving|OpenAI- and Anthropic-compatible APIs, CLI and model-specific launch profiles|
> L186: **Is NInfer faster than llama.cpp, Ollama or vLLM?** No universal ranking is established by the published RTX 4090


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `a175213dbba5` · [字段定义](../../DATASET.md)*
