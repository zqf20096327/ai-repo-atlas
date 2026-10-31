# in-c0/updAPI

⭐ 24 · JavaScript · Apache-2.0 · 推送 2026-08-30 · [GitHub](https://github.com/in-c0/updAPI) · 个人维护

**API 演化数据集与编码 agent 时效性基准**

UpdAPI 跟踪真实 API/SDK 随时间的变化，将经核验、带时间戳的变更事件（新增/弃用/移除/签名变更等）转为可复现的评测案例，用于测量前沿编码模型与 agent 对 API 变化的适应速度（time-to-adoption）。产出三部分：API 演化数据集、前沿 API 时效性基准（验证任务成功率、陈旧 API 错误率、恢复率等指标）、公共 API Freshness Observatory。2026 年 8 月方向重置：原 API 文档索引转为数据采集基础设施，不再是核心产品。工具链本地运行，无 CI 依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 时间戳化、可溯源的真实 API 变更事件数据集
- 以编码 agent 为整体系统的时序评测（time-to-adoption 可测量）
- 对照实验：无检索模型/正常工具/禁网搜索/提供当前文档/RAG/MCP 等条件消融
- 基准工具链本地运行（bench:validate、bench:controls 陈旧对照校验）

## 适用场景

- 评估编码 agent 在 API 变化后的适应与修复速度
- 研究 web 搜索/RAG/文档供给对 agent 成功率的实际提升
- 纵向追踪各编码系统 API 知识滞后情况

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L5: UpdAPI tracks API evolution over time and turns verified, timestamped changes into reproducible evaluation cases for
> L57: Verified API-change events become evaluation cases for contemporary coding systems.
> L127: Rather than asking whether a model has memorised an old benchmark, UpdAPI can observe how quickly coding systems a

## 星数曲线

```mermaid
xychart-beta
    title "in-c0/updAPI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-31 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `fd9c673c33a6` · [字段定义](../../DATASET.md)*
