# ahrefs/ocannl

⭐ 118 · OCaml · BSD-2-Clause · 推送 2026-10-26 · [GitHub](https://github.com/ahrefs/ocannl) · [官网](https://ahrefs.github.io/ocannl/docs/) · 组织维护

**从零实现的 OCaml 编译型深度学习框架**

OCANNL 是以 OCaml 编写、从零实现的编译型深度学习框架，实现反向传播（一阶反向模式自动微分）与形状推断，可将高层张量表示编译至 for 循环。用户通过 %op 与 %cd 语法扩展描述张量运算与赋值计算，自行划定编译单元范围（如整步训练或梯度更新）。支持扩展 einsum 记法、混合精度双向精度推断，后端覆盖 CUDA（≥12.8）、Metal（MSL ≥3.1）与 HIP（经 hipjit）。由 Ahrefs 赞助，提供配置档（reproducible/performance/approximate）与调度自动调优。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-2-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现一阶反向模式自动微分与形状推断，可编译至 for 循环
- %op/%cd 两层抽象，用户显式划定编译单元范围
- CUDA / Metal / HIP 三种 GPU 后端，CUDA 需 ≥12.8
- 扩展 einsum 记法与混合精度双向精度推断

## 适用场景

- 在 OCaml 生态中从零构建与训练神经网络
- 研究编译型张量程序的形状推断与调度优化
- 在 CUDA/Metal/HIP 设备上运行训练与推理例程

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L7: * A from-scratch, compiled Deep Learning framework.
> L9: * The long-term goal is to provide several "low-level" backends, aiming to seek inspiration from projects such as ti

## 星数曲线

```mermaid
xychart-beta
    title "ahrefs/ocannl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 117 --> 119
    line [118, 118]
```

2026-10-18 118 → 2026-10-27 118（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `b17fdc9d1c3f` · [字段定义](../../DATASET.md)*
