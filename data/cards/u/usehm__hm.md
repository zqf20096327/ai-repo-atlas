# usehm/hm

⭐ 3 · Go · AGPL-3.0 · 推送 2026-11-21 · [GitHub](https://github.com/usehm/hm) · [官网](https://usehm.dev) · 个人维护

**内置 AI 编码 agent 的原生桌面代码编辑器，自带密钥即可用**

用 Go 编写、以 WebGPU（Yoga 工具包）渲染 UI 的桌面代码编辑器，在 macOS/Linux/Windows 原生运行，不依赖浏览器引擎。编辑器功能包括 Tree-sitter 语法高亮、LSP 诊断与跳转、ripgrep 项目搜索、Git 面板、集成终端与 Vim 键映射。AI agent 采用 BYOK 模式，支持 YAML 配置、rubber-duck/lazy 等放慢节奏的模式、运行 shell 前默认确认、会话树分支/回退/重放，并可读取 AGENTS.md/CLAUDE.md 指令文件、兼容 Claude Code 命令模板。安装与运行方式未在可见部分给出。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 Anthropic、Gemini、OpenAI、Azure OpenAI 及任意 OpenAI 兼容端点
- 会话以 JSON Lines 追加式保存，支持树状分支、编辑重发与逐条回放
- rubber-duck/lazy 模式与 guard.yaml 规则、shell 执行前默认确认
- 可读取 AGENTS.md/CLAUDE.md，Claude Code 命令模板直接可用

## 适用场景

- 在不离开编辑器的情况下与编码 agent 结对修改代码
- 本地接入自有 API key 或 Ollama/LM Studio 端点使用 agent
- 对 agent 的每处改动在真实编辑器中审查、回退或分支重试

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L9: Hm is a desktop code editor with an AI coding agent built in. It is written in Go and draws its UI with Yoga, a GPU-
> L11: Everything is configured in plain YAML, with a settings page on top. The agent is bring-your-own-key: Anthropic, Go
> L65: ### AI agent


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `dea1fe2ea278` · [字段定义](../../DATASET.md)*
