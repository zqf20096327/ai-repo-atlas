# tinyhumansai/openhuman

⭐ 42,143 · Rust · GPL-3.0 · 推送 2026-10-18 · [GitHub](https://github.com/tinyhumansai/openhuman) · [官网](https://tinyhumans.ai/openhuman) · 个人维护 · 中文 README

**Rust 编写的 agent 运行时：单机运行数百个 agent 的桌面应用与库**

以 GPL-3.0 发布的 agent harness，编译为单进程 Rust 核心，同时提供桌面应用（macOS/Windows/Linux 安装包）与 Rust 库两种形态。内置记忆（每轮按 token 预算召回并附引用）、Jev 工具搜索模型（在 1,215 个工具中选取）、浏览器与桌面控制、MCP 与技能、14 个消息渠道及 Composio 的 119 个 OAuth 集成。模型经 BYOK 接入 26 个 provider，本地模型支持 Ollama、LM Studio、MLX，含自动模型路由。当前为 early beta。README 中列出与六个其他 harness 的公开基准数据，复现材料在 openhuman-benchmarks 仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 动量与使用信号

- 维护:`active` — 距上次 push 1.0 天,年发版 63,180 位贡献者
- 涨星:近 1 天 **+33**(自 20261016 起算)
- 平台:WINDOWS / MACOS / LINUX · 协议:MCP / OLLAMA

## 能力要点

- 桌面应用与 Rust 库双形态，单进程可并行运行数百个 agent（README 称 500 个可放于 $10 VPS）
- RLM token 压缩：大型工具结果压缩为可检索句柄后再交给模型
- Jev 小模型做工具搜索，无截图地从屏幕按钮选取点击
- 14 个消息渠道（Telegram/Discord/iMessage/邮件等）作为 agent 前端

## 适用场景

- 在单个低成本服务器上为每个客户运行一个 agent 的产品化部署
- 通过桌面/终端与 agent 交互，让其操作浏览器和本地应用
- 在 Rust 项目中以函数调用方式嵌入 agent 能力

## 场景标签

`AI 助手` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L4:  A desktop app for people. A Rust library for developers.
> L84:  Use it as a Rust library: call an agent like any other function, or run a whole fleet from one small server.
> L164: |Models|Local models (Ollama, LM Studio, MLX) and BYOK for 26 providers, with automatic model routing|

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `8e8cee749f13` · [字段定义](../../DATASET.md)*
