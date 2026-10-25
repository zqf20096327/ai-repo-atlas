# microsoft/dstoolkit-mlops-v2

⭐ 33 · Python · NOASSERTION · 推送 2026-07-10 · [GitHub](https://github.com/microsoft/dstoolkit-mlops-v2) · 组织维护

**微软基于 Azure ML 的 MLOps 模型训练项目模板**

Model Factory 是微软维护的机器学习项目仓库结构模板：以最少脚本搭建基于 Azure ML SDK v2 的训练环境，CI/CD 支持 GitHub Actions（Azure Pipelines 已弃用、触发器禁用，2026-01-31 后移除）。提供分支策略、基础设施设计、新模型接入等文档，含 nyc-taxi/london-taxi/docker_taxi 示例流水线；本地运行需 Azure CLI 与 ML 扩展，环境可选 VSCode dev container 或 conda。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Azure ML SDK v2 与 GitHub Actions 的最小脚本训练环境模板
- 提供分支策略/基础设施设计/新模型接入/初始设置测试等文档
- 本地运行支持 dev container（两种）与 conda 环境三种方式
- VS Code launch.json 内置数据资产注册与本地流水线调试任务

## 适用场景

- 团队以标准化仓库结构启动 Azure ML 模型训练项目
- 为多个模型统一管理 CI/CD 构建与分支策略
- 在本地或 dev container 中调试 Azure ML 训练流水线

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L5: The idea of this template is to provide a minimum number of scripts to implement development environment to train ne
> L13: - mlops: scripts that are related to Azure ML.

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/dstoolkit-mlops-v2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-25 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `1493cb0d4acc` · [字段定义](../../DATASET.md)*
