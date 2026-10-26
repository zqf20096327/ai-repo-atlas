# kYangLi/DeepH-dock

⭐ 42 · Python · GPL-3.0 · 推送 2026-10-17 · [GitHub](https://github.com/kYangLi/DeepH-dock) · [官网](https://docs.deeph-pack.com/deeph-dock) · 个人维护

**连接第一性原理计算与 DeepH 深度学习方法的接口平台**

面向计算材料学科研用户的模块化接口平台：桥接主流 DFT 软件（SIESTA、QE、OpenMX、FHI-aims、ABACUS）与 DeepH 深度学习哈密顿量方法及紧束缚工具链，提供结构生成、重叠矩阵计算、哈密顿对称化、KPM/Lanczos 快速对角化等算法，以及 DFT 数据生成、预处理、后分析的自动化流水线。可作为 DeepH-pack 套件的专用接口，也可独立用作 DFT 后处理工具；提供统一 Python API 与 dock 命令行，支持 MPI/多线程多级并行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 桥接 5 个主流 DFT 软件包与 DeepH 工作流
- 自动化结构生成、对称化与 KPM/Lanczos 对角化算法
- DFT 训练数据生成、预处理与后分析标准化流水线
- dock CLI 支持注册自定义子命令与 Shell 补全

## 适用场景

- 高通量材料电子结构计算与数据生成
- 为 DeepH 神经网络模型准备标准化训练数据
- 连接 DFT 计算与紧束缚模型参数化

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L16: *DeepH-dock* is a modular, extensible interface platform for quantum materials calculations, dedicated to building 
> L18: At the core of *DeepH-dock* is **a unified and flexible interface layer that seamlessly connects mainstream DFT pac
> L30: - **Multi-Software Compatibility:** Seamlessly bridges major DFT packages (e.g., SIESTA, QE, OpenMX, FHI-aims, ABAC

## 星数曲线

```mermaid
xychart-beta
    title "kYangLi/DeepH-dock 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-26 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ae4bdfe7d9d7` · [字段定义](../../DATASET.md)*
