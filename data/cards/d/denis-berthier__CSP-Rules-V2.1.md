# denis-berthier/CSP-Rules-V2.1

⭐ 21 · CLIPS · GPL-3.0 · 推送 2026-06-20 · [GitHub](https://github.com/denis-berthier/CSP-Rules-V2.1) · 个人维护

**基于模式规则的有限约束满足问题通用求解器**

CSP-Rules-V2.1 是求解有限二元约束满足问题（CSP）的通用模式/规则式求解器，基于 CLIPS 前向链推理引擎（RETE 算法）实现。它由通用部分与应用特定部分组成，内置拉丁方、数独、Futoshiki、Kakuro、地图着色、Hidato、Numbrix 和 Slitherlink 求解器。核心机制是以候选值与矛盾链接表示问题，通过 whips、chains、braids 等通用消解规则按“最简优先”策略推进求解，并给出基于规则族的难度评级；非二元约束可通过增加 CSP 变量转化为二元约束处理。定位为求解器与研究工具，可作为证明辅助，配套出版著作阐述理论，README 未给出安装命令细节。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 CLIPS 前向链推理引擎的模式式 CSP 求解
- 通用消解规则族（whips、chains、braids、ORk-whips 等）
- 内置 8 类逻辑谜题求解器（数独、Kakuro、Slitherlink 等）
- “最简优先”策略与基于规则族的谜题难度评级

## 适用场景

- 求解数独、Kakuro、Slitherlink 等逻辑谜题并获得逐步消解路径
- 按通用规则族对大量谜题实例做难度分类研究
- 将自定义有限二元 CSP 接入通用规则框架求解

## 场景标签

 · 领域:约束满足/逻辑推理工具

## 证据(README 行号)

> L11: **_CSP-Rules is a general pattern-based (or rule-based) solver of finite binary CSPs_**.
> L21: Considering this definition, an implementation in terms of rules of a forward-chaining inference engine seemed rele

## 星数曲线

```mermaid
xychart-beta
    title "denis-berthier/CSP-Rules-V2.1 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `457d98f752c7` · [字段定义](../../DATASET.md)*
