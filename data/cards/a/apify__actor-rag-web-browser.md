# apify/actor-rag-web-browser

⭐ 81 · TypeScript · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/apify/actor-rag-web-browser) · [官网](https://apify.com/apify/rag-web-browser) · 组织维护

**为 LLM/RAG 管道抓取网页并输出 Markdown 的 Apify Actor**

Apify 平台上的 Actor 单仓，包含两个组件：RAG Web Browser 接受搜索查询或 URL 列表，执行网络搜索或加载指定 URL，返回清洗后的 Markdown 文本；URL to Markdown 将网页转换为干净的 Markdown 内容。产物用于向 LLM 应用与 RAG 管道供给实时的网页文本。详细文档位于 actors/ 子目录下各自的 README 中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 接受搜索查询或 URL 列表，抓取网页内容
- 输出清洗后的 Markdown 文本
- 单体仓库含两个 Actor：RAG Web Browser 与 URL to Markdown

## 适用场景

- 为 RAG 管道供给最新的网页文本内容
- 把指定 URL 的网页转成 Markdown 喂给 LLM 应用
- 在 Apify 平台运行作为数据抓取节点

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L5: - **RAG Web Browser** — Web browser for RAG pipelines that accepts a search query or URL list, searches the web or l
> L6: - **URL to Markdown** — Converts web pages to clean Markdown content.

## 星数曲线

```mermaid
xychart-beta
    title "apify/actor-rag-web-browser 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 80 --> 82
    line [81, 81]
```

2026-10-18 81 → 2026-10-28 81（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ed8d308047cd` · [字段定义](../../DATASET.md)*
