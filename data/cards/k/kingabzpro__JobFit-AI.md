# kingabzpro/JobFit-AI

⭐ 19 · Jupyter Notebook · Apache-2.0 · 推送 2026-05-04 · [GitHub](https://github.com/kingabzpro/JobFit-AI) · [官网](https://www.datacamp.com/tutorial/kimi-k2-6-api-tutorial) · 个人维护 · 中文 README

**上传 CV 后由 AI agent 搜索并评分匹配职位的 Gradio 应用**

基于 Gradio 的求职匹配应用：读取候选人 CV PDF（pypdf），通过 OpenAI Agents SDK 运行 Kimi 2.6 agent，为其提供 search_jobs 与 read_job_page 两个工具，分别调用 Olostep Search 搜索职位与 Olostep Scrape 抓取职位页，最终生成含最佳匹配、排名列表、职位备注与被拒职位的 Markdown 报告。默认面向 AI、数据科学、技术写作与开发者教育类岗位，可通过偏好框修改。运行需设置 Moonshot 与 Olostep 两个 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取 CV PDF 后由 agent 自动搜索并抓取职位页
- 通过 OpenAI Agents SDK 运行 Kimi 2.6，配备两个工具
- 生成含最佳匹配、排名与被拒职位的 Markdown 报告

## 适用场景

- 上传我的 CV 自动获得职位匹配排名报告
- 面向 AI/数据科学/技术写作类岗位的求职筛选

## 场景标签

 · 领域:求职/招聘工具

## 证据(README 行号)

> L3: JobFit AI is a Gradio app that reads a candidate CV, runs a Kimi 2.6 agent through the OpenAI Agents SDK, searches t
> L11: - Reads a CV PDF with `pypdf`.

## 星数曲线

```mermaid
xychart-beta
    title "kingabzpro/JobFit-AI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `4aa8836f5d8d` · [字段定义](../../DATASET.md)*
