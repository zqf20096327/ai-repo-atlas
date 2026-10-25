# simonw/llm-plugin

⭐ 32 · Python · 推送 2026-10-12 · [GitHub](https://github.com/simonw/llm-plugin) · 个人维护

**LLM 插件开发的 cookiecutter 脚手架模板**

为 simonw 的 LLM 命令行工具生成插件项目骨架的 cookiecutter 模板：运行 cookiecutter gh:simonw/llm-plugin 后按提示填写插件名、描述、作者等信息，自动生成目录结构与默认配置，并预置 pytest 测试。生成的插件可通过 `llm install -e .` 以可编辑模式安装，用 `llm plugins` 确认加载。前提是本机已安装 cookiecutter（可用 pipx/pip/uv 安装）。面向为 LLM 编写扩展插件的开发者。

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

- 交互式提示生成插件目录结构与命名（连字符/下划线自动转换）
- 生成项目可通过 `llm install -e .` 可编辑安装
- 预置 pytest 测试与开发环境说明

## 适用场景

- 为 LLM 命令行工具快速搭建新插件项目
- 按模板生成带测试的插件开发起点

## 场景标签

 · 领域:LLM 开发工具/脚手架

## 证据(README 行号)

> L1: # llm-plugin cookiecutter template
> L3: A cookiecutter template for creating new llm plugins.

## 星数曲线

```mermaid
xychart-beta
    title "simonw/llm-plugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-25 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `00fa95de39a6` · [字段定义](../../DATASET.md)*
