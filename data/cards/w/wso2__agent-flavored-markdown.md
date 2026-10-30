# wso2/agent-flavored-markdown

⭐ 26 · CSS · NOASSERTION · 推送 2026-10-20 · [GitHub](https://github.com/wso2/agent-flavored-markdown) · 组织维护

**用 Markdown+YAML 定义可移植 AI Agent 的开放规范**

由 WSO2 维护的开放规范：以 Markdown 文件加 YAML front matter 的声明式格式定义 AI agent，将自然语言指令与框架技术配置分离，使 agent 定义可在不同平台与框架间迁移。面向不写框架代码的领域专家与开发者，提供无代码途径。仓库主体为规范文档（spec/docs/specification.md），附 MkDocs 文档站点与 Docker 构建流程，并有 IUI 2026 AgentCraft workshop 论文可供引用。不含运行时实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Markdown + YAML front matter 的声明式 agent 定义格式
- 指令与配置分离，定义跨框架可移植
- 领域专家无需编程即可编写 agent 定义

## 适用场景

- 以平台无关格式编写和迁移 AI agent 定义
- 让非技术领域专家参与 agent 编写
- 作为论文引用或跨工具交换 agent 规范

## 场景标签

 · 领域:AI agent 标准化/规范

## 证据(README 行号)

> L3: A specification for no-code, portable AI Agents.
> L7: AFM (Agent-Flavored Markdown) is an open specification for defining AI agents in a simple, declarative, Markdown-bas
> L9: Most AI agent frameworks intertwine agent instructions with technical configurations, obscuring the core agent logic

## 星数曲线

```mermaid
xychart-beta
    title "wso2/agent-flavored-markdown 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-30 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `b6db1c0857d8` · [字段定义](../../DATASET.md)*
