# dakotamurphyucf/ochat

⭐ 31 · OCaml · MIT · 推送 2026-10-21 · [GitHub](https://github.com/dakotamurphyucf/ochat) · [官网](https://ochatlabs.com) · 个人维护

**用文本文件定义并运行 LLM agent 的 OCaml 工具包**

Ochat 是以纯文本文件（ChatMarkdown）定义 AI agent 的工具包：在文件中声明指令、内置工具（读文件、编辑、网页摄取、文档搜索等）与模型设置，通过本地终端 TUI、脚本 headless 或后台服务运行；支持把另一个 agent 文件作为专家工具复用，并可用 ChatML 脚本控制工作流与事件协调。本体用 OCaml 编写但 agent 定义不限语言。当前仅集成 OpenAI（需 API key），可经 OpenAI 兼容代理接入其他后端。安装需 OCaml 5.1+/Dune 3.21+ 并从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ChatMD 纯文本文件定义 agent，可版本控制并与项目共享
- 内置文件读写、网页摄取、文档搜索等工具，无需自写实现
- 专家 agent 作为工具复用、ChatML 脚本控制多轮工作流
- 支持终端交互、脚本 headless 与后台服务三种运行方式

## 适用场景

- 在项目仓库里定义专属代码理解/评审/文档助手
- 团队共享同一 agent 定义并像代码一样评审变更
- 为长流程工作流编写脚本化的事件协调逻辑

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7: Ochat lets you define an AI agent in a text file and run it against your project.
> L82: You'll need an OCaml/opam installation, this repository checked out locally,
> L142: Today Ochat integrates with OpenAI; future work is intended to support additional backends while keeping ChatMD an

## 星数曲线

```mermaid
xychart-beta
    title "dakotamurphyucf/ochat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-30 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d1568484d6d9` · [字段定义](../../DATASET.md)*
