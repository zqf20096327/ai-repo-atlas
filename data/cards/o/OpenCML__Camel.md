# OpenCML/Camel

⭐ 21 · C++ · MIT · 推送 2026-10-28 · [GitHub](https://github.com/OpenCML/Camel) · 组织维护 · 中文 README

**面向 AI 的图原生编程语言，程序即计算图，支持多后端执行**

Camel 是图原生的通用编程语言，以 AI（模型训练与部署）为主要应用场景。程序直接以计算图形式书写，优化、自动微分（grad 图重写）、GPU 执行与 ONNX/C++ 导出均为图到图的 pass，可在命令行组合或用 Camel 自行编写。提供节点 VM、字节码 VM、JIT、并行调度器等多种后端，并支持从 Python 零拷贝数组调用 Camel 模块。通过 pip 安装，附带语言服务器、格式化器与可逐 pass 调试的调试器。当前处于 1.0 之前的活跃开发期，语言变更不保留兼容垫层。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 程序即计算图，无依赖的计算自动并行执行
- grad(f) 在编译期将函数图重写为导数图
- 多后端：节点 VM、字节码 VM、JIT、GPU 内核、ONNX、C++ 导出
- 提供语言服务器、格式化器、可逐 pass 调试的调试器

## 适用场景

- 用梯度下降等图重写方式编写模型训练程序
- 同一程序以解释、JIT、GPU 或导出 ONNX/C++ 多种方式运行
- 从 Python 调用 Camel 模块处理 NumPy 数组

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L5: **Camel** is a graph-native general-purpose programming language, with AI as its primary application.
> L34: These properties hold for every program where computation matters more than control flow. Training and deploying mo
> L58: |🚀 **Many back ends**|A node VM, a bytecode VM, a JIT, a parallel scheduler, GPU kernels, ONNX and standalone C++ —

## 星数曲线

```mermaid
xychart-beta
    title "OpenCML/Camel 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `c041b1940491` · [字段定义](../../DATASET.md)*
