# GGBond121211/CodeInsight

⭐ 95 · Python · MIT · 推送 2026-10-01 · [GitHub](https://github.com/GGBond121211/CodeInsight) · 个人维护 · 中文 README

**面向本地代码仓库的中英文问答与代码理解工具**

基于 Hybrid RAG 与 LangGraph 的本地代码仓库问答工具：用 FastAPI 后端、React 前端与 CLI 提供服务。流程为问题拆解（最多 8 个子问题）→ Dense/Sparse 双路召回（Qdrant Named Vectors）→ RRF 融合 → 阿里云 qwen3.7-text-rerank 精排 → 带文件路径与行号的回答，引用由后端映射、模型只能引用证据编号。另支持统一对话（聊天/澄清/范围引导）、带审批与 Docker Sandbox 隔离校验的代码修改链路。运行需 Python 3.12+/uv/Node 22 与 OpenAI 兼容的模型接口，本地依赖通过 Docker Compose 管理。

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

- 问题拆解+Dense/Sparse 双路召回+RRF 融合+模型精排的 Hybrid RAG 流水线
- 回答带文件路径与行号引用，引用由后端映射而非模型生成
- 代码修改链路含预览、审批、隔离 workspace 与 pytest Sandbox 校验
- 提供 CLI、FastAPI 接口、React 页面与 OTel/Prometheus 观测

## 适用场景

- 接手陌生代码仓库时用中英文提问快速定位实现
- 要求回答给出源码文件与行号证据、可核查
- 在带审批与隔离校验的流程里让模型生成代码修改补丁

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L5: CodeInsight 用来回答陌生代码仓库里的具体问题。你可以用中文、英文或中英混合提问，它会先拆解问题，再去源码里找证据，最后给出带文件路径和行号的回答。
> L10: 用户问题 → QueryPlan → 代码检索 → 独立证据 → 回答生成 → 文件与行号引用
> L115: - 提供 `auto-answer` CLI、FastAPI 和 React Conversation 页面；同一 Session 可交错普通聊天、代码理解和修改，`clarify` 不会强行进入代码检索。

## 星数曲线

```mermaid
xychart-beta
    title "GGBond121211/CodeInsight 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 94 --> 96
    line [95, 95]
```

2026-10-18 95 → 2026-10-24 95（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `64bb42fac01a` · [字段定义](../../DATASET.md)*
