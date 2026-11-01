# timwuhaotian/killi

⭐ 18 · Rust · MIT · 推送 2026-10-31 · [GitHub](https://github.com/timwuhaotian/killi) · [官网](https://github.com/timwuhaotian/killi#readme) · 个人维护

**面向终端的 Rust 编写小型 AI 编程 agent（Apple Silicon Mac）**

用 Rust 编写的单二进制终端 AI 编程 agent，读取代码、执行命令、编辑文件，可接入 OpenAI 兼容、Anthropic 兼容或 OpenAI Responses 接口的 LLM，支持 MCP 服务器、子代理、计划模式、skills、hooks 与 AGENTS.md。设计核心是尽量少地向模型发送内容并保持发送方式稳定以命中提供商的 prompt cache（70–90% 输入 token 来自缓存）。仅支持 Apple Silicon Mac，作者自述处于早期阶段。提供 install.sh 安装脚本与 cargo 源码构建两种方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单个 6 MB 二进制，启动低于 20 ms，运行一个 prompt 约 15 MB 内存
- 系统提示与工具列表合计约 2,600 tokens，70–90% 输入 token 命中缓存
- 支持 MCP 服务器、子代理（含最多 128 项的 swarm 模式）、计划模式、skills、hooks
- 可从 Kimi Code、pi、omp、opencode 迁移配置，或通过 killi login 接入 ChatGPT/OpenCode Go/Muse Code 订阅

## 适用场景

- 在终端里让 AI 代理修 bug、按规格实现功能、做多文件重构
- 希望控制 token 消耗并利用 prompt cache 的开发者
- 从 Kimi Code 等其他编程 agent 迁移配置继续使用

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L10: **killi is a fast, tiny AI coding agent for your terminal**, written in Rust (one small native
> L11: binary, no runtime). Like Claude Code, Codex CLI, opencode or Kimi Code, it reads your code, runs
> L13: OpenAI Responses LLM, and it supports MCP servers, subagents, plan mode, skills, hooks and


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `a79de09c450a` · [字段定义](../../DATASET.md)*
