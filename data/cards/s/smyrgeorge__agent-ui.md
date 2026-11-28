# smyrgeorge/agent-ui

⭐ 3 · Emacs Lisp · GPL-3.0 · 推送 2026-11-27 · [GitHub](https://github.com/smyrgeorge/agent-ui) · 个人维护

**让 Emacs 里的编码 agent 以画布展示工作进度的包**

一个 Emacs Lisp 包：为运行在 agent-shell 中的编码 agent 提供会话底部的画布，用进度条、清单、表格、图表、diff、图示等 30 类组件就地更新展示 agent 的工作，并通过选项、表单、确认等交互组件把用户回答回传到会话 prompt。驱动方式为 bin/agent-ui 命令行（JSON 进出）或 MCP 工具。依赖 Emacs 29.1+（server 模式）、agent-shell 与 vui；部分组件需 Mermaid CLI、Node/mathjax 或 LaTeX 等可选工具。尚未上架 MELPA，从 GitHub 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 30 种组件类型（progress/table/chart/diff/mermaid 等）就地更新
- 交互式提问组件：choice/confirm/form/rank 等，答案回传会话 prompt
- 命令行（JSON 进出）与 MCP 工具两种驱动方式
- 项目 dashboard 以 el 文件存于仓库，支持定时刷新与 PDF 导出

## 适用场景

- 在 Emacs 中观察编码 agent 的构建进度、测试结果与计划清单
- 通过选项/表单/计划审批等组件与 agent 交互确认
- 为项目维护随仓库提交的运行状态 dashboard

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: **A canvas where coding agents show their work, in Emacs.**
> L5: Agent UI gives a coding agent running in agent-shell a canvas at the
> L150: `agent-ui-mode` ties Agent UI to agent-shell. Each session's agent finds its own canvas, is told about it in its


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `b3f4747047a7` · [字段定义](../../DATASET.md)*
