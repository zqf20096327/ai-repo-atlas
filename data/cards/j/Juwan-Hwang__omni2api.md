# Juwan-Hwang/omni2api

⭐ 37 · Rust · MIT · 推送 2026-10-24 · [GitHub](https://github.com/Juwan-Hwang/omni2api) · [官网](juwanh.com/lab/omni2api) · 个人维护 · 中文 README

**把终端侧 AI agent 包装成 OpenAI 兼容 API 的 Rust 服务器**

Rust + Axum 实现的自托管服务器，在通常由模型占据的位置设一个『座位』：任何能运行 oh-seat CLI 并遵循其循环的 agent（或本地非云端 AI）坐上座位后，即可接收并通过 OpenAI Chat Completions/Responses 或 Anthropic Messages 协议应答调用方请求，附带真实 tool_calls 回传机制。已测试 Claude Code、Codex、Cline 等十余种调用端。提供 install.sh 一键安装、免费快速隧道公网地址及 Docker Compose/Kubernetes 等部署选项；回复速度取决于座位上 agent 的处理节奏。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将终端 agent 暴露为 OpenAI/Anthropic 兼容 API（HTTP/SSE）
- tool_calls 真实回传，由调用方在自己的沙箱执行并路由结果
- 剥离 system prompt 与工具 schema，仅传递用户输入与一行环境信息
- 免费快速隧道、Cloudflare 固定隧道与 Docker Compose/Kubernetes 部署选项

## 适用场景

- 让本地 agent 被任何 OpenAI 兼容的 CLI/IDE 工具当作模型端点调用
- 把一个 AI agent 变成自托管 API 供远程工具接入
- 用统一的 OpenAI 协议聚合人或 agent 作为应答方

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: Turn anything that can sit at a terminal into an OpenAI-compatible API
> L128: ├── server/      # Rust + Axum server (`omni2api` binary): OpenAI/Anthropic ingress, seat API


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `27f79d2c595a` · [字段定义](../../DATASET.md)*
