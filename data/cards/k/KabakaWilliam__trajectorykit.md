# KabakaWilliam/trajectorykit

⭐ 14 · Python · MIT · 推送 2026-03-26 · [GitHub](https://github.com/KabakaWilliam/trajectorykit) · [官网](https://pypi.org/project/trajectorykit/) · 个人维护

**本地运行的深度研究 agent 框架，产出带溯源的研究报告**

面向研究者的极简深度研究 agent 框架：单 YAML 配置驱动，编排器负责拉取 Apptainer 容器镜像、启动沙箱与 vLLM 服务、运行评测与判分。研究引擎默认本地部署 GPT-OSS-20B，可选 GPT-5.4 作为精修层。机制包括递归子 agent 委派、多级搜索/抓取回退、五阶段验证管线、防循环安全门与全量执行 trace（HTML 可视化）。在 Deep Research Bench 报告排名第六（0.5496）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单 YAML 配置完成模型、GPU、vLLM、沙箱、数据集与判分的编排
- 递归子 agent 委派与五阶段验证（rubric 生成 + 质量审计/抽查/引用审计等）
- 默认本地 GPT-OSS-20B，可选 GPT-5.4 四阶段精修管线
- 每轮完整 trace 记录并生成交互式 HTML

## 适用场景

- 在本地跑 PhD 级深度研究任务并得到带引用审计的报告
- 复现或扩展 Deep Research Bench 评测
- 以最小开源模型栈控制推理成本开展自动化研究

## 场景标签

`Agent 框架` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L3: > A **minimal deep research agent harness** for running LLM agents with recursive sub-agents, sandboxed code executi
> L48: TrajectoryKit is rigorously evaluated on **Deep Research Bench**, a benchmark with 100 PhD-level research tasks acr
> L92: - **One config, one command.** Single YAML file specifies everything: model, GPU setup, vLLM config, sandbox, datas

## 星数曲线

```mermaid
xychart-beta
    title "KabakaWilliam/trajectorykit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `35db5a4273dd` · [字段定义](../../DATASET.md)*
