# Arthur-Ficial/apfel

⭐ 6,502 · Swift · MIT · 推送 2026-10-14 · [GitHub](https://github.com/Arthur-Ficial/apfel) · [官网](https://apfel.franzai.com) · 个人维护

**把 Apple Intelligence 内置模型暴露为 CLI 与本机 OpenAI 兼容服务器**

面向 macOS 26+ Apple Silicon 用户的 Swift 工具：读取 Apple FoundationModels 内置的约 3B 参数端侧模型，提供三种使用方式——管道友好的 UNIX 命令行、`--serve` 启动的本地 OpenAI 兼容服务器（base_url http://localhost:11434/v1）与 `--chat` 交互 REPL。支持工具调用（含 MCP 服务器挂载）、流式输出、json_schema 结构化输出，无需 API key、完全端侧运行。限制：上下文窗口 4096/8192 tokens、单一模型不可配置、无 embeddings、响应需数秒。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种形态：UNIX 管道工具 / OpenAI 兼容服务器 / 交互 REPL
- MCP 工具发现与调用（本地进程与远程 Streamable HTTP）
- OpenAI API 兼容：chat/completions、responses、json_schema、流式与真实 token 计数
- 捆绑 cmd/oneliner 等 8 个示例 shell 脚本，`apfel demos` 一键导出

## 适用场景

- 在没有 API key 的 Mac 上通过命令行快速调用本机 LLM
- 让现有 OpenAI SDK 应用切换到本地端侧后端
- 通过 MCP 挂载工具服务器做带工具调用的本地推理
- 写 shell 脚本用自然语言生成命令（cmd 示例）

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L14: Apple Silicon Macs ship a built-in LLM via Apple FoundationModels. `apfel` exposes it as a UNIX tool and a local Op
> L19: |OpenAI-compatible server|`apfel --serve`|Drop-in local `http://localhost:11434/v1` backend for OpenAI SDKs|

## 星数曲线

```mermaid
xychart-beta
    title "Arthur-Ficial/apfel 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-21"]
    y-axis "stars" 6475 --> 6504
    line [6477, 6502, 6502]
```

2026-10-18 6,477 → 2026-10-21 6,502（+25）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-20 · 置信度 high · 依据 README sha `9f672f5168ca` · [字段定义](../../DATASET.md)*
