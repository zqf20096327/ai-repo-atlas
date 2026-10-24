# xieguigang/sciBASIC

⭐ 79 · Visual Basic .NET · GPL-3.0 · 推送 2026-10-23 · [GitHub](https://github.com/xieguigang/sciBASIC) · [官网](http://sciBASIC.NET/) · 个人维护

**VB.NET 科学计算语言内核与运行时，含深度学习与 LLM 推理**

用 Microsoft VisualBasic.NET 编写的跨平台科学计算框架，包含 100+ 个类库项目，分为核心运行时（扩展 VB 语法、CLI 框架、SIMD 数学）、数据框架（NetCDF/HDF5 等科学文件 I/O）、机器学习与深度学习（CNN/Transformer/GNN/SNN 等）、纯托管 decoder-only LLM 引擎（MoE、KV cache、函数调用）、CUDA GPU 加速层和可视化引擎。提供 `vbs` 脚本引擎直接运行 .vb 脚本，无需建工程。面向需要可脚本化、可复现数据处理流水线的科研与开发者，以 NuGet 包或源码构建方式使用；GPU 加速为可选，其余功能可 CPU-only 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯托管 decoder-only LLM 实现：MoE、KV cache、RoPE、schema 约束函数调用
- 纯 VB.NET 实现的深度学习套件（CNN/RNN/Transformer/GNN/LNN/SNN/DQN），不依赖 PyTorch/TensorFlow
- `vbs` 脚本引擎：顶层语句直接运行 .vb 脚本，可升级为正式工程
- 统一 NumericTable 数据模型贯通整个数据科学流水线，免转换胶水代码

## 适用场景

- 用 BASIC 风格脚本完成数据读取、建模与出版级图表输出
- 在 .NET 环境中做深度学习与 LLM 推理而无需 Python 栈
- 读取 NetCDF/HDF5 等科学数据格式并做统计分析与降维

## 场景标签

`数据分析` `推理引擎` · 领域:效率与自动化

## 证据(README 行号)

> L25: |**Math & data science**|`Data_science/`|Numerical math, statistics, ODE solvers, **deep learning (CNN / RNN / Tran
> L26: |**LLM engine**|`llm/`|A pure-managed **decoder-only LLM** implementation: MoE, KV cache, RoPE, function calling wi
> L56: - **LLM inference & training** — decoder-only Transformer with MoE experts, KV cache prefill +

## 星数曲线

```mermaid
xychart-beta
    title "xieguigang/sciBASIC 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 78 --> 80
    line [79, 79]
```

2026-10-18 79 → 2026-10-24 79（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `01a77223f1d1` · [字段定义](../../DATASET.md)*
