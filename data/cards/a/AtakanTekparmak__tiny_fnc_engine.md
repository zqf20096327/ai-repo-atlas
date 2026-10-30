# AtakanTekparmak/tiny_fnc_engine

⭐ 37 · Python · Apache-2.0 · 推送 2026-08-13 · [GitHub](https://github.com/AtakanTekparmak/tiny_fnc_engine) · [官网](https://pypi.org/project/tiny-fnc-engine/) · 个人维护

**解析并执行 LLM 输出函数调用的极简 Python 引擎**

单文件 212 行的 Python 库，用于解析 LLM 输出中 JSON 格式的函数调用并执行：支持动态添加函数、链式调用、函数输出存储与参数引用，支持 Pydantic 模型做参数与返回值的类型校验，并可解析 OpenAI 兼容的 tool_calls 格式。面向在 agent/tool-use 场景中需要轻量函数调用层的开发者。可从 PyPI 安装，也可直接下载单文件使用，需 Python 3.10+ 与 Pydantic；README 提示用户须对载入解释器的函数自行负责。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单文件 212 行，可直接下载嵌入项目
- 链式函数调用与输出存储/参数引用
- Pydantic 模型参数与返回值类型校验
- 解析 OpenAI 兼容 tool_calls 格式

## 适用场景

- LLM agent 项目中执行模型输出的函数调用
- 需要函数间参数传递的多步工具调用
- 作为轻量依赖嵌入不想引入大型框架的项目

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: tiny_fnc_engine is a minimal python library (one file, 212 lines of code) that provides a flexible engine for callin
> L13: - Parse & call functions from OpenAI compatible "tool_calls" format

## 星数曲线

```mermaid
xychart-beta
    title "AtakanTekparmak/tiny_fnc_engine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-30 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `0e48ed24bb3e` · [字段定义](../../DATASET.md)*
