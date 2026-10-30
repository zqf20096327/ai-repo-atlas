# dadukhankevin/Finch

⭐ 42 · Python · MIT · 推送 2026-08-19 · [GitHub](https://github.com/dadukhankevin/Finch) · 个人维护

**通用进化计算库：用可组合层与共享解码器搜索任意可优化问题**

Python 遗传算法库，提供可组合层堆叠的传统 GA 与基于共享解码器的进化引擎，只需给定适应度函数与输出形状即可搜索多种问题（图像进化、曲线拟合、TSP、装箱）。附带实时仪表盘（finch4.hub，端口 8800）展示运行与媒体产物。另含 genetic auto-research（GAR）方法：维护多条研究谱系，以 LLM+Decoder.md 为解码器，配合 evolver/evaluator/judge worker 与版本化研究记录做迭代式自动研究。安装方式为 pip install -e .（源码安装）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 可组合层式传统 GA 与共享解码器进化两种引擎
- GAR：多谱系自动研究，评分发现原子写入共享 Decoder.md
- finch4.hub 实时仪表盘展示运行与演化媒体
- 内置 TSP、背包、图像进化、装箱等示例

## 适用场景

- 用统一接口对不同类型优化问题做进化搜索
- 观察与调试进化过程（实时仪表盘与 Tree of Life）
- 在 LLM 辅助的自动研究流程中运行 GAR 实验

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: Finch 4 is the latest iteration of Finch, combining Finch's modularity with concepts from genespace, latentspace, an
> L34: A new method called genetic auto-research (GAR) is also available within Finch 4. GAR keeps an evolving population 
> L71: Finch 4 ranges from traditional GAs over problem-specific genomes to algorithms that separate genotype from phenoty

## 星数曲线

```mermaid
xychart-beta
    title "dadukhankevin/Finch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-30 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `95a7d7359321` · [字段定义](../../DATASET.md)*
