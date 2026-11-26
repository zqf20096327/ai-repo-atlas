# OmniJev/Flide

⭐ 571 · Python · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/OmniJev/Flide) · [官网](https://flide.org) · 个人维护

**决策模型推理引擎：精确状态分叉加速多问题批量推理**

面向 Jev 风格决策模型的推理服务基础设施，核心机制为 exact state forking：一份 KV 状态分叉给多个问题，各自一次前向传播即得答案，适合对同一输入并行提出多个问题（如每封邮件打 8 个标签）的场景。提供 `/v1/systemone` API 与 `flide serve`，支持会话缓存、批次不变输出、FP8 量化与多前端进程选项。依赖 NVIDIA GPU，支持 Linux 与 Windows WSL2，经 PyPI 或 Docker 镜像安装，附论文与引用条目。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- exact state forking：一个状态分叉多问题，每问题一次前向传播
- 提供 /v1/systemone API 与 flide serve 服务
- 支持 FP8 量化、会话缓存、批次不变输出与张量并行
- README 列出 40+ 个决策模型与聊天模型的适配与延迟对比表

## 适用场景

- 对同一输入并行提出多个问题的批量推理场景（如邮件分诊打标）
- 为决策模型提供本地推理服务与 API
- 在自有模型与请求上验证精确分叉结果（flide verify）
- Agent 多步骤会话中只读取新增内容的会话缓存场景

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L15: Flide is fast inference infrastructure for Jev-style decision models. With exact state forking it is up to 9.5 time
> L51: Flide runs on an NVIDIA GPU under Linux or Windows WSL2. Install it with uv, or pull the Docker image.
> L54: uv pip install flide

## 星数曲线

```mermaid
xychart-beta
    title "OmniJev/Flide 星数(近 19 点)"
    x-axis ["2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 0 --> 627
    line [3, 4, 7, 8, 29, 358, 445, 475, 489, 501, 508, 525, 538, 543, 545, 550, 553, 566, 571]
```

2026-10-29 3 → 2026-11-26 571（+568）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `6b55da20f3d4` · [字段定义](../../DATASET.md)*
