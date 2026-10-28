# danyvarghese/PyGol

⭐ 21 · C · NOASSERTION · 推送 2026-07-09 · [GitHub](https://github.com/danyvarghese/PyGol) · 个人维护

**基于 Meta Inverse Entailment 的归纳逻辑编程（ILP）Python 库**

Python 实现的归纳逻辑编程系统：基于 Meta Inverse Entailment（MIE）从背景知识、正/负例与常量中学习一阶逻辑规则，无需模式声明，可处理表格与关系型数据。支持递归规则学习、自动谓词发明、交叉验证及溯因推理（pygol_abduction）。通过 Janus 连接 SWI-Prolog。面向科研与教育用户，非商业用途免费，商用需联系作者，安装要求 SWI-Prolog 9.2.0+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MIE 从背景知识自动生成 meta theory，无需模式声明
- 支持递归规则学习与自动谓词发明
- 提供学习、交叉验证与溯因推理三种接口
- 可学习可解释的一阶逻辑规则（Michalski train 等示例）

## 适用场景

- 从关系型/表格数据中学习可解释的逻辑规则
- 生物与生态交互的溯因推断（配套 InfIntE 包）
- 少样本场景下学习诊断规则（神经退行性疾病、植物病害）

## 场景标签

 · 领域:机器学习/符号推理

## 证据(README 行号)

> L2: **PyGol** is a novel Inductive Logic Programming(ILP) system based on **Meta Inverse Entailment(MIE)** using Python.
> L108: - ILP Learning Approach :- **pygol_learn()**

## 星数曲线

```mermaid
xychart-beta
    title "danyvarghese/PyGol 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `05efc268c191` · [字段定义](../../DATASET.md)*
