# tfcace/hash

⭐ 33 · Go · MIT · 推送 2026-10-24 · [GitHub](https://github.com/tfcace/hash) · [官网](https://runhash.dev) · 个人维护

**内嵌 AI 助手的 Go 语言终端 shell，`??` 唤起任意 ACP agent**

用 Go 编写的 shell（Harness Assisted SHell），提供编辑器式多行输入、Helix/Vim/Emacs 键位、SQLite 历史、智能补全与实验性 zsh 方言。AI 集成为核心特性之一：命令行任意位置输入 `??` 即可让 agent 执行任务，支持任意 ACP 协议 agent（Claude Code、Cursor CLI、Gemini CLI）经 stdio 接入，或 Ollama 式 HTTP 模型服务器；工具调用需逐次授权，错误修复可在本地学习复用。项目自述为早期阶段，仅测试过 macOS + Ghostty + Claude 组合，不支持 SSH。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- `??` 前缀在任意命令位置唤起 agent，支持回合制对话
- agent 无关：任意 ACP agent 经 stdio 接入，或 Ollama 式 HTTP 服务器
- 工具调用逐次请求 allow/deny 授权，可按项目/全局/会话限定
- 错误修复本地学习，再次出现时无需调用 agent

## 适用场景

- 在终端用自然语言让 agent 查找文件、执行命令
- 不锁定模型或厂商地切换 Claude/Gemini/Cursor/Ollama 作为后端
- 用带编辑器体验与 Helix 键位的替代 shell 日常操作

## 场景标签

`编码 Agent` `AI 助手` · 领域:编码与开发

## 证据(README 行号)

> L17: Hash is a shell that treats AI as a first-class citizen without locking you into any particular model or vendor. Dr
> L30: - **Agent-agnostic** — any ACP agent (Claude Code, Cursor CLI, Gemini CLI) over stdio, or Ollama-style HTTP model s

## 星数曲线

```mermaid
xychart-beta
    title "tfcace/hash 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-27 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `c9c95a84ee29` · [字段定义](../../DATASET.md)*
