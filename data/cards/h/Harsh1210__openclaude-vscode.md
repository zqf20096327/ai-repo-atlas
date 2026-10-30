# Harsh1210/openclaude-vscode

⭐ 15 · TypeScript · MIT · 推送 2026-04-24 · [GitHub](https://github.com/Harsh1210/openclaude-vscode) · 个人维护

**VS Code AI 编程助手扩展：统一 UI 接入任意 LLM 后端**

VS Code 扩展，作为开源 OpenClaude CLI 的编辑器界面：流式聊天面板、原生 diff 查看器、@-mentions、会话历史与检查点回滚均由扩展承载，而工具调用、provider 路由、MCP 与斜杠命令等逻辑全部在 CLI 内运行。支持 OpenAI、Anthropic、Gemini、DeepSeek、Ollama、AWS Bedrock、Vertex AI、GitHub Models 及 200+ OpenAI 兼容端点，可经 /provider 命令会话中途切换。安装需先 npm 全局安装 CLI，再从 VS Code Marketplace 或 .vsix 装扩展。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 provider 路由：OpenAI/Anthropic/Gemini/Ollama/Bedrock 等 200+ OpenAI 兼容端点，/provider 会话中切换
- 原生 VS Code diff 查看器，AI 修改可 Accept/Reject
- @-mentions 引用文件、文件夹、符号与行范围
- MCP 服务器集成与插件管理器，5 种权限模式

## 适用场景

- 在 VS Code 里用自己已有的 API 账号或本地 Ollama 模型做 AI 结对编程
- 同一仓库上并行运行多个 AI 会话（Git worktree 支持）
- 通过 /commit、/review 等斜杠命令让 AI 处理提交与代码审查

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L24: OpenClaude is a full-featured **VS Code extension** that wraps the open-source OpenClaude CLI. The CLI is where all
> L44: ### Multi-Provider Support

## 星数曲线

```mermaid
xychart-beta
    title "Harsh1210/openclaude-vscode 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `41782327b85b` · [字段定义](../../DATASET.md)*
