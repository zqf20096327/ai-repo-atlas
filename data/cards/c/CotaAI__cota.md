# CotaAI/cota

⭐ 31 · Python · MIT · 推送 2026-01-07 · [GitHub](https://github.com/CotaAI/cota) · [官网](https://cotaai.github.io/cota/) · 组织维护 · 中文 README

**通过标注思维链对话示例构建领域对话智能体的平台**

面向业务开发者、领域专家与 AI 工程师的对话智能体（Agent）构建平台：用户以 YAML 编写带 thought 标注的对话示例，系统学习思维模式形成对话策略（DPL），新对话触发时检索相似思维并执行决策；架构遵循 Dialogue State Tracker（DST），内置多轮对话、Form 填写、Action 执行。LLM 通过 endpoints.yml 配置 OpenAI 兼容 API 接入（示例为 GLM-4）。提供 pip 与源码（Poetry）两种安装方式，要求 Python 3.12+，支持 CLI 调试与 WebSocket 服务启动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YAML 标注思维链对话示例即定义业务策略，零代码配置
- 基于 DST 架构与 DPL 对话策略学习，思维链可追踪
- 内置多轮对话、Form 填写、Action 执行等生产级能力
- 提供 cota init / shell / run 命令行工具与 WebSocket 服务

## 适用场景

- 不会编程的领域专家通过编写对话示例构建 AI 助手
- 为垂直业务场景构建可追溯决策的对话智能体
- 用命令行调试并部署对话服务到生产环境

## 场景标签

`聊天机器人` `AI 助手` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L29: COTA采用**标注式策略学习**，将领域知识以思维链的形式注入：
> L33: 2. COTA学习思维模式 → 构建决策策略 (DPL)

## 星数曲线

```mermaid
xychart-beta
    title "CotaAI/cota 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-31 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `81dde5ee8b41` · [字段定义](../../DATASET.md)*
