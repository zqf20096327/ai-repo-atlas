# VladoIvankovic/Codeep

⭐ 22 · TypeScript · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/VladoIvankovic/Codeep) · [官网](https://codeep.dev) · 个人维护 · 中文 README

**面向终端的自主 AI 编码代理：读写代码、跑命令、自我验证**

运行于终端、macOS 原生应用与 Web 仪表盘的自主编码代理：在项目目录中自动识别项目类型、读取文件与目录结构，按 Plan→Read→Edit→Verify→Summary 流程自主创建/编辑/删除文件、执行 shell 命令并循环至任务完成，支持撤销、检查点与 git 回滚。支持十余家模型提供方（含 Ollama 本地运行与任意 OpenAI 兼容端点），提供会话跨设备同步、跨会话召回、@mentions 上下文附加与 MCP 工具。经 npm、curl 脚本或手动二进制安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自主 Agent 模式：9 种工具（读写/编辑文件、执行命令、搜索、抓取 URL）循环至任务完成
- 多提供方支持：Z.AI/OpenAI/Anthropic/DeepSeek/Gemini/MiniMax/Ollama/OpenRouter/自定义 OpenAI 兼容端点
- @file/@folder/@web/@git 消息级上下文附加，附大小上限与缓存
- 会话管理：自动保存、跨会话召回、跨设备同步、检查点与 git 回滚

## 适用场景

- 让 AI 在我的项目里自主改代码并跑测试修失败
- 用本地 Ollama 模型在终端完成编码任务，不依赖云端 API
- 跨设备（CLI 与 Mac 应用）继续同一项目的编码会话

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L9:  Autonomous AI coding agent that reads your project, runs commands, and writes &amp; verifies code — deeper than aut
> L186: Codeep works as a **full AI coding agent** that autonomously:
> L101: ### Multi-Provider Support

## 星数曲线

```mermaid
xychart-beta
    title "VladoIvankovic/Codeep 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-27 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `0147a87ca059` · [字段定义](../../DATASET.md)*
