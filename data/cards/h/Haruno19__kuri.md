# Haruno19/kuri

⭐ 3 · Swift · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/Haruno19/kuri) · 个人维护

**macOS 原生本地优先 LLM 客户端：对话、思考并在沙盒中执行操作**

以 SwiftUI/AppKit 构建的 macOS 原生应用，内含引擎与 kuri 命令行客户端，二者共享同一配置与对话存储。支持本地离线运行与可选接入托管服务商，通过 JSON5 文件声明 provider、模型与 MCP 服务器；模型命令在 Apple Containerization 提供的 Linux VM 沙盒中执行；对话存于 SQLite，API 密钥存于 Keychain。要求 Apple silicon 与 macOS 26，通过 Releases 的 .dmg 安装，尚未做 Apple 公证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置 kuri 命令行客户端，与 GUI 共享配置和会话
- 每条 wire format 一等适配器，支持对话中途切换模型
- 运行时发现 MCP 服务器，工具策略按 allow/ask/deny 配置
- 模型命令在每会话一个的 Linux VM 沙盒中运行

## 适用场景

- 离线用本地模型聊天并处理本机文件
- 通过 kuri CLI 在当前目录进行一次性提问或继续会话
- 接入自托管 Ollama/vLLM 等本地服务端

## 场景标签

`聊天机器人` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5: A lightweight, macOS native, human-designed & Claude-coded app for working with language models, that can chat, thin
> L7: Kuri runs offline with local models, talks to any hosted provider when you want it to, discovers MCP servers at runt
> L15: - **Local-first.** Works with no network. Hosted providers are opt-in.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `89fd01c1f3c6` · [字段定义](../../DATASET.md)*
