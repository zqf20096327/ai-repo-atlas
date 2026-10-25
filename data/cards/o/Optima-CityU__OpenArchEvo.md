# Optima-CityU/OpenArchEvo

⭐ 47 · Python · Apache-2.0 · 推送 2026-10-10 · [GitHub](https://github.com/Optima-CityU/OpenArchEvo) · [官网](https://optima-cityu.github.io/OpenArchEvo/) · 组织维护

**LLM 写架构程序、种群进化筛选的神经架构搜索框架**

面向科研人员的开源神经架构搜索参考代码：LLM 作为变异算子重写完整 PyTorch 架构程序，多岛屿种群、NSGA-II 选择与 TabPFN 代理模型筛选候选，每轮仅训练 ≤16 个程序。搜索流程问题无关，论文中用于发现原生脉冲序列模型，10 轮迭代训练 151 个新架构，约 132 V100 GPU-days。提供 CPU dry-run（用离线替代品，无需 GPU 或 LLM）、可接入任意 OpenAI 兼容端点，并附带 171 个已训练架构的代码库。

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

- LLM 重写完整架构程序，搜索空间为可执行代码而非固定算子组合
- 多岛屿种群 + NSGA-II + TabPFN 代理筛选，每轮仅训练 ≤16 个候选
- 代码/设计理由/行为指纹三视角表示驱动新颖性与去重
- 附 171 个已训练架构 zoo（含 NeuroGate 等 3 个精英架构）

## 适用场景

- 复现论文中的脉冲序列模型架构搜索
- 把架构搜索流程迁移到自己的任务与模型家族
- 浏览已发现架构的源码、设计理由与指标做参考

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L25: Most neural architecture search works inside a fixed space of cells and operators. **OpenArchEvo searches over code
> L30: - **Evolution, not a single agent.** Multi-island populations, NSGA-II selection over predicted fitness and novelty

## 星数曲线

```mermaid
xychart-beta
    title "Optima-CityU/OpenArchEvo 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 45 --> 48
    line [46, 47, 47]
```

2026-10-18 46 → 2026-10-25 47（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `184b9b6f2e1d` · [字段定义](../../DATASET.md)*
