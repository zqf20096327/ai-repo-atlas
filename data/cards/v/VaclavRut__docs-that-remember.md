# VaclavRut/docs-that-remember

⭐ 31 · MIT · 推送 2026-01-13 · [GitHub](https://github.com/VaclavRut/docs-that-remember) · 个人维护

**面向人机协作的文档模板体系：记录决策与经验供 LLM 使用**

一套文档目录结构与 Markdown 模板：按 context/product/features/logs 四层组织，引导团队记录为什么构建、构建了什么、如何构建、上线后发生了什么以及经验教训；强调按时间顺序的日志而非一次性完美文档，每类信息只保留单一存放处。模板结构面向 LLM 可读可填写，为 AI 助手提供功能上下文。使用方式为 git clone 后复制 docs 目录到自己的项目，从 vision.md、system-map.md、prd.md 三个文件起步填写。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四层目录结构（context/product/features/logs）+ 功能模板（spec/tech-design/tasks/test-plan）
- 以时间顺序的日志（implementation/validation/insights）替代易过时的完美文档
- 模板结构面向 LLM 理解与填写，为每个功能提供 AI 协作所需上下文

## 适用场景

- 与 AI 助手协作开发时为其提供项目上下文
- 小团队在无官僚流程的前提下沉淀决策与经验
- 按 5 天路径渐进搭建文档体系

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L40: ### 2. Built for AI Collaboration
> L103: Templates LLMs can fill out. Context for every feature. Prompts that work. Built for human-AI collaboration from d

## 星数曲线

```mermaid
xychart-beta
    title "VaclavRut/docs-that-remember 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-30 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `e60cb65ebd5b` · [字段定义](../../DATASET.md)*
