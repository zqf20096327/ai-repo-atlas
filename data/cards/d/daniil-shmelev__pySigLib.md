# daniil-shmelev/pySigLib

⭐ 27 · C++ · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/daniil-shmelev/pySigLib) · [官网](https://pysiglib.readthedocs.io) · 个人维护

**路径签名/log签名/签名核计算库：PyTorch、JAX、CUDA 加速**

面向时间序列与粗路径计算的 Python 工具库：统一提供截断签名、log 签名（含 Lyndon 坐标）、分支签名与签名核的计算，覆盖 NumPy、PyTorch、JAX 三种接口，支持 PyTorch/JAX 自动微分及 JAX 的 jit/vmap/grad，执行层为多线程 C++ 或原生 CUDA。计算在输入所在设备上运行，跨 Windows/Linux/Mac；另有可通过 ccall 调用、无需 Python 与编译器的 Julia 原生库产物。以 pip 安装，CUDA 为可选扩展。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 签名、log 签名、分支签名、签名核统一工具集
- PyTorch/JAX 自动微分，JAX 支持 jit/vmap/grad
- 多线程 C++ 与原生 CUDA 实现
- 签名流支持在线更新与常数时间区间查询

## 适用场景

- 为时间序列模型提取签名特征
- 在 PyTorch/JAX 模型中嵌入可微分的签名层
- GPU 上进行大规模签名核计算

## 场景标签

 · 领域:机器学习库/时间序列

## 证据(README 行号)

> L17: pySigLib brings path signatures, log-signatures, branched signatures, and
> L19: PyTorch, and JAX support, with automatic differentiation for PyTorch and

## 星数曲线

```mermaid
xychart-beta
    title "daniil-shmelev/pySigLib 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-27 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `cdbdd0a6f937` · [字段定义](../../DATASET.md)*
