# jlowin/vibecheck

⭐ 43 · Python · 推送 2026-09-24 · [GitHub](https://github.com/jlowin/vibecheck) · 组织维护

**Python SDK：一次函数调用接入决策模型做判断类问题**

面向开发者的 Python 库，封装 Typesafe 提供的决策模型（如 Jev）调用：提供 check/classify/label/score 四个函数，分别回答是否、单选、多选、量表评分，每次返回普通 Python 值并附带概率，支持阈值、三态不确定输出、批处理与 filter/group 列表操作。通过环境变量 API key 访问 console.typesafe.ai 或兼容 provider。限制：决策模型不生成文本、不做算术计数。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- check/classify/label/score 四函数返回普通 Python 值与概率
- 阈值与三态不确定（low,high 区间返回 None）机制
- 同一数据多问题批量请求，测试中 100 问约 1% token 开销
- 选项可为字符串/Enum/函数/Pydantic 模型，自动生成标签与描述

## 适用场景

- 在业务代码中做意图、语气、紧急度等快速判断
- 工单路由、内容多标签分类、评论量表打分
- 用自然语言判断替代手写启发式规则并保留概率信号

## 场景标签

 · 领域:AI 应用开发/SDK

## 证据(README 行号)

> L5: vibecheck lets you drop decision models right into your Python code.
> L7: Decision models such as Jev are a new kind of AI model built for judgment calls. They answer typed questions (yes or
> L9: vibecheck puts all of that one function call away. Each call returns a plain Python value, with no prompts to templa

## 星数曲线

```mermaid
xychart-beta
    title "jlowin/vibecheck 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-26 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3f4abfc0e135` · [字段定义](../../DATASET.md)*
