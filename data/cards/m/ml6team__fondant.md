# ml6team/fondant

⭐ 358 · Python · Apache-2.0 · 推送 2026-02-20 · [GitHub](https://github.com/ml6team/fondant) · [官网](https://fondant.ai/en/stable/) · 组织维护

**构建与共享可复用数据处理流水线的 Python 数据框架**

面向数据从业者的数据集协作构建框架：以数据集为核心单元，通过可组合的操作（加载、过滤、加工、写出）生成新数据集，操作与完整处理血缘可共享，且不移动源数据。提供 Pandas 接口编写自定义组件、内置 CLI 运行与编译流水线、组件库与数据浏览器，支持本地 Docker 及 Vertex、SageMaker、Kubeflow 等云端 runner。附带 RAG 评测、ControlNet 微调数据等示例流水线。面向微调与基础模型场景的数据准备。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可组合的即插即用数据处理流水线与现成组件库
- Pandas 接口编写自定义组件
- 内置血缘、缓存与数据浏览器
- 支持 Vertex / SageMaker / Kubeflow 等云端 runner 与本地 Docker

## 适用场景

- 为模型微调构建并清洗数据集
- 复用他人共享的操作与数据集继续加工或分支
- 在云端托管服务上执行数据处理流水线

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L17: Fondant is a data framework that enables collaborative dataset building. It is designed for developing and crafting
> L19: Fondant enables you to initialize datasets, apply various operations on them, and load datasets from other users. I
> L75: - ☁️ Integration with runners across different clouds (Vertex on Google Cloud, Sagemaker on AWS, Kubeflow on any k8

## 星数曲线

```mermaid
xychart-beta
    title "ml6team/fondant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 357 --> 359
    line [358, 358]
```

2026-10-18 358 → 2026-10-23 358（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `6d00d16356f8` · [字段定义](../../DATASET.md)*
