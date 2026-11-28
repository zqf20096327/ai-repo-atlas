# tomDeprez/Tor6IA

⭐ 4 · Go · MIT · 推送 2026-11-27 · [GitHub](https://github.com/tomDeprez/Tor6IA) · [官网](https://github.com/tomDeprez/Tor6IA/releases/latest) · 个人维护 · 中文 README

**P2P 共享闲置电脑运行开源 LLM，赚积分换更大模型**

一个点对点网络：用户机器为他人运行开源 LLM 赚取积分，再用积分调用网络上（含超出本机显存/内存的）模型。单文件安装、自动装 Ollama 与模型，无账号，本机密钥即身份。机制上：端到端加密（X25519/AES-256-GCM），公共哈希链签名账本、每节点周期审计；支持多机分块协作托管大模型，OpenAI 兼容 API 供现有客户端接入。文本-only，不含图像与 tool calls。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单文件安装并自动装 Ollama 与适配本机的模型
- OpenAI 兼容 API（localhost:7606/v1），积分制支付
- 公共哈希链签名账本，tor6ia audit 可手动审计
- 模型按约 1GB 层块拆分，多机协作运行超出单机容量的模型

## 适用场景

- 用自己的 GPU 空闲算力为他人推理换取积分
- 调用超出本机显存/内存的开源模型
- 把家里几台电脑组成一组托管同一大模型
- 通过 OpenAI 客户端接入本地端点使用网络模型

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L11: **Tor6IA is a peer-to-peer network for running open LLMs.** Your machine runs a model for other people and earns cr
> L59: - **Works with your tools.** OpenAI-compatible API on `http://localhost:7606/v1`.
> L181: 1. Your node asks for a model. The coordinator reserves the fastest free machine and returns its public key.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `3bbf5e8d39ed` · [字段定义](../../DATASET.md)*
