# sarva-20/LLM-Observability-FOSS

⭐ 36 · Python · MIT · 推送 2026-01-07 · [GitHub](https://github.com/sarva-20/LLM-Observability-FOSS) · 个人维护

**用 FOSS 工具逐步学习 LLM 可观测性的教程演示仓库**

面向 FOSS United Coimbatore Meetup 制作的 LLM 可观测性教学演示：用 5 个渐进式 Python 脚本展示从无可观测性、Langtrace 两行自动插桩、OpenTelemetry 手动插桩、Jaeger 追踪可视化到统一对比的完整路径。演示 chatbot 调用 Google Gemini API，需要配置 Gemini/Langtrace API key，Jaeger 通过 Docker 容器启动；附工具对比表（Langtrace/OpenTelemetry/OpenLLMetry/Opik/Jaeger）、架构图、troubleshooting 与 Trace/Span/Attributes 概念说明。要求 Python 3.12+，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 个渐进式脚本覆盖自动插桩、手动插桩到多框架统一对比
- 工具对比表涵盖 Langtrace/OpenTelemetry/OpenLLMetry/Opik/Jaeger
- 包含 Docker 启动 Jaeger 的追踪可视化步骤与 troubleshooting 指南

## 适用场景

- 逐步学习如何为 LLM 应用添加追踪与监控
- 对比选型开源 LLM 可观测性工具
- Meetup/教学场景的可复现演示材料

## 场景标签

`LLM 可观测性` `教程课程` · 领域:评测与运维

## 证据(README 行号)

> L6: This repository demonstrates how to add observability to LLM applications **step by step** using **Free and Open Sou
> L22: Each file shows a different stage of adding observability:

## 星数曲线

```mermaid
xychart-beta
    title "sarva-20/LLM-Observability-FOSS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-29 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `c50de6c731b7` · [字段定义](../../DATASET.md)*
