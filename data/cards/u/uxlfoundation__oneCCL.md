# uxlfoundation/oneCCL

⭐ 272 · C++ · NOASSERTION · 推送 2026-10-06 · [GitHub](https://github.com/uxlfoundation/oneCCL) · [官网](https://oneapi-src.github.io/oneCCL) · 组织维护

**面向深度学习的集合通信库，实现高效通信模式**

oneAPI Collective Communications Library (oneCCL) 提供深度学习中常用通信模式的高效实现，是 oneAPI 规范的实现，由 UXL Foundation 治理。支持 SYCL（需 icpx/icx-cl 或支持 find_package(IntelSYCL) 的编译器），C API 采用基于插件的架构，可通过 CCL_PLUGIN 环境变量选择插件。以源码编译方式在 Linux 上构建，针对 Intel ARC 与 BMG GPU 提供专门构建选项，分发采用 Apache License 2.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供深度学习通信模式的高效实现
- oneAPI 规范实现，由 UXL Foundation 治理
- 支持 SYCL 与基于插件的 C API 架构
- 针对 ARC 与 BMG GPU 提供专门构建选项

## 适用场景

- 分布式深度学习训练中的跨设备集合通信
- 基于 oneAPI/SYCL 的异构计算程序集成通信原语
- 在 Intel GPU 集群上构建训练或推理工作流

## 场景标签

 · 领域:深度学习基础设施/高性能计算

## 证据(README 行号)

> L5: oneAPI Collective Communications Library (oneCCL) provides an efficient implementation of communication patterns use
> L7: oneCCL is governed by the UXL Foundation and is an implementation of the oneAPI specification.

## 星数曲线

```mermaid
xychart-beta
    title "uxlfoundation/oneCCL 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 270 --> 272
    line [271, 271]
```

2026-10-18 271 → 2026-10-25 271（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `09635a105f9d` · [字段定义](../../DATASET.md)*
