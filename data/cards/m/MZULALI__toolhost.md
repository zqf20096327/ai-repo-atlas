# MZULALI/toolhost

⭐ 22 · TypeScript · MIT · 推送 2026-09-11 · [GitHub](https://github.com/MZULALI/toolhost) · 个人维护

**让 LLM 在运行时自写并调用工具的 Node.js 宿主库**

TypeScript 库，向模型提供 create_tool 等 5 个内置工具：模型提交名称、JSON Schema 与函数体，库用 acorn 解析源码、拒绝顶层代码、以 SQLite 按版本保存并重启隔离 worker 进程供下一轮调用，出错时可回滚历史版本。运行在子 Node 进程中，隔离故障而非恶意意图，默认启用 Node 权限模型，网络不受限，README 明确声明非沙箱。提供 Anthropic、OpenAI 两种 API 及 Vercel AI SDK 适配器，仅经 GitHub 安装，要求 Node 22.18+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 模型通过 create_tool 在运行时生成工具，SQLite 全历史版本化并可回滚
- acorn 解析源码，拒绝含顶层代码的函数体
- 工具在独立 worker 进程中运行，默认 Node 权限模型限制文件访问与子进程
- 内置 5 个工具管理原语与带稳定错误码的 ToolError

## 适用场景

- 让 agent 在对话中自行编写、修复、回滚所需工具
- 为 Anthropic/OpenAI/Vercel AI SDK 应用增加运行时工具生成能力
- 在容器内为不可信用户提供受限的模型自建工具运行环境

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: Let an LLM write its own tools at runtime.
> L7: The model calls `create_tool` with a name, a JSON Schema, and a function body. toolhost parses the source, proves th
> L52: Adapters exist for Anthropic, OpenAI Responses, OpenAI Chat, and the Vercel AI SDK. Each has a runnable example:

## 星数曲线

```mermaid
xychart-beta
    title "MZULALI/toolhost 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `7f00bc252ab2` · [字段定义](../../DATASET.md)*
