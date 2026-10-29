# ryannduma/CrystaLyse.AI

⭐ 24 · Python · MIT · 推送 2026-09-01 · [GitHub](https://github.com/ryannduma/CrystaLyse.AI) · [官网](https://crystalyseai.readthedocs.io/en/latest/) · 个人维护

**材料设计的科学 agent：编排工具发现与验证无机晶体**

面向计算材料设计的开源科学 agent，通过 MCP 端点编排 SMACT 组分筛选、Chemeleon 晶体结构生成、MACE-MP0 机器学习力场计算与 PyMatGen 相图分析四个计算后端，由 OpenAI Agents SDK 驱动的推理 LLM（o3/o4-mini）协调。提供 Creative/Rigorous/Adaptive 三种模式，并实现溯源强制机制：数值性质须来自工具调用而非模型估计，含渲染门控与 JSONL 审计。含三级安全过滤与可持续性元素标记，首次运行需下载约 770MB 数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四个计算后端经 MCP 端点编排（SMACT/Chemeleon/MACE-MP0/PyMatGen）
- 溯源强制：数值声明须追踪到工具调用，渲染门控拦截无来源数值
- 三种模式（Creative ~50s / Rigorous 2-5min / Adaptive 动态路由）
- 三级安全过滤与关键元素标记

## 适用场景

- 发现稳定或亚稳的新型无机晶体组合（如无铅光伏材料）
- 钠离子电池正极等储能材料候选的生成与验证
- 按发表级严格度做多晶型采样与稳定性验证

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L15: Crystalyse is an open, provenance-enforced scientific agent for computational materials design of inorganic crystal
> L22: Crystalyse integrates four computational backends through Model Context Protocol (MCP) endpoints:

## 星数曲线

```mermaid
xychart-beta
    title "ryannduma/CrystaLyse.AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `d3f3dbfa22c8` · [字段定义](../../DATASET.md)*
