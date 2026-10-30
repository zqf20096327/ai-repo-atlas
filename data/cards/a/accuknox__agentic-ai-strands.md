# accuknox/agentic-ai-strands

⭐ 16 · Python · 推送 2026-08-23 · [GitHub](https://github.com/accuknox/agentic-ai-strands) · 组织维护

**演示 agentic AI 安全风险并用 KubeArmor 沙箱化的图生成应用**

基于 AWS Strands Agents SDK 构建的实验性图生成应用：用户以自然语言提示生成 Plotly 图表，agent 可执行任意 Python 代码，项目以此演示提示注入等 agentic AI 安全风险，说明仅靠 LLM 护栏不足以防护。随后给出 KubeArmor 最小权限沙箱策略，拦截并上报违规执行。提供 K8s 清单部署、Docker 镜像（仅 amd64）与手动安装三种运行方式，模型侧接入 AWS Bedrock，曾在 CNCF Native Live 演示。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自然语言提示驱动的 Plotly 图表生成 agent
- KubeArmor 策略沙箱化，拦截提示注入导致的恶意执行并输出违规日志
- 提供 K8s / Docker / 手动三种运行方式
- Docker 镜像当前仅支持 amd64，不兼容 ARM 设备

## 适用场景

- 演示提示注入攻击下 agentic AI 的任意代码执行风险
- 为 agentic AI 应用套用 KubeArmor 最小权限沙箱策略
- 学习 Strands Agents SDK 的工具调用型 agent 构建

## 场景标签

`网络安全` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L3: **Agentic AI Strands App** is an experimental graph-based AI application built using the AWS Strands Agents SDK. It 
> L116: Now if the prompt injection attacks leads to malicious execution or unwanted access, they will be prevented and re

## 星数曲线

```mermaid
xychart-beta
    title "accuknox/agentic-ai-strands 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `556a779528ec` · [字段定义](../../DATASET.md)*
