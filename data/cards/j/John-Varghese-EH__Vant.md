# John-Varghese-EH/Vant

⭐ 27 · Rust · GPL-3.0 · 推送 2026-11-25 · [GitHub](https://github.com/John-Varghese-EH/Vant) · 个人维护

**把家用 GPU 电脑变成可远程访问的私有 AI 服务器**

Vant 是一个以 Tauri v2（Rust 后端）构建的单二进制工具，分服务器与客户端两种角色：服务器端在自有 GPU/NPU 工作站上编排 16 种 AI 工具（含 Docker Compose 蓝图与本地引擎），客户端在笔记本上以本地回环代理（127.0.0.1:11434）转发推理请求。连接基于 Noise-XX 加密握手与 Cloudflare Tunnel，配 SAS 配对验证、RBAC 与可撤销令牌。构建需 Node.js 18+ 与 Rust 工具链，服务器端要求 Windows/Linux 及独立 GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单二进制支持服务器/客户端双角色切换
- 16 种 AI 工具的一键部署配置（Ollama、ComfyUI、Open WebUI 等）
- Noise-XX 端到端加密 + SAS 防中间人配对
- 为 Claude Code、Cursor、Continue.dev 提供本地回环代理

## 适用场景

- 出门用轻薄本远程调用家里的游戏 GPU 跑本地模型
- 让 IDE 里的 AI 编程工具透明地走自托管推理后端
- 与信任的伙伴以加密配对共享闲置 GPU 算力

## 场景标签

`推理引擎` `图像生成` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L34: |**Primary Function**|Drives bare-metal GPU/NPU acceleration, manages 16 AI containers, and orchestrates encrypted 
> L75: ## 16 Supported AI Engines & Services
> L77: Vant includes ready-to-run deployment profiles for 16 leading open-source AI tools:


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `12d82276e7f0` · [字段定义](../../DATASET.md)*
