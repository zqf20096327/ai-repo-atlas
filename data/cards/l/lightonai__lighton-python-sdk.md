# lightonai/lighton-python-sdk

⭐ 15 · Python · Apache-2.0 · 推送 2026-10-05 · [GitHub](https://github.com/lightonai/lighton-python-sdk) · [官网](https://lighton.ai) · 组织维护

**LightOn 检索/RAG 平台的官方 Python SDK**

封装 LightOn API（欧洲 LightOn 公司的检索基础设施）的 Python 客户端：开发者配置 API key 后，可通过 ingest/ingest_many 上传文档入索引，用 ask 做基于检索的单轮 RAG 问答（支持流式 SSE、pydantic/JSON-Schema 结构化输出、自定义回答模型），用 search 做混合语义+词法检索，用 parse 将 PDF/Office/图片转为逐页 Markdown，用 extract 按模式抽取结构化字段。含工作区管理、文件生命周期、外部元数据合并等。代码库由 AI 辅助实现，维护方声明设计与 QA 由人工把关。

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

- ask/search/parse/extract 四个主要动作，检索限定在已索引的工作区
- 默认 1000 请求/分钟的客户端限速与 429 自动冷却
- 批量和异步两种执行模式，可轮询任务进度
- search 支持内容类型/属性过滤与 scope 参数从问题自动推导过滤条件

## 适用场景

- 在自有软件中集成文档问答与检索
- 批量上传合同、报告等文档建立可查询索引
- 把 PDF/Office 文档即时转为 Markdown 供其他工具使用
- 按自定义 schema 从文档抽取结构化数据

## 场景标签

`RAG` `文档解析` `语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L14: This SDK wraps the LightOn API. Create an account and get an API key on console.lighton.ai 🚀
> L93: Four actions live directly on the client. `ask` and `search` query your **indexed**

## 星数曲线

```mermaid
xychart-beta
    title "lightonai/lighton-python-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `913ffb3d0c29` · [字段定义](../../DATASET.md)*
