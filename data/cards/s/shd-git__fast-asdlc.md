# shd-git/fast-asdlc

⭐ 27 · MIT · 推送 2026-07-01 · [GitHub](https://github.com/shd-git/fast-asdlc) · 个人维护

**AI 原生的 Agentic SDLC 框架：用本地 LLM 代理自动化软件开发生命周期**

以仓库模板形式提供的软件工程方法论：通过 Analyst/Architecture/Dev/QA/SecOps 等专职 Agent 与一个自我调优的 Meta-Agent，覆盖从需求到 DevOps 清单的 SDLC 各环节；采用 DDD、六边形架构、C4 模型与 Spec-Driven 流程，工件以 Markdown/Mermaid 形式 Everything-as-Code。模型无关但官方验证于 Qwen 2.5/3 与 GLM 4 本地模型。启动方式为复制仓库模板后在 Cursor/VS Code(Cline)/Windsurf 等 AI 编辑器中粘贴 BOOTSTRAP-PROMPT 触发交互式配置；限制：README 以方法论说明为主，无安装包或代码运行入口展示。

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

- 专职 Agent 角色分工（Analysis/Architecture/Dev/QA/SecOps）与自我调优 Meta-Agent
- Everything-as-Code：C4 模型、威胁模型、Runbook 均以 Markdown/Mermaid 生成
- Spec-Driven：未经验证的架构规格不生成代码
- 模型无关，官方验证于 Qwen 2.5/3(Coder) 与 GLM 4 本地部署

## 适用场景

- 以仓库模板发起新项目并让本地 LLM Agent 执行 SDLC 各环节
- 在私有基础设施上用开源权重模型开发，控制数据主权
- 以规格驱动与 Everything-as-Code 维护文档与架构一致性

## 场景标签

`Agent 框架` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L11: **Fast-ASDLC** is not just a collection of prompts; it is a complete engineering methodology designed for the AI er
> L24: - **Agentic Roles:** Specialized agents for Analysis, Architecture, Dev, QA, and SecOps.
> L51: Fast-ASDLC uses a **self-bootstrapping engine** powered by the **Meta-Agent**. You don't need to install heavy orch

## 星数曲线

```mermaid
xychart-beta
    title "shd-git/fast-asdlc 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-28 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `947fd8be1ef9` · [字段定义](../../DATASET.md)*
