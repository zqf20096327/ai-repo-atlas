# HelgeSverre/toon-php

⭐ 131 · PHP · MIT · 推送 2026-09-06 · [GitHub](https://github.com/HelgeSverre/toon-php) · [官网](https://github.com/HelgeSverre/toon-php) · 个人维护

**PHP 库：TOON 紧凑数据格式编解码，降低发给 LLM 的 token 消耗**

toon-format/toon 的 PHP 移植，提供 TOON 格式的编码与双向解码：PHP 数组可编码为 TOON 字符串、也可解码还原。均匀对象数组采用表头式表格式编码（字段名声明一次），声明在此获得相比 JSON 更大的 token 节省。支持验证、DateTime/Enum 自动转换、全局辅助函数、缩进配置等。要求 PHP 8.1+，通过 Composer 安装。README 明确其面向 LLM 上下文优化，不作为 API 或存储中 JSON 的替代。附带 OpenAI PHP、Laravel+Prism、Anthropic/Claude、Ollama 等集成教程。

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

- TOON 格式的编码、双向解码与验证 API
- 均匀对象数组的表格式编码：字段名在表头声明一次
- DateTime 转 ISO 8601、PHP Enum 自动规范化、非有限数值转 null
- 提供 OpenAI/Laravel+Prism/Anthropic/Ollama 集成教程

## 适用场景

- 把结构化数据压缩后放进 LLM prompt，减少 token 花费
- 提高 LLM 上下文窗口的利用率
- 让 AI 对话中的数据更易读

## 场景标签

 · 领域:LLM 基础设施/数据序列化

## 证据(README 行号)

> L8: A PHP port of toon-format/toon - a compact data format designed to reduce token
> L252: - Sending structured data in LLM prompts
> L257: **Note**: TOON is optimized for LLM contexts and is not intended as a replacement for JSON in APIs or data storage

## 星数曲线

```mermaid
xychart-beta
    title "HelgeSverre/toon-php 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 130 --> 132
    line [131, 131]
```

2026-10-18 131 → 2026-10-26 131（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `c8b40845affb` · [字段定义](../../DATASET.md)*
