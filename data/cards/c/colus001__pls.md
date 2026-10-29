# colus001/pls

⭐ 67 · Zig · MIT · 推送 2026-05-21 · [GitHub](https://github.com/colus001/pls) · 个人维护

**自然语言转 shell 命令的终端 AI 助手**

用 Zig 编写的单二进制 CLI 工具：用户用任意语言描述任务，LLM 解读并生成 shell 命令，以“执行-观察输出-决定下一步”的代理循环运行，最多 20 轮；破坏性命令（kill/rm/dd 等）触发确认，支持 --dry-run 预览。默认通过免费托管的 Gemini 代理开箱即用、无需 API key，也可切换 Anthropic/OpenAI/Gemini/Ollama 或自带 key；提供 curl 脚本、Homebrew、源码编译（Zig 0.15+）及 .deb 包安装，代理可基于 Cloudflare Workers 自托管。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 免费托管 Gemini 代理，无需 API key 开箱即用
- 执行-观察-决策的代理循环，上限 20 轮
- 破坏性命令确认提示与 --dry-run 预览
- 支持 Anthropic/OpenAI/Gemini/Ollama 多提供方，代理可自托管

## 适用场景

- 用自然语言让终端执行系统管理任务
- 不带 API key 快速上手本地命令行 AI 助手
- 离线场景切换 Ollama 作为本地提供方

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: AI-powered CLI assistant. Type what you want in natural language, and `pls` figures out the shell commands.
> L18: 2. An LLM interprets it and generates shell commands

## 星数曲线

```mermaid
xychart-beta
    title "colus001/pls 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 66 --> 68
    line [67, 67]
```

2026-10-18 67 → 2026-10-29 67（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `1f352e5bb159` · [字段定义](../../DATASET.md)*
