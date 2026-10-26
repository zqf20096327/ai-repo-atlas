# yashbonde/rasp

⭐ 65 · Python · MIT · 推送 2025-11-01 · [GitHub](https://github.com/yashbonde/rasp) · 个人维护

**RASP 编程语言的 Python 实现，用于表达 Transformer 可学习的任务解法**

实现论文 Thinking like Transformers 提出的 Restricted Access Sequence Processing（RASP）语言，提供 select、aggregate、selector_width 等原语，用类注意力机制描述序列任务解法；可将 RASP 代码编译为 PyTorch 神经网络模块用于训练。面向 Transformer 机制研究者与编程语言实现感兴趣的开发者，含 Reverse（WIP）、直方图、排序、Dyck-i 等实验任务与 pytest 测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现 select/aggregate/selector_width 等 RASP 原语
- RASP 代码可生成 PyTorch nn.Module 结构
- 附 Reverse、直方图、排序、Dyck-i 等实验任务与测试

## 适用场景

- 用 RASP 语言编写并研究 Transformer 可表达的序列任务解法
- 将 RASP 程序转为神经网络结构进行训练实验
- 复现论文中的机制可解释性任务（直方图、排序等）

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L3: Implementing Restricted Access Sequence Processing (RASP) transformer language from "Thinking like Transformers" pap
> L21: - `primitives`: neural functions and primitives built using manual codes that can be used for training
> L35: This would create a neural network as follows:

## 星数曲线

```mermaid
xychart-beta
    title "yashbonde/rasp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26"]
    y-axis "stars" 63 --> 66
    line [64, 65, 65]
```

2026-10-18 64 → 2026-10-26 65（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `05d5547b3ed2` · [字段定义](../../DATASET.md)*
