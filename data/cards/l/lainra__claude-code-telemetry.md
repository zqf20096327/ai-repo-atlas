# lainra/claude-code-telemetry

⭐ 45 · JavaScript · MIT · 推送 2026-10-17 · [GitHub](https://github.com/lainra/claude-code-telemetry) · [官网](https://github.com/lainra/claude-code-telemetry#readme) · 个人维护

**将 Claude Code 遥测数据转发到 Langfuse 的本地监控桥**

轻量级遥测桥接器：通过 OpenTelemetry 采集 Claude Code 的 OTLP 遥测数据，解析并转发到自托管的 Langfuse 进行可视化。功能包括按会话/用户/模型追踪成本、Token 与缓存命中统计、工具使用记录、自动将相关工作聚合为 1 小时会话。提供 quickstart 脚本（含 Langfuse 仪表盘）、仅运行桥接的 NPM 与 Docker 三种安装方式；数据保留在本地基础设施上，可选是否记录 prompt。限制：不评估代码质量、不计算 ROI、无团队协作共享功能。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenTelemetry 采集 → 桥接解析 → Langfuse 可视化的数据链路
- 按会话/用户/模型的成本与 Token 用量追踪
- 自动将相关工作聚合成 1 小时会话
- 数据全部保留在本机，prompt 记录可选

## 适用场景

- 追踪我或团队使用 Claude Code 的成本与用量
- 查看每分钟会话中各模型的调用明细与花费
- 把 AI 工具使用数据保留在自己的基础设施上

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L16: Claude Code Telemetry is a lightweight bridge that captures telemetry data from Claude Code and forwards it to Lang
> L84: Claude Code → OpenTelemetry → Telemetry Bridge → Langfuse

## 星数曲线

```mermaid
xychart-beta
    title "lainra/claude-code-telemetry 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-28"]
    y-axis "stars" 44 --> 47
    line [46, 45, 45]
```

2026-10-18 46 → 2026-10-28 45（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c3d8f42a2121` · [字段定义](../../DATASET.md)*
