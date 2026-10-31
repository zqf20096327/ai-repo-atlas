# 2389-research/simmer

⭐ 16 · MIT · 推送 2026-07-06 · [GitHub](https://github.com/2389-research/simmer) · [官网](https://2389.ai/research/products/simmer/) · 组织维护

**Claude Code 插件：用多评委迭代循环精炼任意工件或工作区**

以 Claude Code 插件形式提供的技能，包含 Setup/Generator/Judge/Reflect 四个子技能：识别工件、引出 2-3 条质量标准，每轮由评委会按标准打分（1-10）并给出单点最高杠杆改进（ASI），生成器据此产出改进版本，反思环节追踪最佳候选防止回归。按复杂度自动选择单评委或三评委评审团，评委评分前会阅读评估脚本与配置。支持文档、代码、流水线等多种工件类型，工作区模式以 git 提交跟踪迭代。默认 3 轮一批，每批后询问是否继续。

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

- 四子技能循环：设置/生成/评分/反思，ASI 单点改进策略
- 按复杂度自动选择单评委或定制三评委评审团，评委先阅读评估脚本再打分
- 回归安全：追踪最佳候选，result.md 始终输出最高分版本
- 支持可运行评估脚本（judge-only/runnable/hybrid 三种模式）与 git 提交级工作区迭代

## 适用场景

- 让 AI 按我给出的质量标准多轮打磨一份文案或提示词
- 对代码流水线工作区做迭代调优并对比每轮 git 差异
- 让评委会阅读我的评估脚本，自动寻找更优的配置方案

## 场景标签

 · 领域:开发工具/AI 编码

## 证据(README 行号)

> L12: /plugin marketplace add 2389-research/claude-plugins
> L18: One skill (`simmer`) with four subskills that run the refinement loop:
> L20: - **Setup** — identify the artifact (file or workspace), elicit 2-3 quality criteria, determine evaluation method

## 星数曲线

```mermaid
xychart-beta
    title "2389-research/simmer 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-31 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `a81e09b0b55c` · [字段定义](../../DATASET.md)*
