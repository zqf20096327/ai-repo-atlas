# ginkida/gokin

⭐ 107 · Go · MIT · 推送 2026-10-24 · [GitHub](https://github.com/ginkida/gokin) · [官网](https://gokin.ginkida.dev) · 个人维护

**终端里的 AI 编程代理：自然语言操作代码、命令与 git**

Go 编写的开源 CLI 编程助手，通过自然语言执行文件操作、代码搜索、shell 命令、git 工作流与任务管理，内置 59 个工具并支持 MCP。支持三种提供方：GLM（默认）、DeepSeek（经 Anthropic 兼容 API）与 Ollama（完全本地）。声称零遥测、TLS 强制、密钥自动脱敏与三级权限控制。提供 headless/JSON 输出模式用于 CI 自动化，会话支持恢复、分叉与回滚，并有 Claude SDK 风格控制帧的兼容层。安装提供一键脚本与源码构建（需 Go 1.25+）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种提供方统一接口：GLM（默认）/DeepSeek/Ollama（完全本地）
- 59 个内置工具 + MCP 支持，5 个并行 Agent 共享内存
- headless 模式输出 json/stream-json，支持 --json-schema 结构化输出校验
- 会话恢复/分叉/回滚，含代码与对话的时间线还原

## 适用场景

- 在终端用自然语言改代码、跑测试、建 PR
- 在 CI 中用单次 headless 调用做代码审查或总结
- 通过 Ollama 在本地离线使用编程助手

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L11:  AI-powered coding agent for your terminal GLM · DeepSeek · Ollama — 100% open source
> L23: Most AI coding tools are closed-source, route your code through third-party servers, and give you zero control over
> L25: Three providers, one interface: **GLM (default), DeepSeek** (via Anthropic-compatible APIs) and **Ollama** (fully l

## 星数曲线

```mermaid
xychart-beta
    title "ginkida/gokin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 106 --> 108
    line [107, 107]
```

2026-10-18 107 → 2026-10-28 107（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `ca24148820cc` · [字段定义](../../DATASET.md)*
