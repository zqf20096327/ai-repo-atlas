# heavenaruba/codified-prompt-rule-engine

⭐ 123 · HTML · 推送 2026-10-22 · [GitHub](https://github.com/heavenaruba/codified-prompt-rule-engine) · 个人维护

**将原始指令转换为结构化提示词的元提示编排系统**

面向 LLM 使用者的提示词转换工具：通过五阶段流水线（意图映射、约束编织、认识分层、时间锚定、递归自纠注入）把原始指令转换为带语义标签、置信分区的结构化提示块；可按分析/创意/技术等模式与复杂度配置生成多个变体，并用余弦相似度和蕴含分析输出语义保真分数。README 仅给出 Python 导入示例代码与配置项说明，未见完整安装命令或运行入口；自述会增加 40-80% 提示长度、Crucible 优化需约 3 倍计算预算。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五阶段提示转换流水线（意图映射→约束编织→认识分层→时间锚定→自纠注入）
- 生成多个推理风格变体供选择
- 基于余弦相似度与蕴含分析的语义保真评分（建议低于 0.85 需人工调整）
- 输出结构化 XML 风格提示块，支持 14 种语言

## 适用场景

- 为研究综合、代码生成、客服脚本、法律分析等场景生成结构化提示
- 给高风险领域提示加入置信分区以约束模型输出范围
- 生成并比较多套推理风格变体后选用

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L5: A sophisticated meta-prompting orchestration system that transmutes base-level instructions into context-aware, sema
> L90: ```python

## 星数曲线

```mermaid
xychart-beta
    title "heavenaruba/codified-prompt-rule-engine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 122 --> 124
    line [123, 123]
```

2026-10-18 123 → 2026-10-23 123（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `5dc74d4711c7` · [字段定义](../../DATASET.md)*
