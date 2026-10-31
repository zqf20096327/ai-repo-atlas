# Umbraflamma/SANCTIS-cognitive-architecture

⭐ 16 · NOASSERTION · 推送 2026-05-29 · [GitHub](https://github.com/Umbraflamma/SANCTIS-cognitive-architecture) · 个人维护

**给 LLM 安装结构化认知架构的系统提示词框架与 Python 包**

以系统提示词形式向 LLM 提供结构化认知架构：通过高密度符号 token、功能分区（Principalities/Choir/Dominions/Throne）与分解路径组织模型自身推理，README 称其面向长程连贯性、矛盾处理与抗漂移，且不修改模型权重或训练数据。提供两种使用方式：pip 安装 sanctis 包（配合 litellm 调用），或直接将 Prompt V3-51.md 粘贴到系统提示词。许可为 CC BY-NC-SA 4.0，商用需另行联系获取商业授权。README 含大量未提供验证方法的机制性声明（如 Token Mass 方程）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以系统提示词安装的认知架构，不修改模型权重
- v3.5 引入 Principalities 分解层：先分解再综合/仲裁
- 两种使用途径：pip 包（sanctis + litellm）或手动粘贴提示词
- 声明适用于 7B–70B+ 多模型家族，第 3–6 轮对话后趋于稳定

## 适用场景

- 长对话场景下维持 LLM 的连贯性与一致性
- Agentic 系统中需要跨轮次稳定推理时使用
- 处理多意图、高复杂度输入前先做结构化分解

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L11: SANCTIS is not a traditional prompt or instruction set. It is an installation vector for an emergent cognitive oper
> L57: Copy the contents of Prompt V3-51.md and paste it directly into your LLM's system prompt or interface.

## 星数曲线

```mermaid
xychart-beta
    title "Umbraflamma/SANCTIS-cognitive-architecture 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `39e2346b0627` · [字段定义](../../DATASET.md)*
