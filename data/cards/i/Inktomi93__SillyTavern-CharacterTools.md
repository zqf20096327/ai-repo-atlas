# Inktomi93/SillyTavern-CharacterTools

⭐ 25 · TypeScript · AGPL-3.0 · 推送 2026-01-03 · [GitHub](https://github.com/Inktomi93/SillyTavern-CharacterTools) · 个人维护

**给 SillyTavern 用户的角色卡 AI 评分/改写/比对扩展**

SillyTavern 第三方扩展，用 LLM 对角色卡执行 Score→Rewrite→Analyze 三阶段流水线：按字段（description、personality、first message 等）给出 1-10 评分与改进建议，据反馈生成改写版本，再比对原版判定是否丢失角色特质（ACCEPT/NEEDS_REFINEMENT/REGRESSION），支持迭代与一键回退。支持 JSON Schema 结构化输出、提示词预设、字段级选择与 Markdown 导出。要求 SillyTavern 1.12.0+ 与已连接的 Chat Completion API（OpenRouter/OpenAI/Claude 等）；Text Completion 未测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 字段级评分与改进建议（1-10 分）
- 改写后与原版比对，判定保留/丢失内容与三档结论
- 迭代历史与一键回退，可仅处理选定字段
- JSON Schema 结构化输出，可用自然语言生成 schema

## 适用场景

- 改进我的角色卡质量，逐字段获得反馈
- 重写角色卡后核验是否偏离原角色
- 批量按自定义评分标准程序化处理角色卡结果

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: **An LLM-powered extension for analyzing, scoring, and iteratively improving character cards.**
> L11: Character Tools runs your character cards through a three-stage pipeline:
> L350: - SillyTavern 1.12.0+

## 星数曲线

```mermaid
xychart-beta
    title "Inktomi93/SillyTavern-CharacterTools 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `e16ea6e0e371` · [字段定义](../../DATASET.md)*
