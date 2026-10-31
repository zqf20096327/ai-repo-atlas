# SunDoge/dlpark

⭐ 66 · Rust · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/SunDoge/dlpark) · [官网](https://crates.io/crates/dlpark) · 个人维护

**纯 Rust 的 DLPack 实现，跨框架零拷贝交换张量**

面向 Rust 开发者的张量互操作库：实现 DLPack 的 legacy 与 versioned ABI、C Exchange 1.3 及 Python capsule 协议，使张量在 ndarray、candle、PyTorch/CuPy、MLX、CUDA CudaSlice、safetensors 等容器与框架间零拷贝传递。以 crate 形式发布于 Crates.io，默认不启用任何 feature，按需开启集成；所有权由 managed tensor 的 deleter 管理，导入描述符需 validate 校验。CUDA/Metal 运行时策略由应用自行处理，仓库提供 demos 示例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 legacy/versioned ABI、DLPack 1.3 C Exchange 与 Python Array API 协议
- ndarray/candle/pyo3/cudarc/safetensors/image 等按需启用的零拷贝适配
- demos 覆盖 CUDA、Metal、Torch、MLX 等交换场景

## 适用场景

- 在 Rust 与 PyTorch/CuPy 间零拷贝共享 CUDA 缓冲区
- Rust 张量与 MLX 通过共享 MTLBuffer 交换
- safetensors 文件的零拷贝导出与序列化视图

## 场景标签

 · 领域:深度学习/张量互操作

## 证据(README 行号)

> L9: A pure Rust implementation of DLPack for
> L43: |Feature|Integration|Data movement|

## 星数曲线

```mermaid
xychart-beta
    title "SunDoge/dlpark 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 64 --> 67
    line [65, 66, 66]
```

2026-10-18 65 → 2026-10-31 66（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `d130cb83fa8b` · [字段定义](../../DATASET.md)*
