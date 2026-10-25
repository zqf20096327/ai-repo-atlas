# EliaAlberti/dcode-agent-kit

⭐ 57 · MIT · 推送 2026-06-23 · [GitHub](https://github.com/EliaAlberti/dcode-agent-kit) · 个人维护

**Claude Code 技能：一键脚手架生成可运行的 Deep Agents 智能体**

一个 Claude Code skill（SKILL.md 插件），通过 /new-dcode-agent 命令在任意项目中进行问答式访谈，随后生成自包含的可运行 agent 文件夹（agent.py + model.py + README.md），基于 LangChain Deep Agents 框架与 dcode CLI。支持三种形态：独立 SDK 程序、dcode 交互 agent 或两者结合。生成的 agent 通过环境变量接入任意 OpenAI 兼容 API，无厂商锁定；可变更系统状态的 agent 默认带审批门。安装后生成物会做一次冒烟测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 访谈式四步流程：访谈→规格确认→脚手架→冒烟测试
- 生成自包含 agent 文件夹（agent.py + model.py + README.md），可迁移部署
- 任意 OpenAI 兼容 API 接入（LLM_API_KEY / LLM_BASE_URL / LLM_MODEL 环境变量）
- 可变更类 agent 默认带 approval gate，动作前暂停确认

## 适用场景

- 在现有项目中快速生成一个可部署的自动化 Python agent
- 为 dcode CLI 创建带独立知识与规则的交互式 agent 身份
- 按自己的模型网关/provider 定制 agent 而不绑定厂商

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L11:  A Claude Code skill that scaffolds a Deep Agents (LangChain) agent for you: it interviews you, then drops a ready-
> L69: **Deep Agents** is a LangChain framework for building capable AI agents in Python. You call `create_deep_agent(...)

## 星数曲线

```mermaid
xychart-beta
    title "EliaAlberti/dcode-agent-kit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 56 --> 58
    line [57, 57]
```

2026-10-18 57 → 2026-10-25 57（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `32524774d0b7` · [字段定义](../../DATASET.md)*
