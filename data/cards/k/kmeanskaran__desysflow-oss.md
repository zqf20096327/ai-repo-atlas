# kmeanskaran/desysflow-oss

⭐ 22 · Python · MIT · 推送 2026-04-27 · [GitHub](https://github.com/kmeanskaran/desysflow-oss) · 个人维护

**本地优先的 agentic 系统设计平台，代码库生成版本化架构文档**

DesysFlow OSS 读取代码库与产品目标，通过 LangGraph 多 agent 流水线（需求抽取、架构生成、边界用例注入、批评/修订、图表生成与质检、报告生成、云基础设施 agent）产出版本化架构工件：HLD/LLD、技术报告、非技术简报、Mermaid 图、diff 与元数据，默认写入 ./desysflow/<project>/vN/。提供 CLI、FastAPI 本地后端与 React UI 三种使用方式，支持 ollama/openai/anthropic/groq 四种 LLM 提供商，可经 desysflow.config.yml 配置，含可选的密钥泄露检测 guardrail。需 Python 3.11+、uv 与 Node.js。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 10 节点 LangGraph agent 流水线生成 HLD/LLD/图表/报告等版本化工件
- CLI + 本地 FastAPI 后端 + React UI 三种使用形态
- Provider 可选：ollama/openai/anthropic/groq，含连通性校验
- 可选 LLM_GUARDRAIL 密钥泄露检测（API key/token/连接串模式）

## 适用场景

- 从现有代码库生成高/低层设计与技术文档
- 通过后续提示迭代修订架构设计并保留版本历史
- 为本地 Ollama 模型生成云基础设施图表与报告

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L16: DesysFlow OSS is a local-first, agentic system design platform that converts your codebase and product goals into v
> L28: - Provider-flexible LLM support (`ollama`, `openai`, `anthropic`, `groq`)

## 星数曲线

```mermaid
xychart-beta
    title "kmeanskaran/desysflow-oss 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `bbb915f5a506` · [字段定义](../../DATASET.md)*
