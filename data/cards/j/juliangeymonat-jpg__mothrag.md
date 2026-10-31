# juliangeymonat-jpg/mothrag

⭐ 35 · Python · Apache-2.0 · 推送 2026-10-19 · [GitHub](https://github.com/juliangeymonat-jpg/mothrag) · 个人维护

**确定性多跳 RAG 框架：纯商用 API 实现，无 GPU，答案附带证明树**

面向频繁更新语料的多跳问答 Python 框架：在普通稠密索引上做查询时编排（查询分解、四臂集成池、确定性仲裁），更新仅需一次嵌入调用，无图重建与训练。读取器、嵌入器、检索判官均走按次付费 API（默认 Groq Llama-3.3-70B + Gemini），无本地 GPU；输出确定性（同输入同输出）并附带可检查的证明树。提供 pip 安装、CLI 与论文复现配置；论文声称在 HotpotQA 等基准上达到与 GPU 方案相当的 F1。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 查询时多跳编排，更新仅为 embed+append，无需图重建或训练
- 全部组件走商用按次付费 API，无 GPU，实测约 $0.032/query
- 同输入同输出的确定性管道，每个答案附带可检查证明树
- 提供 CLI、离线回退模式（无 key 可端到端运行）与论文复现脚本

## 适用场景

- 在每日更新的语料（赛事、价格、工单、内部文档）上做多跳问答
- 需要可审计、可复现答案证明链的生产级检索问答
- 预算受限、无 GPU 资源下搭建多跳 RAG 系统

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L23: MothRag does the reasoning as **query-time orchestration over a plain dense index**. An update is **embed + append*
> L30: 1. **Freshness — no rebuild.** Updates are embedding-only (`ingest()` embeds the changed
> L89: ```python

## 星数曲线

```mermaid
xychart-beta
    title "juliangeymonat-jpg/mothrag 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 34 --> 37
    line [35, 36, 35]
```

2026-10-18 35 → 2026-10-31 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9767ce2cbb8e` · [字段定义](../../DATASET.md)*
