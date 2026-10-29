# Summoner-Network/summoner-agents

⭐ 25 · Python · Apache-2.0 · 推送 2026-02-19 · [GitHub](https://github.com/Summoner-Network/summoner-agents) · [官网](https://summoner.org/) · 组织维护

**Summoner 框架的 agent 示例与模板库（58 个 agent）**

面向 Summoner SDK 桌面应用的 agent 集合仓库：收录 58 个 agent，按核心消息（@send/@receive/@hook）、聊天交互、结构化反馈、图/类别编排等类别组织，以表格标注难度级别、所用 SDK 能力（core、aurora、DID、streaming、llm 等）与是否可作为模板复用。每个 agent 文件夹须遵循 agent_<name> 命名、包含 agent.py 与 requirements.txt 的严格结构，通过启动 server.py 后运行 agent.py 使用；SDK 安装指引放在组织主页，README 内提供 build_sdk.sh 与 pip 安装命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 58 个 agent 覆盖消息原语、聊天编排、反馈与图状态机等类别
- 强制目录结构（agent_<name>/agent.py/requirements.txt）以兼容桌面应用导入
- 提供 helper 脚本批量安装全部 agent 依赖（install_requirements.sh）
- 表格标注每个 agent 的难度、SDK 能力、模板/可组合属性

## 适用场景

- 学习 Summoner SDK 的 @send/@receive/@hook 等消息原语用法
- 查找可复用的 agent 模板搭建自己的 agent
- 了解图/状态机式多 agent 编排实现方式

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L22:  (Click to expand) This repository contains a collection of agent examples designed to run within the Summoner fram
> L156: There are 58 agents available in this repo.

## 星数曲线

```mermaid
xychart-beta
    title "Summoner-Network/summoner-agents 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-29 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `ba9277741d24` · [字段定义](../../DATASET.md)*
