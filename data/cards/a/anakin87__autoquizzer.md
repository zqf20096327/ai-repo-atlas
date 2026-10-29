# anakin87/autoquizzer

⭐ 72 · Jupyter Notebook · Apache-2.0 · 推送 2026-08-06 · [GitHub](https://github.com/anakin87/autoquizzer) · [官网](https://huggingface.co/spaces/deepset/autoquizzer) · 个人维护

**从 URL 生成测验的 Gradio 应用：人可玩，也可让 LLM 答题**

部署在 Hugging Face Space 上的 Gradio Web 应用：输入 URL 后下载页面 HTML、抽取文本，调用 LLM（openai/gpt-oss-20b，经 Groq API 提供）生成 JSON 格式测验。用户可亲自作答计分，也可让 LLM 以两种方式答题：闭卷（仅凭参数知识）或 Web RAG（每题做 Google 搜索取前 3 条片段）。基于 Haystack 管道构建，需设置 GROQ_API_KEY 与 SERPERDEV_API_KEY。限制：为避免 Groq 免费额度限流，URL 文本截断为 4000 字符。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- URL→文本抽取→LLM 生成 JSON 测验的管道
- 人机两种玩法：用户答题计分或 LLM 闭卷/Web RAG 答题
- Web RAG 管道每题执行 Google 搜索并注入前 3 条片段
- 基于 Haystack 构建，可替换生成器或模型

## 适用场景

- 把任意网页快速变成测验用于学习自测
- 对比 LLM 闭卷与带搜索两种答题方式的表现
- 作为 Haystack 管道与结构化 JSON 生成的参考实现

## 场景标签

`RAG` · 领域:知识与检索

## 证据(README 行号)

> L15: Generates a quiz from a URL. You can play the quiz, or let the LLM play it.
> L28: - **Quiz generation Pipeline**: downloads HTML content from the URL, extracts the text and passes it to the LLM to 

## 星数曲线

```mermaid
xychart-beta
    title "anakin87/autoquizzer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 71 --> 73
    line [72, 72]
```

2026-10-18 72 → 2026-10-29 72（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `625ee8f1db3a` · [字段定义](../../DATASET.md)*
