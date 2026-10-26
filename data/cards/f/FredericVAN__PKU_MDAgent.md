# FredericVAN/PKU_MDAgent

⭐ 40 · Jupyter Notebook · GPL-3.0 · 推送 2026-09-16 · [GitHub](https://github.com/FredericVAN/PKU_MDAgent) · [官网](https://www.nature.com/articles/s41598-025-92337-6) · 组织维护

**材料科学分子动力学 Agent：LLM 生成/执行/优化 LAMMPS 仿真代码**

北京大学发表于 Scientific Reports 的分子动力学智能体（MDAgent）：基于微调 LLM 的 text-to-code 生成框架，自动生成、执行并迭代优化基于 LAMMPS 的热力学仿真代码，获取材料热力学参数。架构含 Manager、Worker（LAMMPS/MATLAB）、Evaluator，运行于 AutoGen 之上，提供 Chainlit Web UI 与 CLI 两种交互方式，支持 OpenAI 兼容服务与 Ollama 作为模型提供方。附带两个数据集：LSCF（167 条 LAMMPS 脚本微调集）与 LEQS（专家评分评测集），微调使用 Unsloth 框架。安装为 Python 虚拟环境 + requirements.txt，代码执行器支持 Docker 模式，可选 Azure 搜索与 RAGFlow 检索工具。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动生成、执行与迭代优化 LAMMPS 热力学仿真代码
- Manager/Worker/Evaluator 多智能体架构，Evaluator 评分驱动代码迭代
- LSCF 微调数据集（167 条 LAMMPS 脚本）与 LEQS 专家评分评测集
- 支持 OpenAI 兼容 API 与 Ollama 本地模型，提供 Chainlit UI 与 CLI

## 适用场景

- 让 AI 代写并优化 LAMMPS 热力学仿真脚本，降低使用门槛
- 计算材料热力学参数（热膨胀系数、热导率、密度、相变等）
- 用专家评分数据集评测 LLM 生成的 LAMMPS 脚本质量

## 场景标签

`多智能体` `编码 Agent` `科研工具` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L22: 🚀 **Molecular Dynamics Agent (MDAgent)** — a fine-tuned **text-to-code generation agent** empowered by **large lang
> L26: * 📦 **Automatic generation** , **execution** , and **refinement** of **thermodynamic simulation code**
> L302: image-20250218203901925

## 星数曲线

```mermaid
xychart-beta
    title "FredericVAN/PKU_MDAgent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-26 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `93a3dce7e21a` · [字段定义](../../DATASET.md)*
