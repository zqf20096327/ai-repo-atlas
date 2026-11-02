# jimoto-no-llm/rustdsh

⭐ 100 · JavaScript · MIT · 推送 2026-11-01 · [GitHub](https://github.com/jimoto-no-llm/rustdsh) · [官网](https://jimoto-no-llm.github.io/rustdsh/) · 个人维护 · 中文 README

**DeepSeek Harness 的 Rust 启动器/微型编排器，加速本地 LLM agent 运行**

rdsh 是 DeepSeek Harness (dsh) 的 Rust 实现 launcher：非原生子命令透明委托给上游 dsh，保持参数兼容；原生部分以 Rust 运行，提供 token 估算、上下文裁剪、并行文本搜索、会话管理、插件补装、凭证导入与更新监视等工具。模型路由支持 OpenAI 兼容端点及 Ollama/llama.cpp 本地推理。提供预编译二进制（含 .deb/.rpm）、cargo install 与源码构建三种安装方式。注意：已启动的会话仍运行 Node.js，启动性能数据仅指进程冷启动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- dsh 参数 100% 直通委托，现有脚本不改即可用
- 原生 Rust 工具：token 估算、上下文 prune、并行搜索、rdsh doctor 诊断
- 插件补装目录编译进二进制，自动后台跟踪最新 release（sha256 校验）
- 凭证清单化共享：不显示值、按选择策略导入 OAuth/API key

## 适用场景

- 用更快的原生启动器替代 dsh 命令日常运行本地 LLM agent
- 为 dsh 配置补齐缺失的必备插件并自动保持更新
- 从 Codex CLI / opencode 一次性导入已有凭证

## 场景标签

 · 领域:开发者工具/LLM agent 运行时

## 证据(README 行号)

> L18: `rdsh` is a Rust micro-orchestrator for local LLM agents: it bundles the operational surface — web search, session 
> L20: The delegated harness sits behind a swappable adapter layer; the bundled DeepSeek Harness (`dsh`) adapter delegates


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-02 · 置信度 high · 依据 README sha `4816224b890b` · [字段定义](../../DATASET.md)*
