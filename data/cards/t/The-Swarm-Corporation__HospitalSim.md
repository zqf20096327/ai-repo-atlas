# The-Swarm-Corporation/HospitalSim

⭐ 33 · Python · MIT · 推送 2026-01-19 · [GitHub](https://github.com/The-Swarm-Corporation/HospitalSim) · [官网](https://swarms.ai/simulations) · 组织维护

**多智能体医院管理与模拟系统：模拟患者就诊全流程**

基于多智能体协作的医院管理与模拟 Python 库：包含 CEO/CFO/CMO 决策智能体、专科医生、分诊护士与前台接待等角色智能体，覆盖挂号、分诊、问诊、治疗到记录的多步就诊流程；支持基于症状与生命体征的动态分诊评分、优先级队列与等待时间估算，并集成 ChromaDB 提供 RAG 式病历检索、相似病例匹配与患者历史数据访问，另含吞吐量/满意度/财务分析等运营指标。通过 pip 安装，使用需配合 dotenv 加载环境变量（API key 等）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CEO/CFO/CMO、医生、护士、前台等多类智能体协作
- Reception→Triage→Consultation→Treatment→Documentation 多步流程模拟
- ChromaDB RAG 病历检索与 AI 相似病例匹配
- 患者吞吐量、等待时间、满意度与财务分析指标

## 适用场景

- 模拟医院运营流程并分析吞吐量与等待时间
- 测试多智能体协作在医疗分诊场景的行为
- 基于历史病历检索做诊断支持模拟

## 场景标签

`多智能体` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L11: HospitalSim is a sophisticated multi-agent hospital management and simulation system designed to optimize healthcar
> L49: |**ChromaDB Integration**|Advanced RAG (Retrieval-Augmented Generation) system for medical records|

## 星数曲线

```mermaid
xychart-beta
    title "The-Swarm-Corporation/HospitalSim 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-29 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `948aba840c6e` · [字段定义](../../DATASET.md)*
