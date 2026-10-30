# KULeuven-MICAS/zigzag

⭐ 205 · C++ · MIT · 推送 2026-10-11 · [GitHub](https://github.com/KULeuven-MICAS/zigzag) · [官网](https://kuleuven-micas.github.io/zigzag/) · 组织维护

**面向 DL 加速器的架构-映射设计空间探索框架**

ZigZag 是一个用于深度学习加速器的硬件架构与映射设计空间探索（DSE）框架：解析 ONNX 模型，在自定义硬件架构（多维 MAC 阵列、多级存储、内存内计算核心）上自动搜索最优映射，输出能耗与延迟估算，结果以 YAML 格式给出。面向加速器架构研究者与硬件设计人员，由 KU Leuven MICAS 团队维护，有多篇配套论文（IEEE TC 2021 等）。安装与入门通过外部文档链接给出，README 未内嵌安装命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 直接解析 ONNX 模型进行代价评估
- 支持多维 MAC 阵列与数字/模拟内存内计算（IMC）核心定义
- 推断时空数据共享/复用模式，输出能耗与延迟分析
- 结果以 YAML 输出，结构面向扩展

## 适用场景

- 估算 DL 模型在自定义加速器上的能耗与延迟
- 自动搜索 DNN 计算在特定架构上的最优映射
- 探索不同硬件架构配置的设计空间

## 场景标签

 · 领域:AI 硬件/加速器设计工具

## 证据(README 行号)

> L4: **ZigZag** is a novel HW Architecture-Mapping Design Space Exploration (DSE) framework for Deep Learning (DL) accele
> L11: ✔ **ONNX Integration**: Directly parse ONNX models for seamless compatibility with modern deep learning workflows.

## 星数曲线

```mermaid
xychart-beta
    title "KULeuven-MICAS/zigzag 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 204 --> 207
    line [206, 205, 205]
```

2026-10-18 206 → 2026-10-30 205（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `3e623d91f309` · [字段定义](../../DATASET.md)*
