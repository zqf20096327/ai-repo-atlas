# LUMIA-Group/habit-bench

⭐ 5 · Python · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/LUMIA-Group/habit-bench) · 组织维护

**评测记忆型 agent 从弱证据中归纳用户习惯的基准**

HABIT-Bench 通过 4 个领域（Food/Finance/Software/Travel）、114 个合成用户、37,152 条会话与 3,328 个探针，考察 agent 能否从纵向弱证据中归纳潜在习惯并判断其适用边界。仓库提供共享评测器、9 种记忆方法实现与适配器及实验配置；数据集单独发布于 Hugging Face。每个探针有确定 gold 答案，评测支持证据标注打分、断点续跑与自定义记忆方法适配器接入，默认搭配 OpenAI 兼容推理服务使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4 领域 3,328 个探针，覆盖习惯归纳、适用边界、异常保留与漂移等维度
- 内置 Mem0、A-MEM、MemOS、Letta 等 9 种记忆方法集成
- 自定义记忆方法可通过适配器命令接入评测
- 支持断点续跑与逐域证据打分

## 适用场景

- 对比不同记忆方法在个性化习惯推断上的表现
- 为自定义记忆方法跑统一基准评测
- 研究 agent 在弱证据下做出不当个性化行为的情形

## 场景标签

`Agent 记忆` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L23: **Can a memory agent infer a user's latent habits from repeated weak evidence—and recognize when those habits apply
> L25: HABIT-Bench studies this question through longitudinal synthetic user histories in Food, Finance, Software, and Tra
> L33: This repository provides the shared evaluator, memory-method implementations and adapters, and main experiment conf

## 星数曲线

```mermaid
xychart-beta
    title "LUMIA-Group/habit-bench 星数(近 3 点)"
    x-axis ["2026-10-29", "2026-11-08", "2026-11-28"]
    y-axis "stars" 3 --> 6
    line [4, 5, 5]
```

2026-10-29 4 → 2026-11-28 5（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `a40b05726a3a` · [字段定义](../../DATASET.md)*
