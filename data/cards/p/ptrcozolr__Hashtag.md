# ptrcozolr/Hashtag

⭐ 15 · Python · NOASSERTION · 推送 2026-02-25 · [GitHub](https://github.com/ptrcozolr/Hashtag) · 组织维护 · 中文 README

**基于 LLM 的知识库问答平台，支持可视化工作流编排**

Hashtag 是一个由 LLM 驱动的知识库问答系统，提供开箱即用的数据处理、RAG 检索与模型调用能力，并通过 Flow 支持可视化工作流编排以实现复杂问答场景。知识库支持多库复用、混合检索与重排序、多种文件格式导入（txt/md/pdf/docx/csv 等）；应用层支持插件/对话工作流、工具调用、代码沙箱、循环调用；对外提供对齐 GPT 接口的 Completions OpenAPI。技术栈为 NextJS + TS + ChakraUI + MongoDB + PostgreSQL(PG Vector)/Milvus，可通过 Sealos 一键部署或本地开发，另提供免登录分享窗口与 Iframe 嵌入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可视化工作流编排：对话/插件工作流、工具调用、代码沙箱、循环调用
- 知识库支持多库复用、混合检索与重排序、多格式文件导入与 URL 读取
- Completions 接口对齐 GPT 格式，附知识库与对话 CRUD 的 OpenAPI
- 可经 Sealos 一键部署，支持免登录分享与 Iframe 嵌入

## 适用场景

- 搭建基于自有文档的知识库问答系统
- 通过可视化编排构建多步骤复杂问答流程
- 将问答窗口嵌入到自己的网站供访客使用

## 场景标签

`文档问答` `RAG` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L7: Hashtag is a knowledge-based Q&A system powered by a large language model (LLM), offering out-of-the-box data proces
> L79: Project tech stack: NextJs + TS + ChakraUI + MongoDB + PostgreSQL (PG Vector plugin)/Milvus

## 星数曲线

```mermaid
xychart-beta
    title "ptrcozolr/Hashtag 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `247efa950f00` · [字段定义](../../DATASET.md)*
