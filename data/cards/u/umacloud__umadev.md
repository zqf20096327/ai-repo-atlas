# umacloud/umadev

⭐ 264 · Rust · MIT · 推送 2026-09-29 · [GitHub](https://github.com/umacloud/umadev) · [官网](https://umadev.goder.ai) · 组织维护 · 中文 README

**编排既有 AI 编码 CLI 的角色化团队式编码代理**

Rust 单二进制编码代理，自身不含模型端点，驱动 Claude Code、Codex、OpenCode、Grok Build、Kimi Code 五种基础 CLI 之一执行编码任务。核心机制是基于角色的团队编排：协调者路由需求、维护可见计划，八个专家角色（产品、架构、UI/UX、前后端、QA、安全、DevOps）以受限会话产出制品与咨询性裁决；从需求澄清、研究、PRD/架构/UI 文档到实现与质量门禁全流程治理，产出交付包。限制：需自行安装并登录一个基础 CLI，角色裁决为咨询性质。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 驱动五种基础编码 CLI，UmaDev 自身无需额外模型 API key
- 协调者+八角色的受限会话编排与结构化裁决
- 从需求到交付的全流程治理（PRD、执行计划、质量门禁、证据包）
- 单 Rust 二进制，内置策展知识库，检索支持 BM25 与可选本地嵌入模型

## 适用场景

- 让已有 Claude Code/Codex 等 CLI 按团队流程交付完整项目
- 为 AI 生成代码附加 PRD、架构文档与质量报告等交付证据
- 以计划与审计轨迹管理多阶段编码任务

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L14: umadev is **a coding agent that works like a real dev team**. It drives one of five first-class AI coding CLIs you 
> L16: What you get is **role-based team orchestration** over that borrowed brain. For work whose depth warrants it, bound
> L18: A ninth seat, the **coordinator**, routes the request, owns a visible plan for deliberate work, schedules the selec

## 星数曲线

```mermaid
xychart-beta
    title "umacloud/umadev 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 262 --> 266
    line [263, 265, 264]
```

2026-10-18 263 → 2026-10-27 264（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `cea353ddc55c` · [字段定义](../../DATASET.md)*
