# flodl-labs/flodl

⭐ 63 · Rust · MIT · 推送 2026-10-20 · [GitHub](https://github.com/flodl-labs/flodl) · [官网](https://flodl.dev) · 组织维护

**基于 libtorch 的 Rust 原生深度学习框架**

用 Rust 重写 PyTorch 层的深度学习框架：复用 libtorch 的 GPU 内核，API 概念与命名对齐 PyTorch，提供 FlowBuilder 流式图构建器、可嵌套与点路径寻址的 Graph Tree、声明式训练阶段（freeze/thaw 子树）、子图检查点与三级训练控制（bypass/cooperative/managed），以及带 Web 仪表盘的训练监控。支持 CUDA 与 ROCm（AMD 训练尚未在硬件上验证），通过 fdl CLI 或 Docker 脚手架安装，需编译（cargo build）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- FlowBuilder 流式图构建器（split/merge、loop、gate/switch 路由等组合原语）
- Graph Tree 层级组合：点路径寻址、子图冻结与检查点、跨层级指标
- 三级训练控制与分布式多 GPU/多主机支持
- 内置训练监控与 SSE 实时 Web 仪表盘，可导出 HTML/CSV

## 适用场景

- 在 Rust 项目中训练深度学习模型而不引入 Python 运行时
- 把独立训练的子模型组合成更大的架构并分阶段训练
- 多 GPU/多主机分布式训练并实时监控各 rank 指标

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L5: A Rust-native deep learning framework built on libtorch.
> L128: For framework-managed training (same code on CPU, single GPU, multi-GPU),

## 星数曲线

```mermaid
xychart-beta
    title "flodl-labs/flodl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-26 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `97fb2962b923` · [字段定义](../../DATASET.md)*
