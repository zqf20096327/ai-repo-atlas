# hyeonsangjeon/gdpval-realworks

⭐ 28 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/hyeonsangjeon/gdpval-realworks) · [官网](https://hyeonsangjeon.github.io/gdpval-realworks/) · 个人维护 · 中文 README

**面向 220 个真实职业任务的 LLM 评测流水线与证据仪表盘**

基于 GDPVal Gold Subset 构建的可复现实验流水线与静态 React 证据仪表盘：YAML 定义实验，GitHub Actions 执行配置→执行→产物保全→评分→对比的闭环，任务要求模型产出电子表格、报告、演示文稿等可审查文件。区分执行完成、产物完整性、Self-QA 与外部评分四种信号；支持 provider-hosted code_interpreter、subprocess、Docker sandbox、json_renderer 四种执行模式，记录逐任务成本。本地预览仅需 Node.js，无需云凭证；云端实验需 Azure OIDC、HF token 与 API 预算。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 220 个任务覆盖 9 个行业部门、44 种职业，要求产出可审查文件
- 配置→执行→保全证据→评分→对比的可复现流水线（YAML + GitHub Actions）
- 四种执行模式：code_interpreter / subprocess / Docker sandbox / json_renderer
- 分离四种评测信号并记录逐任务成本，仪表盘可查实验排行与产物明细

## 适用场景

- 在真实职业任务上对 LLM 做可复现评测实验
- 查阅各模型在 9 个行业部门的任务完成与外部评分结果
- 审查每次实验的产物、失败与成本证据

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5:  Benchmark LLMs on real expert work, not toy prompts.
> L90: This repository turns those tasks into a repeatable loop:
> L91: **configure -> execute -> preserve evidence -> grade -> compare**. A YAML file

## 星数曲线

```mermaid
xychart-beta
    title "hyeonsangjeon/gdpval-realworks 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-31 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `d11b7a330b2e` · [字段定义](../../DATASET.md)*
