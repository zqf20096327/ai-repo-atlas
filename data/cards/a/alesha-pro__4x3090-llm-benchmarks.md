# alesha-pro/4x3090-llm-benchmarks

⭐ 18 · Python · 推送 2026-08-15 · [GitHub](https://github.com/alesha-pro/4x3090-llm-benchmarks) · 个人维护

**4x3090 家庭主机上的本地 LLM 推理基准数据集（1064 条测量）**

个人维护的本地 LLM 推理基准存档：在一台 4x RTX 3090（96 GB 显存）主机上记录 1064 条测量，覆盖 28 个基准活动、18 个模型家族、26 种量化类别，引擎以 vLLM 为主（671 行），另有 llama.cpp（212 行）与实验性 exllamav3（38 行）。1063 条测量附带完整启动命令，每行保留引擎版本、TP/PP 布局、功耗限制、工作负载等上下文。数据以 JSONL 为源、SQLite 可查询，另提供无依赖的 Python 查询脚本。作者声明这是存档而非排行榜，不同活动间行不可直接比较。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 1064 条测量覆盖 28 个基准活动与 18 个模型家族
- 1063 条附带精确启动命令（argv/shell）
- 26 种量化分类不合并为泛化 INT4 桶
- 提供 JSONL、SQLite 与无依赖 Python 查询脚本

## 适用场景

- 查询特定模型/引擎/量化组合的实测推理速度
- 对比 TP/P2P 布局、KV cache 格式等变量对性能的影响
- 取同活动内数据复现或分析本地推理基准

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: **638 local inference measurements from one 96 GB home rig. The exact launch
> L11: This repository is the database I wanted. You can inspect one result in the
> L27: The archive currently has 1064 measurements from 28 benchmark campaigns across

## 星数曲线

```mermaid
xychart-beta
    title "alesha-pro/4x3090-llm-benchmarks 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `e3a319f34020` · [字段定义](../../DATASET.md)*
