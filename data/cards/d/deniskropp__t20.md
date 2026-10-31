# deniskropp/t20

⭐ 14 · Python · 推送 2026-10-26 · [GitHub](https://github.com/deniskropp/t20) · [官网](https://ai.violass.club/t20) · 个人维护

**面向多智能体协作任务编排的 CLI 框架：目标→计划→委派执行**

Python 编写的多智能体框架：用户给出高层目标后，由 Orchestrator 代理生成分步计划并将任务委派给 YAML 定义的专职代理（设计、编码、音乐、文案等），迭代执行并把每步 prompt 与输出记录到会话目录以供追溯。代理通过 YAML 文件自定义，可指定模型与委派团队。运行时通过 LLM 抽象层接入 Gemini（需 Google API key）及 Ollama 等提供商。以 t20-system CLI 操作，仓库含 2026 年状态说明，称其为早期基础并主要作历史参考与可扩展底座使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Orchestrator-delegate 模型：目标→计划→任务委派→迭代执行
- 代理以 YAML 定义，可自定义角色、模型与委派团队
- 每步 prompt 与输出写入会话目录，全流程留痕
- LLM 抽象层提供 Gemini、Ollama 等实现

## 适用场景

- 用一条命令让代理团队生成落地页、React 组件等前端代码
- 组织多代理完成音乐制作、文案与视频脚本等创作任务
- 按 YAML 模板扩展自己的专职代理参与编排

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7: **T20 is a sophisticated, multi-agent framework designed to tackle complex tasks through collaborative AI. It empowe
> L18: 2. **Dynamic Planning**: A lead `Orchestrator` agent analyzes the goal and generates a step-by-step plan.
> L197: |`llm.py`|Provides an abstract base class `LLM` and concrete implementations for different LLM providers (Gemini, 

## 星数曲线

```mermaid
xychart-beta
    title "deniskropp/t20 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `943b5e381d16` · [字段定义](../../DATASET.md)*
