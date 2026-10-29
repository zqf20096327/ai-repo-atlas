# EconSolider/dynare-copilot

⭐ 24 · AMPL · MIT · 推送 2026-07-16 · [GitHub](https://github.com/EconSolider/dynare-copilot) · 个人维护 · 中文 README

**面向 DSGE 建模者的 Claude Code/Codex 技能：把宏观直觉转为经验证的 Dynare .mod 文件**

一个标准 Agent Skill（SKILL.md + 参考库），供 Claude Code 插件安装或 OpenAI Codex 直接加载。它把宏观经济学建模需求（如复制 Smets-Wouters 2007、含金融加速器的新凯恩斯模型）转化为可运行的 Dynare .mod 文件：先确认建模选择并生成推导文档，再分阶段增量写代码，优先写非线性方程系统。内置 149 个 MMB 复制模型与 89 个 Pfeifer 语法示例的双本地参考库，另含 161 个推导的模型档案与已知错误日志。连接 MATLAB MCP 后可自动运行 Dynare 并迭代修复错误；无 MATLAB 时仍可写模型但不运行。运行生成的文件需另装 Dynare 7.1 与 MATLAB/Octave。

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

- 内置 149 个 MMB 复制模型 + 89 个 Pfeifer 语法示例双参考库
- 先确认建模选择、分阶段增量构建、默认非线性方程系统的工作流
- 经 MATLAB MCP 自动运行 Dynare 读取错误、最小修复并重跑的调试循环
- 论文级 IRF 矢量图输出（plot_irfs_pub.m / plot_series_pub.m）

## 适用场景

- 把论文的最优化问题与 FOC 翻译成可运行的 Dynare .mod 文件
- 复制 Smets-Wouters 2007 等经典 DSGE 论文并出 IRF
- 排查 Blanchard-Kahn 条件不满足、稳态求解失败等错误
- 生成可直接放入论文的出版级 IRF 对比图

## 场景标签

`编码 Agent` `科研工具` · 领域:编码与开发

## 证据(README 行号)

> L9: > A Claude Code skill that takes your macroeconomic intuition — "I want a New Keynesian model with a financial accel
> L90: The skill is just a standard Agent Skill — a `SKILL.md` with `name` + `description` frontmatter plus a `references/

## 星数曲线

```mermaid
xychart-beta
    title "EconSolider/dynare-copilot 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-29 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `2511d28708fd` · [字段定义](../../DATASET.md)*
