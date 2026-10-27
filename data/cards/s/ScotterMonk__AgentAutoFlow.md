# ScotterMonk/AgentAutoFlow

⭐ 37 · Python · CC0-1.0 · 推送 2026-06-22 · [GitHub](https://github.com/ScotterMonk/AgentAutoFlow) · [官网](https://OceanMedia.net) · 个人维护

**AI 编码团队的自定义指令集：扩展 Kilo/Roo/Cline 的多模式协作**

一套 markdown 指令文件与脚本，用于增强和扩展 Kilo Code、Roo Code、CLine 等编码代理的内置模式：新增 Architect Super Team（三步 Planner 流程）、Architect Quick、Dispatcher、Coder-Sr、Coder-Jr 等模式，并附多个技能文件（Agent Skills 开放格式）。采用规格驱动+测试驱动组合，核心机制是把高成本推理前置到规划阶段、由低成本模型执行原子任务以节省 token。文件放入项目根目录并按需修改即用，兼容多种编码代理框架。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | CC0-1.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Architect Super Team 三步 Planner 流程（planner-a/b/c）
- 规划阶段前置高推理模型、Dispatcher/Coder 用低成本模型的分层设计
- 附带 .kilocode/skills 技能文件夹，采用 Agent Skills 开放格式
- 兼容 Kilo Code、Roo Code、CLine、Cursor 等多种编码代理

## 适用场景

- 为编码代理配置多角色开发团队以构建新应用
- 在现有项目中按规划-分发-编码流程修改或修 bug
- 通过分层模型分配降低编码代理的 token 成本

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: Your customizable AI coding team that learns!
> L6: This set of instructions (markdown files and scripts) enhances and extends the modes/agents that come with many codi

## 星数曲线

```mermaid
xychart-beta
    title "ScotterMonk/AgentAutoFlow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-27 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `8e501c3a60f9` · [字段定义](../../DATASET.md)*
