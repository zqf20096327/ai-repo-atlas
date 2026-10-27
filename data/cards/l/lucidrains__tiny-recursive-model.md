# lucidrains/tiny-recursive-model

⭐ 192 · Python · MIT · 推送 2025-12-23 · [GitHub](https://github.com/lucidrains/tiny-recursive-model) · 个人维护

**面向研究者的 Tiny Recursive Model (TRM) PyTorch 非官方实现**

lucidrains 对 Tiny Recursive Model (TRM) 的非官方 PyTorch 实现。TRM 是 Sapient AI 的 Alexia Jolicoeur-Martineau 提出的 HRM 改进模型，用于递归推理任务。本仓库以 Python 库形式提供模型类（TinyRecursiveModel）、MLPMixer1D 等组件与 Trainer 训练接口，通过 pip 安装即可导入使用；README 附官方仓库、访谈与论文评述链接及 BibTeX 引用。作为论文的非官方复现，模型细节以官方仓库与论文为准。

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

- Tiny Recursive Model (TRM) 的 PyTorch 非官方实现
- 提供 TinyRecursiveModel、MLPMixer1D 组件与 Trainer 训练接口
- 附论文引用条目（Less is More: Recursive Reasoning with Tiny Networks）

## 适用场景

- 复现或实验 TRM 递归推理架构
- 在自定义数据上训练/微调 TRM 模型
- 对比 HRM 及其改进变体的推理表现

## 场景标签

 · 领域:深度学习/模型实现

## 证据(README 行号)

> L5: Implementation of Tiny Recursive Model (TRM), improvement to HRM from Sapient AI, by Alexia Jolicoeur-Martineau
> L27: from tiny_recursive_model import TinyRecursiveModel, MLPMixer1D, Trainer

## 星数曲线

```mermaid
xychart-beta
    title "lucidrains/tiny-recursive-model 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 191 --> 193
    line [192, 192]
```

2026-10-18 192 → 2026-10-27 192（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `628a86472ad7` · [字段定义](../../DATASET.md)*
