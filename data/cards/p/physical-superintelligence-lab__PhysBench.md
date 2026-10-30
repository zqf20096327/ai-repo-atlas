# physical-superintelligence-lab/PhysBench

⭐ 93 · Python · Apache-2.0 · 推送 2026-01-21 · [GitHub](https://github.com/physical-superintelligence-lab/PhysBench) · [官网](https://physbench.github.io/) · 组织维护

**评测视觉语言模型物理世界理解能力的基准数据集与评测代码**

ICLR 2025 论文 PhysBench 的官方仓库：提供 10,002 条测试条目与 200 条验证条目的基准数据集（发布于 Hugging Face），覆盖物理对象属性、对象关系、场景理解与物理动力学四大类、19 个子类、10 个能力维度；eval 目录内含评测工具，可复现论文结果或评测自有模型。已对 75 个 VLM 进行实验，并提出利用先验物理知识与专家模型的 PhysAgent 增强方法。训练集划分、3D 资产与剩余代码尚未发布，测试集可通过 EvalAI 提交。README 可见范围内未给出安装命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 10,002 条测试条目 + 200 条验证条目，四大物理理解类别、19 个子类
- 已评测 75 个 VLM，附测试集排行榜
- 提出 PhysAgent：借助物理先验知识与专家模型增强 VLM
- eval 目录提供评测工具，支持复现论文结果或评测自有模型

## 适用场景

- 评测自己模型的物理世界理解能力
- 在 EvalAI 上提交预测并登上测试集排行榜
- 研究 VLM 在物理属性、关系、场景与动力学上的能力差距

## 场景标签

`模型评测` `多模态` · 领域:评测与运维

## 证据(README 行号)

> L21: **Vision-Language Models (VLMs)** have emerged as promising tools for building **embodied agents**, whereas their l
> L36: We have released the **dataset** on Hugging Face **🤗 Dataset**, and you can use the **evaluation tool** in the eval

## 星数曲线

```mermaid
xychart-beta
    title "physical-superintelligence-lab/PhysBench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 92 --> 94
    line [93, 93]
```

2026-10-18 93 → 2026-10-30 93（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `f009d5485e4e` · [字段定义](../../DATASET.md)*
