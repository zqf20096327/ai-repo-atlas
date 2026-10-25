# shrixtacy/Ai-Council

⭐ 32 · Python · MIT · 推送 2026-03-31 · [GitHub](https://github.com/shrixtacy/Ai-Council) · [官网](https://pypi.org/project/ai-council-orchestrator/1.0.0/) · 个人维护

**多 AI 模型编排库：把模型当专门 agent 协调路由与仲裁**

Python 库，协调多个 AI 模型完成复杂任务：将模型视为具有不同能力与成本特征的专门 agent，通过 5 层架构（分析、路由、执行、仲裁、综合）自动路由任务、仲裁冲突输出、做成本优化与失败降级。提供成本/时间估算、ConfigBuilder 自定义配置、系统状态监控，并带本地 Web 界面（配置 Gemini、xAI Grok 等模型 key 后运行）。以 pip 包发布，含 95 个单元测试与示例脚本，面向需要在多模型间做编排与容错的开发者。

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

- 5 层架构：分析、路由、执行、仲裁、综合
- 成本/时间预估与成本上限、并行度等可配置项
- 冲突仲裁与失败降级机制（熔断器）
- 附带 Web 界面与示例脚本、95 个单元测试

## 适用场景

- 在多个 LLM 之间按任务类型自动路由与编排
- 对多模型输出做冲突仲裁与综合
- 按预算与质量要求控制多模型调用成本

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L24: AI Council is a revolutionary Python-based system that intelligently coordinates multiple specialized AI models to 
> L131: AI Council follows a sophisticated **5-layer architecture** designed for production use:
> L137:  C --> D[⚡ Execution Layer]

## 星数曲线

```mermaid
xychart-beta
    title "shrixtacy/Ai-Council 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-25 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1350473fa6f6` · [字段定义](../../DATASET.md)*
