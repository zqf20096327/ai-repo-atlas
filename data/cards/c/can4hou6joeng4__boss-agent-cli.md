# can4hou6joeng4/boss-agent-cli

⭐ 2,301 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/can4hou6joeng4/boss-agent-cli) · [官网](https://can4hou6joeng4.github.io/boss-agent-cli/) · 个人维护 · 中文 README

**面向真人与 AI Agent 的 BOSS 直聘求职/招聘 CLI**

把 BOSS 直聘的职位发现、福利筛选、本地候选池、投递沟通与招聘者链路统一到一个 Python CLI。真人运行 boss 进入纯终端向导；Agent 可通过 MCP（暴露 83 个工具）、subprocess 解析 JSON 信封或 Python SDK 调用同一套 workflow。stdout 仅输出七键 JSON 信封，boss schema 为能力真源，可导出 openai-tools/anthropic-tools/mcp-tools 定义。附带 JD 分析、简历润色、模拟面试等 AI 功能，本地模型权重外置，经 OpenAI 兼容接口接入 Ollama/vLLM。批量采集需额外安装 crawl extra，受预算、checkpoint 与停止条件约束。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP 接入暴露 83 个工具，schema 可导出三种工具定义格式
- 福利筛选按 AND 逻辑真实匹配并支持本地匹配分排序
- 双受众设计：hints.next_actions 给 Agent、operator_actions 给真人操作者
- 本地模型权重外置，支持 Ollama/vLLM OpenAI 兼容接口

## 适用场景

- 用自然语言 Agent 帮我搜岗位、按双休五险一金筛选并管理候选池
- 让 AI 分析 JD、润色简历并做模拟面试准备
- 招聘者在终端里批量处理候选人搜索与简历接收
- 低成本环境用本地模型跑 AI 求职增强功能

## 场景标签

 · 领域:求职招聘/效率工具

## 证据(README 行号)

> L23: boss-agent-cli 把职位发现、福利筛选、本地简历与 AI、投递沟通、招聘者候选人处理和可恢复采集统一到一个 CLI。真人直接运行 `boss` 进入纯终端向导；Agent 使用 JSON、schema、MCP 或 Py
> L36: - **AI 求职增强 + 本地模型**：JD 分析、简历润色、定向优化、候选池匹配、模拟面试、沟通指导；本地模型权重外置，支持 Ollama/vLLM OpenAI 兼容接口 —— `ai analyze-jd` `ai loc
> L70: // 方式一：MCP（推荐）—— Claude Desktop / Cursor 等 MCP 宿主，暴露 83 个已实现工具

## 星数曲线

```mermaid
xychart-beta
    title "can4hou6joeng4/boss-agent-cli 星数(近 26 点)"
    x-axis ["2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 2121 --> 2320
    line [2137, 2141, 2151, 2157, 2161, 2165, 2169, 2172, 2137, 2203, 2206, 2212, 2217, 2220, 2221, 2224, 2225, 2228, 2238, 2281, 2284, 2286, 2288, 2293, 2304, 2301]
```

2026-10-25 2,137 → 2026-11-27 2,301（+164）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `bdbcf7ab95a8` · [字段定义](../../DATASET.md)*
