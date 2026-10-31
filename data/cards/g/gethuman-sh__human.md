# gethuman-sh/human

⭐ 68 · Go · MIT · 推送 2026-10-15 · [GitHub](https://github.com/gethuman-sh/human) · [官网](https://gethuman.sh) · 组织维护

**面向团队的 AI 开发一体化工作台：接入追踪器与文档并安全运行编码代理**

开源的 AI 开发装备套件：把 Jira/GitHub/Linear 等问题追踪器、Notion 文档、Figma 设计、Amplitude 分析通过统一连接器接入，配合代码索引与跨源搜索供 AI 使用；以守护进程+devcontainer 客户端架构运行 Claude Code 于隔离沙箱，提供出站防火墙、密钥脱敏文件系统、凭据保管与审计日志。CLI 支持工单读写，另含 Wails 桌面流水线看板与 Claude Code 技能安装。面向希望统一装配并管控 AI 编码代理的团队。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一连接 7+ 问题追踪器与 Notion/Figma/Amplitude，跨源全文搜索
- daemon+devcontainer 分体架构，凭据留在宿主机，代理运行于隔离容器
- 出站防火墙（SNI 域名过滤）、密钥脱敏文件系统、审计与破坏性操作日志
- 结构化代码导航与信号提取，宣称最多节省 95% token

## 适用场景

- 为编码代理统一接入工单、文档、设计与分析数据源
- 在隔离沙箱中运行 Claude Code 并管控其凭据与出站访问
- 用桌面看板驱动从创意到评审的流水线并跟踪成本

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L15: **human is your team's AI dev rig** — everything your AI development needs, best of breed, already wired. Trackers,
> L115: - AI Developer Agents — run Claude Code in isolated containers

## 星数曲线

```mermaid
xychart-beta
    title "gethuman-sh/human 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 67 --> 69
    line [68, 68]
```

2026-10-18 68 → 2026-10-31 68（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `4292f4d1d6d1` · [字段定义](../../DATASET.md)*
