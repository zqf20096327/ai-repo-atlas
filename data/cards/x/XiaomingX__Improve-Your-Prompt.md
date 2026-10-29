# XiaomingX/Improve-Your-Prompt

⭐ 44 · Python · Apache-2.0 · 推送 2026-02-01 · [GitHub](https://github.com/XiaomingX/Improve-Your-Prompt) · [官网](https://twitter.com/seclink) · 个人维护 · 中文 README

**用于优化 prompt 的元提示模板：自动生成专家人设**

一个元提示（meta-prompt）项目：将用户问题填入模板后，由语言模型生成针对该问题的专家 SystemPrompt（第二人称人设描述），再将生成的人设与原问题配合使用以获得回答。README 给出人设自动生成模板、小说家等示例及两步使用流程。代码部分基于 Python 3.11+ 与 uv 依赖管理运行，功能核心是提示文本模板本身。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 元提示模板：根据指令生成适合回答该指令的专家人设描述
- 两步用法：填入问题生成 SystemPrompt，再配合用户问题使用
- 提供 uv 管理的 Python 代码入口（uv run src/main.py）
- 附人设生成示例（环境科学家、小说家等）

## 适用场景

- 为自己的问题生成匹配的专家 SystemPrompt
- 用高能力模型为低能力模型优化提示
- 参考人设自动生成的提示写法

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: 什么是“元提示”？它是一种利用更智能的语言模型来生成或改进提示的技术。
> L7: 如何得到最好的结果，Improve-Your-Prompt是一个用于优化prompt的prompt

## 星数曲线

```mermaid
xychart-beta
    title "XiaomingX/Improve-Your-Prompt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-29 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1dae812e50cd` · [字段定义](../../DATASET.md)*
