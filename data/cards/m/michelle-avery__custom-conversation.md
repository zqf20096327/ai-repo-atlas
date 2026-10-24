# michelle-avery/custom-conversation

⭐ 98 · Python · MIT · 推送 2026-10-18 · [GitHub](https://github.com/michelle-avery/custom-conversation) · 个人维护

**面向 Home Assistant 用户的高度可配置 LLM 对话组件**

Home Assistant 的自定义对话 agent 集成：通过 LiteLLM 兼容多家 LLM 提供商，支持配置备用提供商、动态修改 API 设置、细粒度提示词自定义、意图处理配置，以及实验性的 Langfuse 提示词管理与追踪。可启用内置意图匹配 agent 与 LLM agent 双通道，内置优先、失败后转 LLM。提供事件总线对话事件便于调试分析。通过 HACS 或手动复制文件安装，UI 内完成配置。限制：Langfuse 集成为实验性且不支持 Home Assistant 模板。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 经 LiteLLM 兼容多家 LLM 提供商，支持配额耗尽后自动回退备用提供商
- 提示词拆分为可配置组件，支持自定义意图暴露与回退行为
- 内置 agent 与 LLM agent 双通道处理（内置优先，失败转 LLM）
- Langfuse 提示词管理、追踪与评分集成（实验性）

## 适用场景

- 对 Home Assistant 语音助手的 LLM 交互做细粒度定制
- 免费低配额 LLM 为主、付费为备的成本控制
- 通过 Langfuse 追踪与评分分析助手对话表现

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L3: A highly configurable conversation agent for Home Assistant, designed for users who want fine-grained control over t
> L10: - Compatible with multiple LLM providers, via LiteLLM. See Supported Providers for the list of supported providers.
> L75: * Enabling the LLM Agent enables interaction with Large Language models

## 星数曲线

```mermaid
xychart-beta
    title "michelle-avery/custom-conversation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 97 --> 99
    line [98, 98]
```

2026-10-18 98 → 2026-10-24 98（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `9d5eb15e697a` · [字段定义](../../DATASET.md)*
