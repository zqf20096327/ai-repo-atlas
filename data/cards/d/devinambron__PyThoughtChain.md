# devinambron/PyThoughtChain

⭐ 20 · Python · 推送 2026-02-18 · [GitHub](https://github.com/devinambron/PyThoughtChain) · 个人维护

**基于 OpenAI API 的思维链对话应用，面向本地 LLM**

Python 实现的聊天应用，通过 OpenAI API 接入 LLM，按用户输入判定任务类型（产品开发、科研、创意写作、编程、通用），以结构化提示工程生成思维链，包含基于关键词与迭代进度的置信度评分、文本思维导图可视化、用户逐轮反馈迭代与流式响应。项目已归档：作者说明其构建于 2024 年 9 月、早于原生推理模型出现，现主要适用于本地 LLM 部署（LM Studio、Ollama）与 7B–13B 小模型及教学参考。安装方式为 git clone 后运行 setup.py，实测环境为 M1 Pro Max 上的 LM Studio + Llama3.1-8B。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 按任务类型（5 类）生成结构化思维链
- 基于关键词与迭代进度的置信度评分决定迭代停止
- 文本思维导图可视化与用户逐轮反馈迭代
- 支持流式响应，兼容本地 LLM（LM Studio、Ollama）

## 适用场景

- 在本地小模型上获得结构化的思维链推理
- 产品开发或科研中辅助头脑风暴与假设设计
- 学习推理模型出现前的思维链提示工程实现

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L20: PyThoughtChain is a Python-based chat application that utilizes the OpenAI API to provide a conversational interfac
> L26: - Determines the appropriate task type (product development, scientific research, creative writing, coding, or gene

## 星数曲线

```mermaid
xychart-beta
    title "devinambron/PyThoughtChain 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `35cae00bf2a4` · [字段定义](../../DATASET.md)*
