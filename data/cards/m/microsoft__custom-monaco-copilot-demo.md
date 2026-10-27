# microsoft/custom-monaco-copilot-demo

⭐ 52 · JavaScript · MIT · 推送 2026-09-07 · [GitHub](https://github.com/microsoft/custom-monaco-copilot-demo) · 组织维护

**微软示例：基于 Monaco 与 OpenAI API 的 AI 辅助代码编辑器**

演示用代码示例，实现基于 Monaco 编辑器的 AI 辅助编辑器：通过 OpenAI API 提供上下文感知的代码补全（Ctrl/Alt+Space 触发），并包含 XML 校验与错误高亮（XmlValidator）、自定义主题（MonacoTheme）和用于询问代码与修复语法错误的聊天界面（ChatBox）。面向希望在 Monaco 网页 IDE 中接入 AI 能力的开发者。README 明确声明仅供演示与教学，不适用于生产环境；运行需在应用中配置 OpenAI API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 OpenAI API 的上下文感知代码补全（快捷键触发）
- XML 校验与错误高亮（XmlValidator）
- 与编辑器集成的聊天界面，可诊断并修复语法错误
- Monaco 自定义主题配置

## 适用场景

- 学习如何在 Monaco 编辑器中接入 OpenAI API 做代码补全
- 参考实现自定义网页 IDE 的 AI 聊天与语法诊断功能
- 教学演示 AI 辅助代码编辑器的组成模块

## 场景标签

`代码生成` `教程课程` · 领域:编码与开发

## 证据(README 行号)

> L3:  This repository contains a sample implementation of an AI-assisted code editor that provides intelligent code sugge
> L48: The `CodeSuggestions` feature provides context-aware code completion suggestions using the OpenAI API. It is implem
> L70: > This is strictly for demonstration and educational purposes, and is not intended or appropriate for production us

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/custom-monaco-copilot-demo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-18 52 → 2026-10-27 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `4b4a560ce2dd` · [字段定义](../../DATASET.md)*
