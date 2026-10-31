# hev/vibecheck

⭐ 22 · TypeScript · NOASSERTION · 推送 2026-01-14 · [GitHub](https://github.com/hev/vibecheck) · [官网](https://vibescheck.io/) · 组织维护

**面向任意 LLM 的 YAML 评测 CLI 框架，供开发者快速跑评估**

vibecheck 是一个用 npm 安装的命令行 agent 评测框架：以 YAML DSL 定义评估（支持 match/not_match/or/token 约束/semantic 嵌入相似度/llm_judge 等 7 类检查），可对 openai、anthropic 等多家模型运行评测并做多模型对比、按 price-performance 排序查看结果；提供 suite 保存、变量与密钥管理、MCP 工具调用测试、程序化 API（含 Jest 扩展）与 Claude Code 集成文档。限制：目前为邀请制开发者预览，需在 vibescheck.io 申请 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- YAML DSL 定义评估，7 种检查类型（含 semantic 嵌入相似度与 llm_judge）
- 多模型对比评测，按 price-performance 排序结果
- 支持 MCP 工具调用测试与密钥管理
- 提供程序化 API 与 Jest expect 扩展

## 适用场景

- 从命令行对我的 agent/LLM 跑 YAML 定义的回归评测
- 对比多个模型在同一评估集上的成功率与性价比
- 在 CI/Jest 测试中集成 LLM 评测断言

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L8: **An agent evaluation framework for any LLM** - A simple and intuitive YAML based DSL for agent evals.
> L10: vibecheck makes it easy to evaluate any language model with a simple YAML configuration. Run evals, save the result

## 星数曲线

```mermaid
xychart-beta
    title "hev/vibecheck 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `b18d245c9915` · [字段定义](../../DATASET.md)*
