# driftkit-ai/driftkit-framework

⭐ 50 · Java · Apache-2.0 · 推送 2026-10-05 · [GitHub](https://github.com/driftkit-ai/driftkit-framework) · 个人维护

**Java LLM 智能体框架：内置提示词版本管理与测试追踪**

面向 Java 开发者的 LLM 智能体与工作流框架，模块覆盖模型客户端（OpenAI、Gemini、Claude、DeepSeek、Spring AI 适配）、嵌入、向量存储、RAG 管道、工作流引擎（含 Loop/Sequential 多智能体与人工介入）、音频转写与聊天助手会话。核心差异点是提示词生命周期平台：DRAFT→CURRENT 状态机、版本化、测试集与回归检测、追踪与缓存指标，基于 MongoDB 存储并提供 Vue UI。当前 0.9.x、单一维护者，部分模块无测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 提示词状态机与版本化、审计日志
- 测试集+评测运行+定时回归检测，可从 UI 驱动
- 跨 Claude/OpenAI/DeepSeek 归一化的 CacheUsage 缓存指标
- 多智能体模式（Loop、Sequential、AgentAsTool）与人工介入工作流

## 适用场景

- 让非开发人员在代码外编辑与测试提示词
- 按提示词版本查看追踪与缓存指标
- 构建带人工审批环节的 LLM 工作流

## 场景标签

`Agent 框架` `多智能体` `提示工程` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L3: A Java framework for LLM agents and workflows where prompt lifecycle management (versioning, testing, tracing) is bu
> L127: |driftkit-context-engineering|Prompt management platform: storage backends, template engine, Vue UI, test sets, tr

## 星数曲线

```mermaid
xychart-beta
    title "driftkit-ai/driftkit-framework 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-27 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `15b6ee982d7e` · [字段定义](../../DATASET.md)*
