# kamathhrishi/finance-agent

⭐ 145 · Python · MIT · 推送 2026-06-19 · [GitHub](https://github.com/kamathhrishi/finance-agent) · [官网](https://www.stratalens.ai) · 个人维护

**面向公众公司 SEC 文件的问答研究平台**

基于单个研究 agent 的股票研究平台：不使用分块与向量库，agent 通过 ls/read_file/grep/glob 四个文件系统工具直接读取本地预清洗的 SEC markdown 语料（300+ 美国科技公司、10-K/10-Q/8-K 三年历史），可选 Tavily news_search 工具。语料经 datamule 从 EDGAR 拉取并转换为 markdown，进程内 watcher 每 30 分钟轮询新申报。运行需 Python 3.11+、ripgrep、PostgreSQL、OpenAI API key，前端用 npm 构建，FastAPI 提供服务，默认部署平台为 Railway。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无向量库的文件系统工具型研究 agent（ls/read_file/grep/glob）
- SEC EDGAR 自动摄取：datamule 下载、HTML→markdown 清洗、30 分钟轮询 watcher
- 300+ 美国科技公司 10-K/10-Q/8-K 三年语料，支持 S3 快照冷启动
- FastAPI 服务 + Swagger/ReDoc 文档 + Logfire 观测

## 适用场景

- 就某公司财报/公告提问并得到带引用的回答
- 自建本地 SEC 文件研究语料并自动跟进新申报
- 浏览与检索上市公司的 10-K/10-Q/8-K 文件

## 场景标签

`文档问答` `科研工具` · 领域:知识与检索

## 证据(README 行号)

> L3: Equity-research platform that answers questions about public-company SEC filings (10-K · 10-Q · 8-K). Built around a
> L27: So the rebuild deleted the vector DB, the chunk store, the rerank step, the question-classifier, and the iterative 

## 星数曲线

```mermaid
xychart-beta
    title "kamathhrishi/finance-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 144 --> 146
    line [145, 145]
```

2026-10-18 145 → 2026-10-29 145（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `743e0defa018` · [字段定义](../../DATASET.md)*
