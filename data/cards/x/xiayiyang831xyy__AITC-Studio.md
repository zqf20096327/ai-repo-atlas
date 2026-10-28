# xiayiyang831xyy/AITC-Studio

⭐ 24 · Python · 推送 2026-08-27 · [GitHub](https://github.com/xiayiyang831xyy/AITC-Studio) · 个人维护 · 中文 README

**面向测试工程师的 AI 测试用例生成与管理平台**

AITC 将需求文档到测试用例的流程组织为一条工程链路：需求导入与功能点结构化、项目级混合 RAG（向量+BM25+RRF+可选 Rerank）知识增强、基于 LangGraph 的多 Skill 用例生成（核心/安全/接口专项）、规则质检与 AI Judge 评分、人工评审采纳后入库，并支持测试任务执行与离线评测回归。技术栈为 React+FastAPI+SQLAlchemy+Chroma，模型接口采用 OpenAI-compatible 协议，默认支持 Mock 模式无需 Key 体验。当前版本以本地和中小规模部署为目标（默认 SQLite、单 Worker 锁），生产化需自行引入 PostgreSQL/Redis 等。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LangGraph 状态节点拆分生成流程，支持断点恢复与幂等重试
- skill.yaml+Handler+Prompt+Pydantic Schema 的 Skill 插件体系，专项能力可动态发现
- 向量+BM25+RRF 融合+可选 Rerank 的混合 RAG，引用来源随结果保存
- AgentRun 持久化、Worker 租约心跳、预算控制与事件追踪的运行治理

## 适用场景

- 把 PRD/需求文档批量转化为可评审的测试用例草稿
- 沉淀业务规则与历史缺陷为项目知识库，约束用例生成上下文
- 对 AI 生成用例做规则质检、AI Judge 评分与人工采纳后交付执行
- 固化样本与模型快照，对生成质量做离线评测回归对比

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L3: **从需求文档到可执行测试用例的 AI 测试工程平台**
> L45: AITC 面向测试工程师与测试负责人，解决三个典型问题：
> L54: 需求导入 → FeatureList 确认 → RAG 增强生成 → 规则质检 → AI Judge

## 星数曲线

```mermaid
xychart-beta
    title "xiayiyang831xyy/AITC-Studio 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-28 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `152d1571912b` · [字段定义](../../DATASET.md)*
