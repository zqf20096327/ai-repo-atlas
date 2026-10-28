# google-deepmind/simulation_streams

⭐ 28 · Python · Apache-2.0 · 推送 2026-09-23 · [GitHub](https://github.com/google-deepmind/simulation_streams) · 组织维护

**用 LLM 构建复杂模拟的开发平台（ECS + 图形编辑器）**

DeepMind 发布的基于 LLM 的模拟开发平台：采用 Entity-Component-Systems 范式，附带在浏览器中显示的图形编辑器。平台为 Flask 应用，建议在本地 venv 中通过 source setup.sh 安装，支持 Web 服务器、命令行分步运行与编辑器三种启动方式。configs 目录内置市场经济、社会模拟及 6 个经典强化学习任务的示例配置；code_world 配置允许用纯 Python 实现自定义环境。示例命令以 Gemini 模型与 API key 运行。附 arXiv 论文引用；声明非 Google 官方支持产品。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Entity-Component-Systems 范式与浏览器图形编辑器
- 内置市场经济、社会模拟与 6 个经典 RL 任务配置
- code_world 通用配置支持纯 Python 自定义环境
- Flask 应用本地运行，支持 Web/命令行/编辑器三种模式

## 适用场景

- 用 LLM 搭建社会模拟或市场经济模拟
- 将经典强化学习任务作为 LLM 模拟配置运行
- 通过图形编辑器设计模拟流程并查看指标

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: A development platform for simulations with large language models.
> L6: It comes with an Entity-Component-Systems approach and graphical editor.

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/simulation_streams 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-28 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `b2deb93599e4` · [字段定义](../../DATASET.md)*
