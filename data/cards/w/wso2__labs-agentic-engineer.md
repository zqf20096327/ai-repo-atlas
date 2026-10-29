# wso2/labs-agentic-engineer

⭐ 25 · Go · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/wso2/labs-agentic-engineer) · 组织维护

**WSO2 实验平台：在企业平台内用多 agent 驱动软件开发全流程**

构建在 OpenChoreo 之上的实验性开源平台，将 SDLC 拆为 Specification→Design→Implementation→Build→Deploy→Manage 各阶段，每阶段配备专用 agent；需求以 Git 仓库中的 spec 文件为契约，编码 agent 通过 GitHub issue/分支/PR 执行任务（合并需人工评审），由 webhook 驱动任务状态流转。本地运行依赖 k3d 集群部署 OpenChoreo、Thunder 身份服务与 AEP 服务，模型连接支持 Anthropic Messages 或 OpenAI 兼容接口，编码 agent 以一次性 Pod 运行 Claude Agent SDK。README 自声明为早期实验室项目，API 与数据模型仍会变动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- SDLC 六阶段各配备专用 agent，共享跨制品上下文
- spec 文件（需求/设计/原型/领域模型）作为下游 agent 的工作契约
- 编码 agent 经 GitHub issues/branches/PRs 工作，合并需人工评审，以一次性 Pod 调度
- 本地以 k3d + aectl 部署整个平台，模型连接支持 Anthropic Messages 或 OpenAI 兼容格式

## 适用场景

- 企业内从需求澄清到部署的 agent 驱动软件开发
- 业务负责人通过对话引导需求抽取，产出规格与原型
- 在已有 API 管理、身份、部署与可观测性平台内运行编码 agent

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L9: An experimental, open-source platform that explores what **agent-driven software
> L30: It treats the SDLC as a chain of stages — **Specification → Design → Implementation
> L155: |`runners/`|`remote-worker`, the coding agent: a one-shot pod running the Claude Agent SDK. One image serves imple

## 星数曲线

```mermaid
xychart-beta
    title "wso2/labs-agentic-engineer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-29 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `aa0c82bf3225` · [字段定义](../../DATASET.md)*
