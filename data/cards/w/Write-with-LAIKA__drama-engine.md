# Write-with-LAIKA/drama-engine

⭐ 42 · TypeScript · MIT · 推送 2026-03-02 · [GitHub](https://github.com/Write-with-LAIKA/drama-engine) · 组织维护

**浏览器端 TypeScript 多智能体叙事对话框架**

TypeScript 编写的叙事智能体框架，可在浏览器中执行，面向前端开发者构建多 agent 对话应用。核心机制：由 moderator 编排多 agent 会话，agent 可将任务委派给 deputy 链执行 ad-hoc 提示序列；prompt 依据参与者、任务、状态与材料动态组装。模型与供应商无关，支持任何兼容 OpenAI API 标准的后端（completions 与 chat/completions 端点），支持 ChatML 与 Mistral 提示格式。以 npm 包或源码方式安装，通过环境变量配置后端地址与 API key；框架自身不处理 CORS。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 agent 会话由 moderator 编排，agent 可委派任务给 deputy 链
- 基于上下文动态组装 prompt
- 兼容 OpenAI API 标准的任意后端，支持 ChatML 与 Mistral 提示格式
- 同伴（companion）支持心情概率、知识解锁随互动渐进等叙事机制

## 适用场景

- 在前端构建带 NPC 角色的多 agent 叙事对话应用
- 组合不同提示技术（few-shot、摘要、分析）的模块化推理流程
- 需要供应商无关的 LLM 接入的对话型产品

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: The Drama Engine is a framework for agentic interaction with language models. It is written in TypeScript to execute
> L17: - *Multi-agent workflows with delegation*: The conversation between several agents is orchestrated via a moderator.
> L19: - *Model- and vendor-agnostic*: When run locally, the Drama Engine can use any back-end that supports OpenAI’s API 

## 星数曲线

```mermaid
xychart-beta
    title "Write-with-LAIKA/drama-engine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-30 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `013467cc53db` · [字段定义](../../DATASET.md)*
