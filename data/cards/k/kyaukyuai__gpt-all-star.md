# kyaukyuai/gpt-all-star

⭐ 239 · Python · MIT · 推送 2026-10-20 · [GitHub](https://github.com/kyaukyuai/gpt-all-star) · [官网](https://kyaukyuai.github.io/gpt-all-star/) · 个人维护

**多 AI agent 协作从零生成 Web 应用的代码生成工具**

研究项目：由多个自主 AI agent 组成团队，从零开发 Web 应用。机制上为每个步骤选择 leader agent 制定行动计划，再与成员 agent 协作完成各任务；通过环境变量配置 OpenAI/Azure/Anthropic 端点与模型。以 Python 包发布（pip 安装、CLI 运行），开发者路径推荐 Docker compose 启动并开放 7681 端口 Web 终端，依赖 poetry 管理。当前验证范围限于 React + ChakraUI + JavaScript 的客户端应用，其他语言库欢迎贡献。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 多 agent 团队协作：每步选定 leader 制定行动计划并分配成员执行
- 支持 OpenAI/Azure/Anthropic 端点切换（环境变量配置）
- 提供 CLI 与 Docker compose 运行方式，含 7681 端口 Web 终端
- team 成员可通过 agents.yml 自定义

## 适用场景

- 用自然语言指令让 AI agent 团队从零搭建 Web 应用
- 研究自主多 agent 协作的代码生成流程
- 通过自定义 agents.yml 调整团队角色分工

## 场景标签

 · 领域:开发工具/代码生成

## 证据(README 行号)

> L5: AI-powered code generation tool for scratch development of web applications with a team collaboration of autonomous 
> L18: - **AI Agent Collaboration**: Assemble a group of AI agents and work together to carry out the steps.
> L107: This is a research project and the main focus is currently on validating `Client Web Applications` in `React` and 

## 星数曲线

```mermaid
xychart-beta
    title "kyaukyuai/gpt-all-star 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 238 --> 240
    line [239, 239]
```

2026-10-18 239 → 2026-10-22 239（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `fd2942310bca` · [字段定义](../../DATASET.md)*
