# blurryface13/asteria-agent

⭐ 42 · Python · Apache-2.0 · 推送 2026-09-27 · [GitHub](https://github.com/blurryface13/asteria-agent) · 个人维护 · 中文 README

**本地优先的科研智能体工作台：自主规划并撰写带引用的报告**

面向文献调研、综述写作与实验设计的多 Agent 科研工作台：用户以自然语言描述目标，AgentOrchestrator 负责意图与路由，科研支路由 Lead 安排子目标并行调查、按批综合与补研，Writer 成稿后由 CitationAgent 核对正文与原文出处。技术栈为 Python + FastAPI + Next.js + PostgreSQL/Redis/ChromaDB，通过 stdio MCP 接入科研工具，支持 Ollama 与 DeepSeek 模型。提供 Docker Compose GPU 部署与验收脚本；部分功能（语义评分、检查点恢复）仍在开发中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 Agent 编排：Lead 并行委派研究、CitationAgent 核对引用
- 生成 Markdown/LaTeX/PDF 报告，图表数据与来源独立留档
- 分层记忆：PostgreSQL 会话、Redis 上下文、ChromaDB 主题语义召回
- Docker Compose GPU 部署与部署验收脚本

## 适用场景

- 我用自然语言下达调研目标，让 Agent 产出带引用的文献综述
- 实验室多成员隔离使用共享知识库做研究与问答
- 导入研究 Trace 做规则归因与 BadCase 质检

## 场景标签

`科研工具` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: 面向文献调研、综述写作和实验设计的科研智能体工作台。用自然语言描述目标，Agent 自主规划、委派研究、阅读与追踪论文，在证据充分后交付带引用的报告。
> L7: 当前主入口按 EchoMind 的角色编排方式适配：`AgentOrchestrator` 负责意图与主辅路由，工作角色共享 `BaseAgent` 工具循环；科研支路由 Lead 安排互补子目标并行调查、按批综合与补研，Write
> L13: - **报告交付**：生成 Markdown、LaTeX 与 PDF，在工作台检查报告、源码、研究轨迹和引用关系；支持围绕报告继续问答。

## 星数曲线

```mermaid
xychart-beta
    title "blurryface13/asteria-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-29 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `01901055225c` · [字段定义](../../DATASET.md)*
