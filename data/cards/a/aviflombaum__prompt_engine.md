# aviflombaum/prompt_engine

⭐ 79 · Ruby · MIT · 推送 2026-08-05 · [GitHub](https://github.com/aviflombaum/prompt_engine) · 个人维护

**Rails 引擎：集中管理 LLM 提示词，支持版本控制与 A/B 测试**

以 Rails Engine 形式嵌入应用的提示词管理系统：提供挂载在 /prompt_engine 的管理界面，团队可在其中创建、版本化、测试提示词而无需部署代码变更。机制上自动检测 {{variables}} 生成类型化参数，每次保存生成新版本并支持一键回滚，内置 Playground 用真实 LLM 供应商测试，API 密钥经 Rails 加密存储。渲染 API 返回 RenderedPrompt 实例，可转换为 OpenAI 或 RubyLLM/Anthropic 参数格式。README 声明处于活跃开发期，不保证向后兼容。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 提示词自动版本化与一键回滚，管理界面修改无需部署代码
- 自动检测 {{variables}} 并生成类型化参数
- 内置 Playground 以真实 LLM 供应商测试提示词
- 支持 A/B 测试与评估集（EvalSet/TestCase 模型）
- API 密钥经 Rails 加密存储

## 适用场景

- 在 Rails 应用中集中管理团队的 LLM 提示词
- 对提示词做多版本 A/B 测试并跟踪性能
- 不发布代码即可更新线上提示词

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: A powerful Rails engine for managing AI prompts with version control, A/B testing, and seamless LLM
> L4: integration. PromptEngine provides a centralized admin interface where teams can create, version,
> L21: - **A/B Testing**: Test different prompt variations with built-in evaluation tools

## 星数曲线

```mermaid
xychart-beta
    title "aviflombaum/prompt_engine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 78 --> 80
    line [79, 79]
```

2026-10-18 79 → 2026-10-24 79（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `af6bc4d20b6d` · [字段定义](../../DATASET.md)*
