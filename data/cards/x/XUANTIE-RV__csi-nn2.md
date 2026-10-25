# XUANTIE-RV/csi-nn2

⭐ 105 · C · Apache-2.0 · 推送 2026-02-10 · [GitHub](https://github.com/XUANTIE-RV/csi-nn2) · 组织维护 · 中文 README

**面向玄铁 RISC-V CPU 的神经网络算子库，供端侧推理部署**

SHL（csi-nn2）是玄铁提供的异构计算库，为玄铁 CPU 平台实现 CSI-NN2 神经网络算子 API：提供 C 参考实现与针对玄铁 CPU 的汇编优化，支持对称/非对称量化、8bit/16bit/f16 数据类型、NCHW/NHWC 布局，覆盖 CPU 架构并含异构调度参考实现；各 NPU 平台优化由对应厂商完成。可通过 pip 安装 hhb 包获取二进制，或用玄铁 RISC-V GCC 交叉编译（如 C906）部署到开发板运行 mobilenetv1 示例。面向嵌入式端侧模型部署开发者。

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

- 面向玄铁 CPU 的神经网络算子 C 参考实现与汇编优化
- 支持对称/非对称量化与 8bit/16bit/f16 数据类型
- 兼容 NCHW 与 NHWC 布局，含异构调度参考实现
- 提供 PyPI 包（hhb）与源码交叉编译两种安装方式

## 适用场景

- 在玄铁 C906 等 RISC-V 开发板上部署量化神经网络模型
- 为端侧推理应用调用 CSI-NN2 API 执行算子计算
- 配合 HHB 部署工具链完成模型量化与 BN 融合后部署

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: SHL(Structure of Heterogeneous Library, Chinese name: ShiHulan) is a high-performance Heterogeneous computing librar
> L4: The interface of SHL uses XuanTie neural network library API for XuanTie CPU platform: CSI-NN2, and provides a serie
> L17: In principle, SHL only provides the reference implementation of XuanTie CPU platform, and the optimization of each 

## 星数曲线

```mermaid
xychart-beta
    title "XUANTIE-RV/csi-nn2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 104 --> 106
    line [105, 105]
```

2026-10-18 105 → 2026-10-25 105（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `eaf799d06f2c` · [字段定义](../../DATASET.md)*
