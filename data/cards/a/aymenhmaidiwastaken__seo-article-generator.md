# aymenhmaidiwastaken/seo-article-generator

⭐ 15 · Python · MIT · 推送 2026-03-25 · [GitHub](https://github.com/aymenhmaidiwastaken/seo-article-generator) · 个人维护

**本地 AI 驱动的 SEO 文章采集与改写工具**

Python 编写的 SEO 内容生成流水线：从 DuckDuckGo、Bing、Google、Reddit、Quora 5 个搜索引擎按关键词抓取文章，用 trafilatura 抽取正文并去重过滤，再通过本地 Ollama 模型（如 llama3、mistral）改写为带 SEO 标题、meta 描述、slug 与分类的文章，输出格式化的 Excel 文件或博客 JS 对象。支持检查点断点续跑、多关键词批量并行处理。面向需要在自有机器上批量生成 SEO 内容、不依赖外部 API key 的用户；使用前需自行安装并运行 Ollama。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 个搜索引擎并发抓取，每关键词 25 种查询变体并自动去重
- 通过本地 Ollama 改写文章，生成 SEO 标题/meta/slug/分类
- 检查点系统支持暂停与 --resume 续跑
- 批量并行处理多组关键词，输出带格式与统计的 Excel

## 适用场景

- 按关键词批量采集并改写出 SEO 优化文章
- 夜间跑批量任务生成大量内容并导出 Excel
- 将生成文章转为静态站点/CMS 可用的博客格式

## 场景标签

`网页抓取` `AI 写作` · 领域:效率与自动化

## 证据(README 行号)

> L32: Rewrites every article using a local LLM through Ollama. Each article gets:
> L5:  Crawl thousands of articles from 5 search engines, extract clean content, and rewrite them into unique SEO-optimize

## 星数曲线

```mermaid
xychart-beta
    title "aymenhmaidiwastaken/seo-article-generator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c34d36f1de37` · [字段定义](../../DATASET.md)*
