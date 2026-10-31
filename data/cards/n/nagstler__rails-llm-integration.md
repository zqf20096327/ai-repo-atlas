# nagstler/rails-llm-integration

⭐ 13 · Ruby · MIT · 推送 2026-03-14 · [GitHub](https://github.com/nagstler/rails-llm-integration) · 个人维护

**教 Claude Code 按 Rails 惯例编写 LLM 功能的技能包**

面向 Rails 开发者的 Claude Skill：将仓库复制到项目的 .claude/skills/ 目录后，Claude Code 读取其参考文档与模板，按统一约定生成 LLM 服务对象、后台任务、模型路由与预算配置等代码结构，覆盖重试、成本追踪、prompt 模板管理等场景。参考文档支持 ruby_llm、langchain-rb、ruby-openai、anthropic-rb 四种客户端方案，并附带代码库反模式审计脚本与 ERB prompt 模板、迁移模板。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 LLM::BaseService / BaseJob 模式，统一服务对象、重试规则与模型路由
- 参考文档覆盖 4 种 Ruby LLM 客户端（ruby_llm/langchain-rb/ruby-openai/anthropic-rb）
- 附带 generators、迁移模板与代码库 LLM 用法审计脚本
- 支持 Braintrust 评测管线与 CI 门的生成约定

## 适用场景

- 让 Claude Code 在 Rails 项目里生成结构一致的 LLM 服务代码
- 为已有散乱的 LLM 调用建立重试、成本追踪等约定
- 审计代码库中的 LLM 调用反模式

## 场景标签

`编码 Agent` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5:  A Claude Skill that teaches Claude Code how to write LLM features
> L34: > This skill gives Claude Code a set of Rails conventions for LLM calls so it generates consistent, structured code

## 星数曲线

```mermaid
xychart-beta
    title "nagstler/rails-llm-integration 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `5842afaaa553` · [字段定义](../../DATASET.md)*
