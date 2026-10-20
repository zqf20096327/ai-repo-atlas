# ByteNestLab/x-ai-agent

⭐ — · [GitHub]() · 组织维护

**开源 X/Twitter AI Agent 框架：内容生成、回复、排程与分析**

TypeScript 库，供开发者、创作者与营销团队构建自己的 X（Twitter）AI Agent：目标→AI 推理→行动方案→人工批准→执行→分析的循环。提供推文生成/改写、AI 回复建议、带时区与重试的排程模型、互动规划器、互动率分析与 SafetyGuard 安全层（垃圾语言检测、每日限额）。关键限制：AIProvider 接口当前仅 MockAIProvider 可运行，OpenAI/Gemini/Claude 为占位适配器，官方 X API 与浏览器自动化均未实现，排程为内存态 MVP。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 动量与使用信号

- 安装:github 包 `release-assets` 月下载无数据

## 能力要点

- AI 推文生成与 6 种风格改写引擎
- SafetyGuard 检测垃圾语言、近似重复与每日限额
- 默认人工批准的互动工作流（createEngagementWorkflow）
- 生成/执行分离设计，LLM、排程、X 客户端、存储层均可替换

## 适用场景

- 构建需人工审核的 X 内容自动化工作流
- 本地生成推文草稿与回复建议（无需 API key）
- 为创作者或营销团队搭建 X 运营分析反馈闭环

## 场景标签

`Agent 框架` `AI 写作` · 领域:Agent 开发

## 证据(README 行号)

> L3: Open-source X/Twitter AI Agent framework for content generation, intelligent replies, scheduling, engagement workflo
> L164: An application that turns a goal into reviewed AI suggestions and measurable actions on X. This repository provide


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `8978f81a7c11` · [字段定义](../../DATASET.md)*
