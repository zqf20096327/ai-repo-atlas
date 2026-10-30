# marcusgreen/moodle-qtype_aitext

⭐ 33 · PHP · 推送 2026-10-25 · [GitHub](https://github.com/marcusgreen/moodle-qtype_aitext) · [官网](https://moodle.org/plugins/qtype_aitext) · 个人维护

**Moodle 题型插件：用远程 LLM 批改自由文本答案**

Moodle 4.5+ 的自由文本问答题型，将学生答案提交给外部 LLM（如 ChatGPT 或自托管 Ollama）批改：每题自定义评分 prompt 与可选 marking scheme，AI 按设定的标准打分并给出反馈。批改通过两个独立的 companion question behaviour 插件实现，不覆盖 Moodle 核心行为，需随本插件一并安装；AI 不可用时批改优雅降级，不丢失答题记录。题面编辑表单带 AJAX prompt tester，可直接试 prompt。AI 反馈也可展示给人工批改者作参考。从 Moodle 插件市场安装，GPL v3 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每题自定义评分 prompt 与可选 marking scheme
- 通过两个专用 question behaviour 插件实现批改，与核心行为隔离
- AI 不可用时批改优雅降级，不丢答题记录
- 题面编辑表单内 AJAX prompt tester 可直接试 prompt

## 适用场景

- 在 Moodle 测验中用 AI 批改语言、写作类自由文本答案
- 设定自己的评分标准让 AI 按标准打分并给出解释性反馈
- 人工批改时参考 AI 生成的反馈

## 场景标签

 · 领域:教育/在线测评

## 证据(README 行号)

> L11: A Moodle question type that accepts free-text answers and grades them with a remote Large Language Model (LLM) such
> L30: 1. A **prompt** telling the AI how to evaluate the response.

## 星数曲线

```mermaid
xychart-beta
    title "marcusgreen/moodle-qtype_aitext 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-30 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6e7fa5bc21fd` · [字段定义](../../DATASET.md)*
