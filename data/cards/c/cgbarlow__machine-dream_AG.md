# cgbarlow/machine-dream_AG

⭐ 22 · TypeScript · 推送 2026-01-24 · [GitHub](https://github.com/cgbarlow/machine-dream_AG) · 个人维护

**持续机器认知研究平台：以数独为测试床的 LLM 经验学习与梦境巩固**

以纯 LLM 推理（无提示无回退）游玩数独并从对错经验中学习的认知研究平台。核心机制为 GRASP 循环（Generate→Review→Absorb→Synthesize→Persist）、5 阶段梦境巩固管线与 SQLite 认知记忆（AgentDB）；经验经 FastCluster/DeepCluster/LLMCluster 聚类合成为可跨会话迁移的学习单元，并从失败中提取反模式与推理修正。支持 LM Studio、OpenAI、Anthropic、Ollama、OpenRouter 等 profile 配置与 AISP 提示校验，提供 CLI 与批量 A/B 测试脚本；TUI 组件标注为实验性。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯 LLM 数独推理，无提示、无确定性回退
- 5 阶段梦境巩固管线产出可迁移的学习单元
- 三种聚类算法（FastCluster/DeepCluster/LLMCluster）带版本化
- 失败学习：反模式提取与推理修正，默认启用

## 适用场景

- 研究 LLM 在持续会话间的经验积累与知识巩固
- 对比有无学习单元的模型表现（A/B 测试）
- 试验多 provider 配置下的认知实验流水线

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L5: An AI system that learns from experience, consolidates knowledge during "dream cycles," and improves continuously ac
> L9: Machine Dream demonstrates **continuous cognition**: AI models that think, learn, and remember across sessions witho
> L160: Profiles for LM Studio, OpenAI, Anthropic, Ollama, OpenRouter, or any OpenAI-compatible API.

## 星数曲线

```mermaid
xychart-beta
    title "cgbarlow/machine-dream_AG 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28", "2026-10-31"]
    y-axis "stars" 20 --> 23
    line [22, 21, 22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `93660b959512` · [字段定义](../../DATASET.md)*
