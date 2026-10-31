# subinium/ddududdudu

⭐ 13 · TypeScript · 推送 2026-03-20 · [GitHub](https://github.com/subinium/ddududdudu) · 个人维护

**Rust TUI + TypeScript 引擎的多模型 AI 编码 harness CLI**

面向开发者的终端 AI 编码工具：原生 Rust TUI 配 TypeScript harness 引擎，围绕 Anthropic/OpenAI/Gemini 三家 provider 的四种角色模式（JENNIE/LISA/ROSÉ/JISOO）做编排、委派与验证。内置 26 个文件、git、搜索、测试、委派类工具；支持会话恢复、git worktree 隔离委派、上下文压缩与分层记忆、成本预算跟踪及多模型并行基准。仅支持源码安装（Node.js>=20 与 Rust 工具链），需 provider 认证；基准任务包仍在打磨中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 四模式多 provider 编排与并行/委派运行
- 内置 26 个工具（文件/git/检索/测试/委派等）
- LLM 上下文压缩与分层记忆晋升管道
- 多模型并行基准，输出 JSONL 报告与成本跟踪

## 适用场景

- 在终端用多个 LLM 模型协作完成编码任务
- 跨仓库恢复与续接历史编码会话
- 对多个模型做编码任务基准对比与成本核算

## 场景标签

`编码 Agent` `模型评测` · 领域:编码与开发

## 证据(README 行号)

> L14: - Native Rust TUI with a TypeScript harness engine
> L39: ddudu treats a coding harness as a small operating layer around provider runtimes rather than as a prompt wrapper.
> L76: |`JENNIE`|Anthropic|`claude-opus-4-6`|orchestration, verification, delegation|

## 星数曲线

```mermaid
xychart-beta
    title "subinium/ddududdudu 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `a9243d42f02f` · [字段定义](../../DATASET.md)*
