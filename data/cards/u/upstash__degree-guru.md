# upstash/degree-guru

⭐ 220 · TypeScript · 推送 2025-12-12 · [GitHub](https://github.com/upstash/degree-guru) · [官网](https://degreeguru.vercel.app/) · 组织维护

**教你在自有网站数据上构建 RAG 聊天机器人的开源模板**

基于 Vercel AI SDK、LangChain.js、Upstash Vector 与 OpenAI 的 RAG 聊天机器人示例项目：Python/Scrapy 爬虫按 crawler.yaml 配置抓取指定网站，切块、生成向量嵌入并写入 Upstash Vector；Next.js 聊天应用读取向量库生成回答，支持流式与非流式两种模式，并通过 Upstash Redis 按 IP 做速率限制。默认用斯坦福大学学位数据作示例，修改配置即可换成任意领域数据。以源码形式提供，需配置 Upstash 与 OpenAI API key，爬虫可经 docker-compose 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置 Scrapy 爬虫：抓取任意指定网站并自动向量化入库
- 栈为 Next.js + LangChain.js + Upstash Vector + OpenAI（gpt-3.5-turbo / ada-002 嵌入）
- 流式与非流式两种回答模式，非流式模式可显式给出来源 URL
- 基于 IP 的速率限制防止 API 滥用

## 适用场景

- 用自己网站的内容搭一个领域问答机器人
- 学习爬虫、向量数据库与 LLM 协同工作的 RAG 全流程
- 高校或机构为学位/课程信息提供问答入口

## 场景标签

 · 领域:LLM 应用/RAG 模板

## 证据(README 行号)

> L14: **DegreeGuru** is a project designed to teach you making your own AI RAG chatbot on any custom data. Some of our fa
> L20: This chatbot is trained on data from Stanford University as an example, but is totally domain agnostic. We've creat

## 星数曲线

```mermaid
xychart-beta
    title "upstash/degree-guru 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 219 --> 221
    line [220, 220]
```

2026-10-18 220 → 2026-10-24 220（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `b96b75440f50` · [字段定义](../../DATASET.md)*
