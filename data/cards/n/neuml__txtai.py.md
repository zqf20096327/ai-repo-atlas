# neuml/txtai.py

⭐ 16 · Python · Apache-2.0 · 推送 2026-10-06 · [GitHub](https://github.com/neuml/txtai.py) · 组织维护

**txtai API 的 Python 客户端绑定库**

txtai 是面向语义搜索、LLM 编排与语言模型工作流的 AI 框架，本仓库提供其 API 的 Python 绑定：一个最小依赖的 Python 库，适用于 txtai 以 API 服务形式运行的场景，通过该客户端连接并调用 API 实例。README 明确说明其他情况下应直接安装 txtai 本体。安装方式为 PyPI（pip install txtai.py），examples 目录提供嵌入、抽取式问答、零样本分类、pipeline 与 workflow 等示例脚本，需先启动 txtai API 实例后运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- txtai API 的 Python 绑定，最小依赖设计
- 仅适用于 txtai 以 API 服务形式运行的场景
- examples 目录含嵌入/QA/零样本分类/工作流示例

## 适用场景

- 在 Python 中调用远程运行的 txtai API 服务
- 通过示例脚本了解 txtai 的功能范围
- 已有 txtai API 实例时以轻量客户端接入

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L16: txtai is an all-in-one AI framework for semantic search, LLM orchestration and language model workflows.
> L18: This repository contains Python bindings for the txtai API. This is a minimal dependency library for Python designe
> L35: txtai.py connects to a txtai api instance. See this link for details on how to start a new api instance.

## 星数曲线

```mermaid
xychart-beta
    title "neuml/txtai.py 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `ec3e786e3bee` · [字段定义](../../DATASET.md)*
