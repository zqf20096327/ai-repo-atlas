# runpod/serverless-workers

⭐ 63 · Python · MIT · 推送 2026-10-20 · [GitHub](https://github.com/runpod/serverless-workers) · [官网](https://github.com/runpod-workers) · 组织维护

**RunPod 官方 serverless worker 容器集合：模型端点部署模板**

RunPod 官方提供的 serverless endpoint worker 集合，覆盖 Stable Diffusion v1/v2、DreamBooth、Anything v3/v4、Openjourney、Whisper 等模型，以 Docker 容器形式发布于 Docker Hub，可通过 RunPod 平台部署为 API 端点。各 worker 使用 RunPod Python 包实现工作函数，并借助 Cog 打包构建容器。README 声明本仓库将被归档，各 worker 已拆分至 runpod-workers 组织下的独立仓库维护。

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

- 收录 Stable Diffusion、DreamBooth、Anything、Openjourney、Whisper 等模型 worker
- 各 worker 以 Docker 容器发布于 Docker Hub，可部署为 RunPod 端点
- 使用 RunPod Python 包实现工作函数，Cog 辅助打包
- 已宣布归档，由 runpod-workers 各独立仓库替代

## 适用场景

- 在 RunPod 上快速部署 Stable Diffusion 或 Whisper 为 serverless API
- 参考官方 worker 实现编写自定义 RunPod worker

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L1: Serverless | Endpoint Workers
> L13: All the workers us the RunPod Python Package to implement the work functions.

## 星数曲线

```mermaid
xychart-beta
    title "runpod/serverless-workers 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 61 --> 64
    line [62, 63, 63]
```

2026-10-18 62 → 2026-10-31 63（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e7e55fef58b5` · [字段定义](../../DATASET.md)*
