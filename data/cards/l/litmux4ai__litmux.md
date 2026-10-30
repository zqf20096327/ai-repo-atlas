# litmux4ai/litmux

⭐ 108 · Python · MIT · 推送 2026-05-21 · [GitHub](https://github.com/litmux4ai/litmux) · [官网](https://litmux.dev) · 组织维护

**LLM 提示词单元测试与模型比选 CLI 工具**

Python CLI 工具，面向开发 AI 功能的团队：以 YAML 配置编写对 LLM 调用的 pass/fail 断言（contains/regex/json-schema/llm-judge 等类型），支持 litmux run 批量测试、eval 数据集评测、generate 用 AI 生成测试数据集、cost 按调用量做成本预估、compare 并排对比模型输出。可配置 openai/anthropic/google/huggingface 多家 provider，接入 GitHub Actions CI，CLI 完全离线可用，云端面板为可选的私有 beta 功能。

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

- YAML 配置的提示词单元测试，8 种断言类型（含 llm-judge 与成本/延迟阈值）
- 跨模型成本预估：按调用量找出通过测试的最便宜模型
- AI 生成测试数据集（litmux generate）
- CLI 完全离线运行，云端同步为可选 opt-in

## 适用场景

- 给 LLM 提示词写回归测试，防止改动引入退化
- 在多个模型间比较输出质量与成本后做选型
- 把 LLM 测试接入 CI/CD 流程

## 场景标签

`提示工程` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L3: Unit tests for AI. Test prompts, compare models, catch regressions.
> L41: ### `litmux eval` — bulk evaluation against datasets

## 星数曲线

```mermaid
xychart-beta
    title "litmux4ai/litmux 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 107 --> 109
    line [108, 108]
```

2026-10-18 108 → 2026-10-30 108（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `0453060f14b5` · [字段定义](../../DATASET.md)*
