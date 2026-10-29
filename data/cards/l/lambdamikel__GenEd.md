# lambdamikel/GenEd

⭐ 22 · Common Lisp · GPL-3.0 · 推送 2026-10-17 · [GitHub](https://github.com/lambdamikel/GenEd) · [官网](https://www.michael-wessel.info/thesis.html#gened) · 个人维护

**用描述逻辑对图形记法做形式推理的可视化图形编辑器**

1996 年汉堡大学学士论文产出的 Common Lisp & CLIM 图形编辑器：通过加载 CLASSIC 描述逻辑知识基定义 Petri 网、状态机、ER 图等可视形式语言的语法，利用 ABox 实例分类服务识别图形对象组合的语义类别，其中几何与拓扑空间关系起关键作用。本发布版本中 CLASSIC 接入已禁用（作者无 CLASSIC 源码），分类能力不可用；可用 LispWorks 6.1 + Motif32 CLIM 在 Ubuntu 上加载运行。作者自述代码质量不高，属遗留软件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 通过 CLASSIC 知识基定义可视形式语言（Petri 网/状态机/ER 图）的语法与语义
- 利用 CLASSIC 的 ABox realization 实例分类服务识别图形组合
- 基于几何与拓扑空间关系（如 RCC）的定义机制
- 本发布版本已禁用 CLASSIC 接入，分类能力不可用

## 适用场景

- 研究用描述逻辑定义可视形式语言的语法与语义
- 了解 1990 年代符号 AI 与 CLIM 图形界面的历史实现
- 尝试自行恢复 CLASSIC 接入或改接 Racer 推理机

## 场景标签

 · 领域:知识表示/图形编辑器

## 证据(README 行号)

> L20: A key innovative feature was its capability to classify constellations
> L32: Originally, Gened was hooked up to the CLASSIC Description Logic

## 星数曲线

```mermaid
xychart-beta
    title "lambdamikel/GenEd 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `9584f8e58412` · [字段定义](../../DATASET.md)*
