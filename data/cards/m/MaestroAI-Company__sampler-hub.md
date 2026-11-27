# MaestroAI-Company/sampler-hub

⭐ 3 · Rust · AGPL-3.0 · 推送 2026-11-17 · [GitHub](https://github.com/MaestroAI-Company/sampler-hub) · [官网](https://maestroai.company/sampler/) · 组织维护

**自托管同步枢纽：多设备同步 Opera 数据并共享本地 AI 模型**

运行在自有电脑上的小型自托管服务器：为配对的手机、桌面与浏览器同步对话、设置与 AI provider，每个用户以端到端加密的 profile 隔离（Argon2id + XChaCha20-Poly1305，SQLite 逐行加密）。枢纽可共享本机运行的 Ollama/LM Studio/llama.cpp 供所有设备调用，也可自行下载并运行 llama.cpp 模型（按机器自动选 CUDA/Vulkan/Metal/CPU 后端）。传输用 iroh QUIC 直连或中继，无需开端口；提供 Windows 安装包、macOS dmg 与 Linux 安装脚本，亦可从 Rust 源码构建。 许可为 GNU AGPL v3。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 端到端加密的多设备同步，枢纽不可读存储内容
- 共享本机 Ollama/LM Studio/llama.cpp 给所有配对设备（含外网访问）
- 枢纽可自行下载运行 llama.cpp GGUF 模型并自动选 GPU 后端
- iroh QUIC 直连/中继传输，无需开放端口

## 适用场景

- 在家自建服务器，让手机、桌面、浏览器共用同一套对话与模型
- 家庭多人合用一个枢纽，各自 profile 数据互不可见
- 把家里电脑上的本地模型暴露给自己的设备在户外使用

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: Sampler-Hub is a small self-hosted server that keeps your Opera devices in sync. Install it on a computer you own, p
> L7: - **Shared AI**: Ollama, LM Studio and llama.cpp running on the hub's computer can be used from every paired device,
> L8: - **Local models**: the hub can download and run llama.cpp models itself. It picks the GPU backend for you, and you 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `f6adcfeeefe5` · [字段定义](../../DATASET.md)*
