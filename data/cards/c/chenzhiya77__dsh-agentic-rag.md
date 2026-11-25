# chenzhiya77/dsh-agentic-rag

⭐ 4 · Python · MIT · 推送 2026-11-06 · [GitHub](https://github.com/chenzhiya77/dsh-agentic-rag) · 个人维护 · 中文 README

**DeepSeek Harness 的本地知识库插件：三路检索与全链路联动**

面向 DeepSeek Harness（DSH）宿主的 Agentic RAG 插件，由宿主工具、浏览器面板、knowledge 服务三块组成。提供文档/表格/视频的解析切分、实体图谱与 wiki 条目生成、向量+图谱+wiki 三路检索、文档感知读回，以及两层检索质量评测（确定性 IR 指标与 RAGAS LLM 评分）。写入时下游对象沿派生关系级联更新，读取时沿来源关系回溯源切片。托管模式自带便携 Python、Qdrant 与引擎，运行时包仅提供 Windows x64；其他平台需走外部服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 向量/图谱/wiki 三路检索与文档感知读回（六件 hrag_* 工具）
- 编辑/重抽/删除沿派生关系向下级联传导
- 两层评测：确定性 IR 指标 + RAGAS LLM 评分报告
- 粘贴厂商截图智能识别并回填模型配置表单

## 适用场景

- 为 DSH 会话挂载本地知识库，让 agent 按检索纪律回答
- 批量解析 PDF/Word/Excel/视频并构建实体图谱与 wiki
- 用题库与趋势图跟踪知识库检索质量

## 场景标签

`RAG` `知识图谱` `模型评测` `文档解析` · 领域:评测与运维

## 证据(README 行号)

> L3: > **DeepSeek Harness（DSH）插件**：一套内置本地知识库——从文档 / 表格 / 视频的解析与切分，到实体图谱、wiki 条目、三路检索、文档感知、知识库管理与检索质量评测；默认自带本地知识服务（便携 Pyth
> L94: - **聊天模型来自 DSH**：宿主侧 OpenAI 兼容代理 + `dsh:<provider>/<model>` 别名，provider 的 endpoint 与 key 留在 DSH；目录变化或插件激活时自动同步。
> L218: - 插件基于 **DeepSeek Harness**（<https://github.com/deepseek-ai/deepseek-harness>，MIT）的插件 API。

## 星数曲线

```mermaid
xychart-beta
    title "chenzhiya77/dsh-agentic-rag 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-10", "2026-11-25"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-08 3 → 2026-11-25 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `2ee6c51e881f` · [字段定义](../../DATASET.md)*
