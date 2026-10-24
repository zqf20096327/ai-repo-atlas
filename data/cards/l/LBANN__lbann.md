# LBANN/lbann

⭐ 231 · C++ · NOASSERTION · 推送 2026-08-06 · [GitHub](https://github.com/LBANN/lbann) · [官网](http://software.llnl.gov/lbann/) · 组织维护

**LLNL 的高性能分布式深度学习训练框架**

Livermore Big Artificial Neural Network (LBANN) 是 Lawrence Livermore 国家实验室开发的 C++ 深度学习框架，面向 HPC 集群上的大规模分布式模型训练，属于 RADIUSS 项目生态。当前 LBANNv2 采用 BYOT（bring your own Torch）模式，先 pip 安装 PyTorch 再 pip 安装本包。README 仅含构建与版权信息，详细功能与文档需查阅仓库其他文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 面向 HPC 集群的分布式神经网络训练
- C++ 实现，属 LLNL RADIUSS 软件生态
- v2 采用 BYOT 模式，依赖用户自装的 PyTorch

## 适用场景

- 在大型超算集群上做分布式深度学习训练
- 需要与 LLNL RADIUSS 软件栈配合的科研工作流

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L1: # Build
> L3: To save some pip-related heartburn, LBANNv2 is currently BYOT ("bring
> L4: your own Torch").

## 星数曲线

```mermaid
xychart-beta
    title "LBANN/lbann 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 230 --> 232
    line [231, 231]
```

2026-10-18 231 → 2026-10-24 231（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 low · 依据 README sha `b6b12e79bfbc` · [字段定义](../../DATASET.md)*
