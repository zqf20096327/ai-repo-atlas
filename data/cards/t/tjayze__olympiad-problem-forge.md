# tjayze/olympiad-problem-forge

⭐ 56 · HTML · 推送 2026-10-26 · [GitHub](https://github.com/tjayze/olympiad-problem-forge) · 个人维护

**跨平台桌面应用：按模板生成奥赛级数学题并管理题库**

基于 PyQt5 的离线优先桌面应用，面向学生、教练与自学者，用于生成、预览、筛选与归档竞赛风格数学题。机制上分为三层：模板定义（参数化数学对象）、受引导随机实例化（生成具体数值/几何配置）、用户策展（标签、保存到本地题库）。覆盖代数、几何、组合、数论等域，每个条目带符号化可解性校验、二维难度调节、自动解答思路与确定性种子；支持西/英/加泰罗尼亚/葡语叙述及 LaTeX/PDF/Markdown/JSON 导出。声明与数学奥赛组织无关联，生成题为原创合成而非真题复制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 百余个模板族覆盖代数/几何/组合/数论，同一模板可产出数千道可解题
- 符号化可解性校验层在题目呈现前检查每个生成项
- 二维难度引擎（结构深度+参数张力）与确定性生成种子
- 多语言题面（西/英/加泰罗尼亚/葡语）及 LaTeX/PDF/Markdown/JSON 导出

## 适用场景

- 为奥赛训练按难度梯度批量生成原创练习题
- 教练为单一题型快速生成变式题
- 离线环境下维护带标签的个人题库并导出打印

## 场景标签

 · 领域:教育/数学

## 证据(README 行号)

> L7: **Epsilon Olympiad Forge** is a cross-platform desktop workshop for generating, curating, and archiving competition-
> L33: This separation means the same template can yield thousands of distinct problems, each provably solvable, each with

## 星数曲线

```mermaid
xychart-beta
    title "tjayze/olympiad-problem-forge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-27 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `0694bfb6b08e` · [字段定义](../../DATASET.md)*
