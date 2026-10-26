# zhengbrody/multimodal-rag-system

⭐ 41 · Python · MIT · 推送 2026-07-12 · [GitHub](https://github.com/zhengbrody/multimodal-rag-system) · 个人维护

**带 agent 循环的多模态 RAG 个人问答系统（文本+CLIP 图像检索）**

面向个人网站访客的自然语言问答系统：访客提问后，agent 决策层执行路由（文本/图像/混合/免检索）→检索→证据评分→改写重试（≤3 次）→生成→对来源核验→受限重生成，每次请求返回完整决策 trace。检索层为双模态：个人文本知识库与 CLIP 图像库（OpenCLIP ViT-H/14 + Qdrant，Flickr30k 协议下 Recall@5 为 0.942）。提供 FastAPI 服务、Streamlit 前端与公开在线 demo，附带 199 个测试、Prometheus 指标与 40 例评测报告；提供手写与 LangGraph 两个经测试验证等价的编排器。README 同时列出 agent 相对基线的输赢项（如延迟约 6 倍、LLM 调用约 5.7 倍）。

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

- agent 循环：路由→检索→评分→改写→生成→核验，带预算上限与回退机制
- OpenCLIP ViT-H/14 + Qdrant 图像检索，Flickr30k 5,000-caption 协议 Recall@5=0.942
- 手写与 LangGraph 两个编排器，13 个测试断言输出一致
- 5 层抗幻觉策略与 40 例双裁判（LLM 裁判+机械 grounding）评测

## 适用场景

- 为个人网站部署可溯源、会拒绝未知问题的问答服务
- 按图/文字查询图像库（caption→图、反向以图搜图）
- 对照手写 agent 循环与 LangGraph 实现做工程选型参考

## 场景标签

`RAG` `多模态` · 领域:知识与检索

## 证据(README 行号)

> L28: A personal-website Q&A system that grew, eval-first, into an **agentic multimodal RAG**.
> L34: - **Agent decision layer** (`POST /agent/ask`) — a budget-guarded loop that decides *how* to

## 星数曲线

```mermaid
xychart-beta
    title "zhengbrody/multimodal-rag-system 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-26 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4c2c5e0891bb` · [字段定义](../../DATASET.md)*
