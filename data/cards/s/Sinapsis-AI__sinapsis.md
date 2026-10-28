# Sinapsis-AI/sinapsis

⭐ 41 · Python · AGPL-3.0 · 推送 2026-03-30 · [GitHub](https://github.com/Sinapsis-AI/sinapsis) · [官网](https://sinapsis.tech/) · 组织维护

**面向 AI 工作流的模块化 Agent 构建与管理平台**

Sinapsis 是一个 Python 编写的 AI 工作流框架：以可组合、可复用的 Templates 为基本单元，通过 Agents 按 YAML 声明式配置编排执行，支持拓扑排序、并行执行、执行阻塞控制与状态管理；Data Containers 原生支持图像、音频、文本、时间序列等多模态数据。提供 CLI、Docker 镜像（含 CUDA GPU 版）及覆盖异常检测、聊天机器人、OCR、目标检测、语音、时间序列等任务的系列子包。需 Python 3.10+，AGPLv3 许可另提供商业许可通道。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Templates + Agents 的声明式 YAML 工作流编排，支持拓扑排序与并行执行
- Data Containers 原生支持图像/音频/文本/时间序列等多模态数据
- 20+ 官方子包覆盖 OCR、目标检测、异常检测、聊天机器人、语音等任务
- 提供基础镜像与含 CUDA 12.4.0 的 NVIDIA 镜像

## 适用场景

- 用配置文件组合模块快速搭建端到端 AI 工作流
- 在 CV、NLP、语音、时间序列等多领域复用模板组件
- 通过 Docker 镜像获得预配置的运行环境（含 GPU 加速）

## 场景标签

`Agent 框架` `多模态` `目标检测` `OCR` · 领域:Agent 开发

## 证据(README 行号)

> L11:  Build and manage AI workflows through modular and scalable Agents based on composite and reusable Templates.
> L23:  The all-in-one AI-native platform that unifies the most powerful and innovative AI tools, from computer vision
> L167: The sinapsis framework contains a list of public packages with **Templates** covering a wide range of tasks,

## 星数曲线

```mermaid
xychart-beta
    title "Sinapsis-AI/sinapsis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-28 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `de205a3baaa1` · [字段定义](../../DATASET.md)*
