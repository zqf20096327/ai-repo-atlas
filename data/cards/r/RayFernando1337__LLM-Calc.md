# RayFernando1337/LLM-Calc

⭐ 258 · TypeScript · MIT · 推送 2026-02-22 · [GitHub](https://github.com/RayFernando1337/LLM-Calc) · [官网](https://llm-calc.rayfernando.ai) · 个人维护

**计算可用 RAM 能容纳的量化 LLM 最大参数量的网页计算器**

React + TypeScript + Vite 构建的网页应用：用户输入可用 RAM、估算的操作系统内存占用、上下文窗口大小与量化位数，应用按换算逻辑（扣除系统与上下文内存后除以每参数字节数）计算可容纳的最大模型参数量（以十亿计）。面向需要为本地推理选配模型的开发者与爱好者。通过 git clone 与 bun 安装运行，界面使用 Tailwind CSS 构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 RAM、OS 占用、上下文窗口与量化位数计算最大参数量
- React + TypeScript + Vite + Tailwind CSS 网页应用
- 输出以十亿参数为单位的可容纳模型规模

## 适用场景

- 在购买或下载模型前确认本机 RAM 能跑多大的量化模型
- 对比不同量化级别下可运行的参数规模
- 为本地推理环境规划内存预算

## 场景标签

`模型量化` · 领域:训练与推理

## 证据(README 行号)

> L3: This project is a React + TypeScript + Vite application that calculates the maximum number of parameters that can fi
> L46: 1. Enter your available RAM in GB

## 星数曲线

```mermaid
xychart-beta
    title "RayFernando1337/LLM-Calc 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 257 --> 259
    line [258, 258]
```

2026-10-18 258 → 2026-10-23 258（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `4e1bcab67d40` · [字段定义](../../DATASET.md)*
