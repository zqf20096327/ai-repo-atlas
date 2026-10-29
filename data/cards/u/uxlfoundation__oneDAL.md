# uxlfoundation/oneDAL

⭐ 653 · C++ · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/uxlfoundation/oneDAL) · [官网](http://uxlfoundation.github.io/oneDAL/) · 组织维护

**C++/DPC++ 机器学习库：为表格数据提供 CPU/GPU 加速算法**

UXL Foundation 治理的 oneAPI 规范实现，提供面向表格数据的机器学习例程（线性回归、K-Means、随机森林等），支持 CPU、GPU 与多节点分布式。CPU 加速基于 SIMD 指令与缓存利用，GPU 加速基于 SYCL 框架与 oneMKL。可通过 C++/DPC++ 接口直接使用，或经 Extension for Scikit-learn 让现有 scikit-learn 代码调用其作为后端；也被 OAP MLlib 项目用于加速 Spark MLlib。安装支持二进制分发（Intel oneAPI、Conda、NuGet）与源码编译。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- C++ 与 DPC++ 接口的表格数据机器学习例程
- CPU（SIMD）与 GPU（SYCL/oneMKL）加速
- 分布式计算模式，附 MPI 示例
- 经 Extension for Scikit-learn 加速现有 scikit-learn 代码

## 适用场景

- 加速现有 scikit-learn 流水线而少改代码
- 在 C++ 项目中使用线性回归、K-Means、随机森林等算法
- 多节点分布式场景下运行 K-Means 等计算

## 场景标签

 · 领域:机器学习/数据分析

## 证据(README 行号)

> L13: oneAPI Data Analytics Library (oneDAL) is a C++ and DPC++ library (powering the Extension for Scikit-learn in Pytho
> L14: which implements accelerated machine learning routines for tabular data (e.g. linear regression, K-means clustering
> L17: Acceleration on CPUs is achieved by leveraging SIMD instructions and exploiting cache structures of modern hardware

## 星数曲线

```mermaid
xychart-beta
    title "uxlfoundation/oneDAL 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 652 --> 654
    line [653, 653]
```

2026-10-18 653 → 2026-10-29 653（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `3eceae208b30` · [字段定义](../../DATASET.md)*
