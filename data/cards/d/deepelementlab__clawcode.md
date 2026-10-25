# deepelementlab/clawcode

⭐ 126 · Python · GPL-3.0 · 推送 2026-05-21 · [GitHub](https://github.com/deepelementlab/clawcode) · [官网](https://ideepe.com/clawcode.html) · 组织维护 · 中文 README

**面向开发者的开源编码 agent 平台，带经验学习与多 agent 协作**

用 Python 与 Rust 实现的终端原生编码 agent 平台：提供 TUI/非交互两种运行方式、基于角色的多 agent 编排（/clawteam、/designteam、ResearchTeam）、文件/Shell/浏览器/MCP 等工具执行面、研究流水线（deepresearch、peerreview、lit、audit、compare）、DeepNote 知识库子系统，以及 Instinct→ECAP→TECAP 三层经验学习模型，把会话中的工具痕迹转化为可复用工件。支持 54 个品牌设计系统路由与 12 个内置垂直领域扩展。模型层 provider 无关，可通过 OpenAI 兼容端点接入多种模型。安装方式为源码 venv + pip install -e，要求 Python ≥ 3.12；许可证 GPL-3.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Instinct→ECAP→TECAP 三层经验学习模型，将会话行为转化为可版本化复用技能
- /clawteam 多角色编排：架构/实现/QA/交付专家协作，含收敛检测与回滚
- 研究子系统：5 种工作流 + ResearchTeam 并行专家角色与合并策略
- DeepNote 知识库：wiki 工具集、Notion 导入、Obsidian 兼容导出

## 适用场景

- 在终端里让多角色 agent 团队完成 API 重构、微服务设计等工程任务
- 跑证据驱动的研究流水线（文献综述、同行评审、对比分析）
- 把团队工程经验沉淀为可复用的机构记忆（ECAP/TECAP）
- 按品牌设计系统生成风格一致的 UI 设计产物

## 场景标签

`多智能体` `科研工具` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L9:  Open-source coding agent platform with terminal-native execution, multi-agent orchestration, closed-loop learning, 
> L42: Today, ClawCode combines **agent runtime**, **tool execution**, **workflow orchestration**, and **experience learni
> L58: Your tools should serve your workflow, not a vendor's ecosystem. Provider-agnostic model layer, OpenAI-compatible e

## 星数曲线

```mermaid
xychart-beta
    title "deepelementlab/clawcode 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25"]
    y-axis "stars" 124 --> 127
    line [125, 126, 126]
```

2026-10-18 125 → 2026-10-25 126（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `3515b714d751` · [字段定义](../../DATASET.md)*
