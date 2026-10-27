# yuanzhw/AI-bioworkflow

⭐ 96 · Python · Apache-2.0 · 推送 2026-10-15 · [GitHub](https://github.com/yuanzhw/AI-bioworkflow) · [官网](https://yuanzhw.com) · 个人维护 · 中文 README

**面向生信分析的 LLM 规划约束型工作流编译器，生成可审计 WDL 1.0**

将自然语言或结构化生信需求约束为 Catalog 校验的 Recipe Tool Plan，经类型化 Workflow IR 由确定性编译器（Analyzer + Python/Jinja2 Renderer）生成并用 WOMtool 92 / miniwdl 验证 WDL 1.0。模型只负责规划，不直接写 WDL；工具版本、容器等以 Catalog 为权威来源，失败修复可回放。提供 FastAPI、SQLite run history、Next.js DAG 工作台与在线 RNA-seq demo；公开实例默认禁用真实执行，无登录/多租户等生产级能力。结构化入口可绕过模型与 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 自然语言 → Catalog-bound Plan → Workflow IR → 确定性生成 WDL 1.0，CI 强制 WOMtool/miniwdl 校验
- Catalog 作为工具/版本/容器权威来源，编译器不猜测或静默替换镜像
- 结构化输入路径无需 API key，输出确定性可复现
- FastAPI + SQLite run history + Next.js DAG 工作台，含公开 demo

## 适用场景

- 从自然语言或结构化需求生成可审计的生信 WDL 工作流
- 复现 RNA-seq 差异表达分析路径（fastp→Salmon→tximport→DESeq2→MultiQC）
- 审查 LLM 生成工作流的计划、诊断与证据链

## 场景标签

`工作流自动化` `代码生成` · 领域:效率与自动化

## 证据(README 行号)

> L22: - **模型负责规划，不负责写最终 WDL。** 自然语言先变成带 schema 的 Recipe Tool Plan；结构化入口可以完全绕过模型和 API key。
> L24: - **编译与验证保持确定性。** Workflow IR 先经 Analyzer 检查，再由 Python/Jinja2 Renderer 生成 WDL；WOMtool 92 是与 Cromwell 92 对齐的主校验器。

## 星数曲线

```mermaid
xychart-beta
    title "yuanzhw/AI-bioworkflow 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 95 --> 98
    line [97, 96, 96]
```

2026-10-18 97 → 2026-10-27 96（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `9dc8cabb5ea1` · [字段定义](../../DATASET.md)*
