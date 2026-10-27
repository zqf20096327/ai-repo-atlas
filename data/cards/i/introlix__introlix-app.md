# introlix/introlix-app

⭐ 42 · TypeScript · Apache-2.0 · 推送 2026-06-27 · [GitHub](https://github.com/introlix/introlix-app) · [官网](https://introlix-app.vercel.app) · 组织维护

**面向研究者的多 Agent AI 研究平台：规划、检索与写作**

基于 FastAPI 与 Next.js 的自托管研究平台，通过多 Agent 系统组织研究流程：ContextAgent 提问收集研究范围、PlannerAgent 生成研究计划、ExplorerAgent 经 SearXNG 联网检索、EditAgent 辅助文档编辑，另带流式对话界面。支持 OpenRouter 或 Google AI Studio 作为 LLM 提供方，向量存储用 Chromadb，数据库为 SQLite。提供 Docker Compose 与源码两种运行方式，需自行部署 SearXNG。文件上传等功能标注为 Coming Soon。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 四类专职 Agent（Context/Planner/Explorer/Editor）组成的多阶段研究工作流
- SearXNG 自托管隐私搜索与 Chromadb 向量语义检索
- Lexical 富文本编辑器与 AI 辅助文档编辑
- 支持 OpenRouter / Google AI Studio 双 LLM 提供方切换

## 适用场景

- 组织和执行从选题到成文的深度研究流程
- 通过带联网检索的对话获取实时信息
- 在自托管环境中管理研究项目与文档

## 场景标签

`多智能体` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L30: - **AI-Powered Research Desk**: Multi-stage AI-guided research workflow with context gathering, planning, and explo
> L44: 2. **Context Agent**: AI asks clarifying questions to understand your research scope
> L267: - **LLM Providers**: OpenRouter or Google AI Studio

## 星数曲线

```mermaid
xychart-beta
    title "introlix/introlix-app 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-27 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1cc03e23042d` · [字段定义](../../DATASET.md)*
