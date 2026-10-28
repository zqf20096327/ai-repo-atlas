# DragonflyRobotics/Neuroxide

⭐ 104 · Rust · GPL-3.0 · 推送 2026-03-18 · [GitHub](https://github.com/DragonflyRobotics/Neuroxide) · 个人维护

**用 Rust 从零重写 PyTorch 风格 API 的 AI 框架**

由个人发起的 Alpha 阶段项目，用 Rust 重新实现 PyTorch 风格的 API，提供张量（Tensor）、TensorDB、前向/反向自动求导、算子（Add/MatMul/Mul/Pow）等基础组件，支持 CPU 与 CUDA 设备，BLAS 依赖可选。已实现并基准测试矩阵乘法（含有限广播，官方建议手动广播常量项）。文档稀少，内置 nn.Linear 等层尚未完成，安装方式为 git clone 后 cargo run 或 cargo build 链接使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- Rust 实现的 PyTorch 风格张量与算子 API
- 前向/反向传播与选择性反向到部分叶子节点
- 支持 CPU 与 CUDA 设备的算子执行
- 张量支持 +、-、*、/ 运算符重载

## 适用场景

- 在 Rust 项目中链接使用 PyTorch 风格的自动求导张量库
- 参与早期框架开发的贡献者实验与验证
- 需要硬类型语言构建 AI 计算的场景原型验证

## 场景标签

 · 领域:AI 框架/机器学习基础设施

## 证据(README 行号)

> L4: Welcome! This project attempts to rewrite the PyTorch framework (maintaining a consistent API call) in Rust in hopes
> L74: Python has many benefits, mainly its flexibility, which makes it an avid language for AI/ML. The tradeoff is the cl

## 星数曲线

```mermaid
xychart-beta
    title "DragonflyRobotics/Neuroxide 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 103 --> 105
    line [104, 104]
```

2026-10-18 104 → 2026-10-28 104（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `b40c373273db` · [字段定义](../../DATASET.md)*
