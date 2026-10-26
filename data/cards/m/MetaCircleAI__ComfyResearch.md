# MetaCircleAI/ComfyResearch

⭐ 32 · TypeScript · MIT · 推送 2026-08-11 · [GitHub](https://github.com/MetaCircleAI/ComfyResearch) · 组织维护 · 中文 README

**本地可视化工作台：以节点图构建可复现的机器学习实验**

面向 AI/机器学习研究者的本地可视化实验工作台：将数据集、模型、损失、优化器与 Trainer 连接为类型化边定义的可执行节点图，通过 FastAPI 与 PyTorch 后端运行训练；可挂载 Observables 测量学习动力学（如 Hessian 特征值、Edge of Stability 复现），并保存含上下文的研究工件用于对比。实验可在 CPU/MPS/CUDA 间迁移，也可配置远程 SSH GPU 主机。要求 Python 3.10+ 与 Node.js 20+，从源码克隆构建前端运行，当前仓库需 GitHub 组织授权访问。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 节点图可执行：类型化边定义依赖并发送到 PyTorch 训练后端
- Observables 机制：挂载学习动力学诊断而不改变优化目标
- 实验可在 CPU/MPS/CUDA 与远程 SSH GPU 主机间迁移
- 内置 Edge of Stability (CPU) 定性复现模板

## 适用场景

- 在可视化界面搭建并运行可复现的 ML 训练实验
- 测量并对比学习动力学（损失历史、Hessian 特征值等）
- 把本地实验迁移到远程 SSH GPU 主机运行

## 场景标签

`MLOps` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L19: ComfyResearch is a local visual workbench for AI and machine-learning research. Connect a dataset, model, loss, opt
> L29: - **The graph is executable.** Typed edges define the dependencies sent to the training backend; it is not only a d
> L105: Node graph → validated training request → PyTorch execution

## 星数曲线

```mermaid
xychart-beta
    title "MetaCircleAI/ComfyResearch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-26 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `806fcb128154` · [字段定义](../../DATASET.md)*
