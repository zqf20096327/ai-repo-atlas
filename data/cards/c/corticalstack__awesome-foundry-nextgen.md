# corticalstack/awesome-foundry-nextgen

⭐ 29 · Jupyter Notebook · MIT · 推送 2026-10-28 · [GitHub](https://github.com/corticalstack/awesome-foundry-nextgen) · 个人维护

**Microsoft Foundry 平台动手实验集：Notebook+Bicep 覆盖全流程**

面向 Microsoft Foundry（Azure 企业级统一 PaaS）的系列动手实验，以 Jupyter Notebook 与 Bicep 模板覆盖：平台供给、Agent 基础与托管 Agent、MCP 工具、Foundry IQ 知识库、护栏、红队测试、微调与可观测性等 16 个编号实验。全流程使用 DefaultAzureCredential 认证，不依赖管理密钥。要求 Azure CLI v2.60+、cognitiveservices 扩展与 uv 包管理器，通过 git clone 后 uv sync 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 16 个按依赖顺序组织的实验，含 Agent 子实验 15 个
- Bicep 实现 hub/spoke 架构与 Azure Policy 治理策略
- 覆盖 Prompt Shields/PII 检测/自定义黑名单三层护栏与 PyRIT 红队扫描
- 包含 Olive+PEFT(LoRA) 知识蒸馏微调实验

## 适用场景

- 按顺序学习 Microsoft Foundry 平台的供给与治理模式
- 参考 Bicep 模板搭建 hub/spoke 架构与 APIM 网关
- 实践托管 Agent、MCP 工具与护栏、红队扫描等能力

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L11: A hands-on lab series for **Microsoft Foundry NextGen** - Azure's unified PaaS for enterprise AI
> L13: provisioning, agents, hosted Copilot SDK agents, MCP tools, knowledge bases, fine-tuning, guardrails, red-teaming,

## 星数曲线

```mermaid
xychart-beta
    title "corticalstack/awesome-foundry-nextgen 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-29 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `e1c0f45bc837` · [字段定义](../../DATASET.md)*
