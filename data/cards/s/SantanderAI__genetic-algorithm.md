# SantanderAI/genetic-algorithm

⭐ 39 · Python · Apache-2.0 · 推送 2026-10-01 · [GitHub](https://github.com/SantanderAI/genetic-algorithm) · [官网](https://github.com/SantanderAI) · 组织维护

**无依赖 Python 遗传算法引擎，适应度准则可插拔，服务 LLM 自动研究**

Santander AI Lab 开源的纯标准库遗传算法引擎，提供种群、选择（轮盘/精英）、交叉、变异与可复现种子等进化搜索机制；核心设计是适应度准则作为可替换插件，引擎只要求插件返回一个数值。README 将其定位为构建 LLM/AI autoresearcher（生成→评估→选择→循环）的可复用搜索核心，支持将 LLM-as-judge 嵌入评估准则，并提供多线程适应度评估以适配 I/O 密集的 LLM 评估。同时明示局限：评估调用开销大、适应度插件设计不当会诱发 reward hacking、小型或凸搜索空间不宜使用。Python 3.10+，无第三方运行时依赖。

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

- 适应度准则以插件形式可插拔，可组合多目标（如质量与 token 成本）
- 仅依赖 Python 标准库，无第三方运行时依赖
- 多线程适应度评估，适配 LLM judge 等 I/O 密集评估
- 每代进化产出可审计记录，支持 seed 复现

## 适用场景

- 以进化循环实现 Karpathy 式 autoresearcher，用 LLM-as-judge 评估候选
- 优化 prompt、pipeline 配置等无明确数值指标的候选方案
- 数值优化与目标向量搜索（附示例 optimize_sphere、autoresearcher）

## 场景标签

`科研工具` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: > **Open source by Santander AI Lab.** A dependency-free Python **genetic-algorithm library / engine** with **plugga
> L55: - **Put an LLM *inside* the criterion.** A plugin can be an *LLM-as-a-judge* that
> L114: # The GA framed as a Karpathy-style autoresearcher (offline LLM-as-judge stub)

## 星数曲线

```mermaid
xychart-beta
    title "SantanderAI/genetic-algorithm 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-28 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2709daa8cb57` · [字段定义](../../DATASET.md)*
