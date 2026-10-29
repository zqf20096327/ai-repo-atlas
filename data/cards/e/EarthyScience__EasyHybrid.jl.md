# EarthyScience/EasyHybrid.jl

⭐ 27 · Julia · MIT · 推送 2026-10-28 · [GitHub](https://github.com/EarthyScience/EasyHybrid.jl) · [官网](https://earthyscience.github.io/EasyHybrid.jl/stable/) · 组织维护

**Julia 混合建模框架：把神经网络嵌入过程机理模型并联合训练**

Julia 语言的科学计算包，提供将神经网络与过程机理模型集成的混合建模框架：神经网络 h(x;θ) 预测样本级参数（如基础呼吸 rb），机理模型 M 接收该预测与强迫变量，输出预测值，参数可设为已知、固定或从数据学习。框架自动处理两部分的集成，支持带边界的参数设定与训练过程可视化，可读取 NetCDF 时间序列数据。README 标注为开发中（Work in progress），由欧盟 Horizon Europe AI4SoilHealth 与 ERC USMILE 项目资助，面向生态系统等地球科学建模场景的研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 神经网络预测样本级参数并与机理模型 Q10 等集成的混合建模框架
- 参数支持固定、已知或全局学习，可设定上下边界
- 内置训练函数 train 与基于 WGLMakie 的交互式训练可视化
- 读取远程 NetCDF 时间序列数据作为输入

## 适用场景

- 在生态呼吸等机理模型中用神经网络预测难以测定的参数
- 结合领域知识与数据驱动学习进行时间序列建模
- 科研项目中复现或扩展混合建模实验

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L20: `EasyHybrid.jl` provides a simple and flexible framework for hybrid modeling, enabling the integration of neural ne
> L73: 1. **Process-based Model**: The `RbQ10` function represents a classical Q10 model for respiration with base respira

## 星数曲线

```mermaid
xychart-beta
    title "EarthyScience/EasyHybrid.jl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-29 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c2fd51e927ea` · [字段定义](../../DATASET.md)*
