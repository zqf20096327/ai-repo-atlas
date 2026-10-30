# roitberg-group/torchani-amber

⭐ 18 · Fortran · MIT · 推送 2026-10-27 · [GitHub](https://github.com/roitberg-group/torchani-amber) · 组织维护

**在 Amber 分子动力学软件中接入 ANI 等神经网势的接口**

连接 TorchANI 类神经网原子间势（NN-IP）与 Amber 分子动力学引擎（sander 与 pmemd）的接口：每步模拟中由深度网络计算能量与力，交由 MD 引擎传播，支持纯 ML 模拟、力场处理非键相互作用的混合模式以及 ML/MM 模拟（后者需 sander）。内置 ANI-1x/2x/1ccx 与改进版 ANI-2xr/2dr，另支持 AimNet 2、Nutmeg 及自定义 TorchANI 2.0 API 模型。安装需从源码经 cmake 编译并自行编译 Amber，即使 CPU-only 运行也依赖 CUDA Toolkit、cuDNN 与 LibTorch。面向熟悉 Amber 的计算化学与分子模拟研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在 Amber 的 sander/pmemd 中以深度网络势计算能量与力
- 支持纯 ML、力场混合与 ML/MM 三种模拟模式
- 内置 ANI 系列模型，另支持 AimNet 2、Nutmeg 与自定义 jit 模型
- 支持 float64 双精度与 CUDA GPU 加速（cuAEV 扩展）

## 适用场景

- 用神经网势在 Amber 中跑全 ML 分子动力学
- QM 区域用 NN-IP、其余用力场的 ML/MM 模拟
- 加载自定义 TorchANI 2.0 API 模型做能量与力预测

## 场景标签

 · 领域:计算化学/分子模拟

## 证据(README 行号)

> L6: Interface enabling molecular dynamics or minimizations with ANI-style NN-IPs (neural
> L8: Energies and forces are calculated with the deep NNs at each step of the simulation,

## 星数曲线

```mermaid
xychart-beta
    title "roitberg-group/torchani-amber 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `f0e52a18190a` · [字段定义](../../DATASET.md)*
