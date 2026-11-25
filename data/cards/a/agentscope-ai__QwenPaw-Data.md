# agentscope-ai/QwenPaw-Data

⭐ 205 · Python · Apache-2.0 · 推送 2026-11-24 · [GitHub](https://github.com/agentscope-ai/QwenPaw-Data) · 组织维护 · 中文 README

**面向企业数据分析的多智能体系统：自然语言到端到端分析工作流**

由 DataBridge、Skill-Hub、Host 三个子系统构成的企业级数据分析智能体系统：DataBridge 将数仓、仪表盘、业务文档等异构资产治理为元数据图、知识图与轨迹图；Skill-Hub 组织可复用分析方法（异常检测、维度下钻、归因等）；Host 将技能物化为 DAG 执行图并管理工件与恢复。提供浏览器 Console、CLI、Headless HTTP/SSE 引擎和 QwenPaw App 集成四种接入方式，本地安装无需登录或账户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三子系统架构：事实治理（DataBridge）、方法编排（Skill-Hub）、执行控制（Host）
- 自然语言请求分解为 DAG 工作流，支持并行分支与 SQL/Python/文件工具调用
- 任务轨迹与反馈转化为可复用经验的自进化机制
- Python + uv 工作区 monorepo，包含七个包并发布至 PyPI

## 适用场景

- 业务指标监控与异常归因诊断（DAU、收入、转化率）
- 月度/季度周期性业务报告的自动生成
- 通过对话对数据做即席多维深挖分析
- 将分析引擎以 HTTP/SSE 服务集成到自有应用

## 场景标签

`多智能体` `数据分析` · 领域:Agent 开发

## 证据(README 行号)

> L11: **QwenPaw-Data is an agentic data system built for enterprise data analysis.**
> L17: QwenPaw-Data organizes its system design around three core dimensions: **facts**, **methodology**, and **execution*
> L44: The design principle of QwenPaw-Data is to decompose enterprise data analysis according to the core questions an AI

## 星数曲线

```mermaid
xychart-beta
    title "agentscope-ai/QwenPaw-Data 星数(近 21 点)"
    x-axis ["2026-10-23", "2026-10-24", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-16", "2026-11-18", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-25"]
    y-axis "stars" 165 --> 208
    line [168, 172, 173, 174, 177, 179, 182, 184, 186, 172, 192, 193, 195, 196, 197, 198, 201, 202, 204, 205, 205]
```

2026-10-23 168 → 2026-11-25 205（+37）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 mid · 依据 README sha `e504a82e1075` · [字段定义](../../DATASET.md)*
