# zgornel/DataLinter

⭐ 19 · Julia · MIT · 推送 2026-10-28 · [GitHub](https://github.com/zgornel/DataLinter) · 个人维护

**面向 ML 工作流的数据与代码 linting 库与工具**

用 Julia 编写的上下文 linting 库，开发起点是用 Julia 重写 Google 的 data linter，并在此基础上支持数据上下文（如代码片段、分析类型信息），以检测更复杂的数据与代码质量概念问题。内置 27 个数据+代码 linter（含 Google 原 linter），支持 CSV/Parquet/Arrow 数据集、tree-sitter 的 R 代码解析、可定制规则引擎，提供 CLI 与 HTTP server 两种零配置运行模式。分发方式包括含编译产物的 Docker 镜像、Linux x86-64 预编译二进制与 Julia 包安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 27 个数据+代码 linter（含 Google 原 linter）
- 支持 CSV/Parquet/Arrow 数据集与 Text/JSON/HTML 输出
- tree-sitter 代码解析实现 R 语言一级支持
- CLI 与 HTTP server 双模式，零配置运行

## 适用场景

- ML 流水线中自动检查数据集与配套代码质量问题
- 在 RStudio/VSCode/Jupyter/CI 中集成数据 lint 检查
- 按分析类型上下文检测数据概念性问题

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L3: Linting library and tools for machine learning, statistical modelling, data, code.
> L20: **DataLinter** is a library for contextual linting of data and code. Its development started by rewriting Google's 

## 星数曲线

```mermaid
xychart-beta
    title "zgornel/DataLinter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `2b6ba54c1446` · [字段定义](../../DATASET.md)*
