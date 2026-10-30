# amitpuri/agentic-healthcare-ai

⭐ 16 · Python · MIT · 推送 2026-06-04 · [GitHub](https://github.com/amitpuri/agentic-healthcare-ai) · 个人维护

**面向医护的多智能体医疗评估演示系统（FHIR+React）**

演示型解决方案：基于 CrewAI 与 Microsoft Autogen 两套框架构建专科化医疗 AI 智能体（全科、心内、临床药师、护理协调、急诊分诊），通过 FHIR R4 API 读取患者数据，产出综合评估、急诊分诊与用药重整等结果，并以 React + Material-UI 提供带框架切换的对话控制台。安全层面声明 HIPAA 合规设计与 SMART on FHIR 认证。整体以 Docker Compose 完整栈交付（含 Postgres/Redis/ELK/Prometheus/Grafana），运行需 OpenAI API key 与 FHIR 服务器；README 顶部标注 'AI Generated'，本仓库标题亦称 Demo solution。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CrewAI 与 Autogen 双框架实现可切换的多智能体医疗评估
- 5 类专科智能体角色：全科/心内/药师/护理/急诊
- FHIR R4 数据集成与 SMART on FHIR 认证、HIPAA 合规设计
- Docker Compose 全栈交付，含监控（Prometheus/Grafana）与日志（ELK）

## 适用场景

- 医疗机构演示多智能体协作的患者综合评估流程
- 结合 FHIR 服务器试用急诊分诊与用药重整工作流
- 作为 CrewAI/Autogen 医疗场景集成的参考实现

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L7: 1. **CrewAI Healthcare Agents** - Collaborative AI agents using the CrewAI framework
> L8: 2. **Autogen Healthcare Agents** - Multi-agent conversational AI using Microsoft's Autogen framework
> L11: The system implements specialized medical AI agents that work together to provide comprehensive patient care, clini

## 星数曲线

```mermaid
xychart-beta
    title "amitpuri/agentic-healthcare-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `a041549c5fdb` · [字段定义](../../DATASET.md)*
