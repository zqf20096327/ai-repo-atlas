# CompleteTech-LLC/build-ai-workflows-in-5-steps

⭐ 16 · Python · MIT · 推送 2026-09-22 · [GitHub](https://github.com/CompleteTech-LLC/build-ai-workflows-in-5-steps) · 组织维护

**教学笔记本：5 步法将目标图+源文档变成可执行 AI 工作流**

CompleteTech LLC 发布的 Jupyter 教学课程（29 个 cell），演示一套五步 AI 工作流设计方法：上下文启动、任务分解、Mermaid 可视化工作流设计、工作流固化（转化为可执行 Python 以跳过后续 AI 调用）。内置示例为从杂乱的合成餐厅财务 PDF 推断出目标仪表盘的转换流程，支持替换用户自己的目标图与源文档。支持 Anthropic/OpenAI/Google 三家 API，自动检测可用密钥，面向零基础到有经验开发者。课程明确不含 prompt 缓存、流式、多 agent 编排与评测。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五步法：上下文启动、任务分解、Mermaid 工作流、固化为可执行 Python
- provider 无关：自动检测 Anthropic/OpenAI/Google 密钥，任选其一
- 可替换自己的目标图与源文档，工作流整体重定向
- 教程明确列出不在范围内的话题（缓存、流式、多 agent、评测）

## 适用场景

- 零基础学习从目标图+源文档设计 AI 工作流
- 把杂乱 PDF 转换为可复用的确定性 Python 流程
- 练习可迁移的 prompt 工程模式

## 场景标签

`教程课程` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L26: This repository is a teaching notebook about a repeatable AI workflow design method, not a restaurant-finance produ
> L28: Watch an AI read the goal image, then the source document, then decompose the transformation into a workflow, rende

## 星数曲线

```mermaid
xychart-beta
    title "CompleteTech-LLC/build-ai-workflows-in-5-steps 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `144dc5b0ca04` · [字段定义](../../DATASET.md)*
