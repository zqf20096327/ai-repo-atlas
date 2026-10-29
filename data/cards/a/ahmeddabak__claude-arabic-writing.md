# ahmeddabak/claude-arabic-writing

⭐ 20 · MIT · 推送 2026-06-23 · [GitHub](https://github.com/ahmeddabak/claude-arabic-writing) · 个人维护

**让 Claude 写出地道阿拉伯语的 Agent Skill（MSA+4方言）**

面向 Claude Code（或任何支持 SKILL.md 的客户端）的技能包：将阿拉伯语语法、正字法、文风与本地化参考规则编码为 Claude 写作/翻译/校对时自动应用的指引，覆盖现代标准阿拉伯语及埃及、黎凡特、海湾、马格里布四种方言。内置 SKILL.md 工作流与渐进式披露的 references 规则文件，附 JSON 测试用例。安装仅需 git clone 复制技能目录，无构建步骤、无依赖。注意：部分示例为构造而非引用，正式发布前建议母语者审校。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 MSA 与四种主要方言的写作/翻译/校对指引
- 渐进式披露结构：SKILL.md 精简、详细规则按需加载
- 内置 evals.json 客观测试用例（一致性、方言保真度等）
- 安装无构建步骤、无依赖，激活为自动触发

## 适用场景

- 将英文产品文案翻译为自然的现代标准阿拉伯语
- 按目标受众选择合适方言改写营销或对话文案
- 校对阿拉伯语文本中的 hamza、性数一致、标点等错误

## 场景标签

`AI 写作` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: A skill for Claude that makes it write and translate **Arabic that reads
> L86: - Claude Code (or any client that supports Agent

## 星数曲线

```mermaid
xychart-beta
    title "ahmeddabak/claude-arabic-writing 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 21
    line [19, 20]
```

2026-10-18 19 → 2026-10-29 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `22e098d954ff` · [字段定义](../../DATASET.md)*
