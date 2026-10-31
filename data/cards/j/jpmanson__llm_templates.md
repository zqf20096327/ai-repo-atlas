# jpmanson/llm_templates

⭐ 33 · Python · MIT · 推送 2026-08-13 · [GitHub](https://github.com/jpmanson/llm_templates) · 个人维护

**给 LLM 开发者的对话/指令模板格式化 Python 库**

Python 库 llm-templates，把带角色（user/assistant/system）的消息列表转换为与模型训练格式一致的输入字符串，也支持把模型输出反向解析回消息列表。内置 zephyr、llama2/3/3.1、mistral、gemma、cohere、phi3 等模板；对 HuggingFace 模型，在 tokenizer_config.json 可用时读取其 Jinja2 模板。通过 pip/uv 安装，要求 Python 3.10+，提供 Colab 快速上手笔记本。不负责模型推理本身，仅做提示格式转换。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置 zephyr/llama2/llama3/llama31/mistral/gemma/cohere/phi3 等模板
- HuggingFace 模型经 tokenizer_config.json 读取 Jinja2 模板
- 双向转换：消息列表→提示字符串，模型输出→消息列表

## 适用场景

- 推理前把多轮对话按模型训练格式拼成提示字符串
- 解析 LLM 输出文本回结构化消息列表
- 在本地或 HuggingFace 模型间切换时保持提示格式一致

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L4: It's a conversation formatter for chat models. The library allows you to easily format a chat conversation, with the
> L112: This is where `llm-templates` comes in. It is a Python package that provides a simple and flexible way to convert 

## 星数曲线

```mermaid
xychart-beta
    title "jpmanson/llm_templates 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-31 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `fe62a07dba54` · [字段定义](../../DATASET.md)*
