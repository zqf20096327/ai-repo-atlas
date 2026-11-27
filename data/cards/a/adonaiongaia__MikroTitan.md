# adonaiongaia/MikroTitan

⭐ 5 · Rust · GPL-3.0 · 推送 2026-11-26 · [GitHub](https://github.com/adonaiongaia/MikroTitan) · 个人维护

**本地双引擎 LLM 桌面工作室：支持超内存模型运行**

基于 Tauri 的本地桌面 AI 工作室，在统一界面后管理两个推理引擎：janas-server 通过 SSD 流式读取 .jns 模型权重，使超过内存容量的模型可以运行；llama-server 在 CPU/GPU 上运行 GGUF 模型。提供 Agent 模式（Think→Act→Observe 循环与工作区工具）、本地文档库（BM25+TF-IDF 检索与引用）、whisper.cpp 本地语音输入、分支聊天、MCP 工具范围控制、崩溃安全会话存储。安装器不捆绑引擎二进制，启动时自动按硬件探测下载并校验。以 Linux AppImage 分发，首次运行需网络。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双引擎：janas-server SSD 流式运行超 RAM 的 .jns 模型，llama-server 运行 GGUF
- Agent 模式：有界 Think→Act→Observe 循环、审批、规划、逐文件撤销
- 本地文档库：BM25+TF-IDF 检索，聊天与代理回复带 [D#] 引用
- 启动时自动探测 CUDA/ROCm/Vulkan/Metal/CPU 并下载校验引擎

## 适用场景

- 在内存有限的设备上运行大于内存的 LLM
- 本地无遥测、无账号地使用聊天与 Agent 工作流
- 从 Hugging Face 浏览并下载 GGUF 模型管理本地推理
- 本地 PDF/笔记文档的检索式问答

## 场景标签

`推理引擎` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L5: **A dual-inference local AI desktop studio.** Run **Janas-LLM** models with SSD streaming so models larger than RAM 
> L7: MikroTitan is a local AI studio with **agent mode**, a local document vault, **local voice input**, branching chat h
> L15: - **Dual engines.** `janas-server` streams `.jns` models from SSD, so a model larger than RAM can still run; `llama


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `139040087a79` · [字段定义](../../DATASET.md)*
