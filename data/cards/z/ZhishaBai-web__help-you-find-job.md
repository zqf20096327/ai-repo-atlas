# ZhishaBai-web/help-you-find-job

⭐ 61 · Python · Apache-2.0 · 推送 2026-10-03 · [GitHub](https://github.com/ZhishaBai-web/help-you-find-job) · [官网](https://app-you-find-job-sszicd3jn6vphnuuhtm84a.streamlit.app/) · 个人维护 · 中文 README

**面向中国求职者的 AI 求职助手：画像—规划—采集—匹配—分析全流程**

基于 Python、Streamlit、LangChain、DrissionPage 的 AI 求职助手系统，覆盖五个子系统：上传 PDF 简历经 LLM 生成结构化用户画像与职场报告、职业规划对话问答、招聘平台岗位自动化采集、基于 RAG 检索与 LLM 的五维人岗匹配评分（能力/职责/发展/背景/潜力），以及 Pandas/Seaborn 数据可视化。用户自配 LLM 与 Embedding 的 API Key/URL。爬虫功能需本地浏览器，其余功能提供线上 demo，无需本地部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 简历+偏好问答 → LLM 生成 JSON 画像、职场报告与岗位检索词
- DrissionPage 自动化采集招聘平台岗位（单线程以降低封禁风险）
- RAG 模式先向量检索 Top50 岗位再 LLM 五维评分
- 分析结果输出 JSON/Excel，含单岗位与全岗位可视化分析

## 适用场景

- 上传简历让 AI 生成职业画像并给出职业规划建议
- 自动采集招聘岗位并按个人画像打分排序
- 对匹配结果做可视化分析与求职决策参考

## 场景标签

`网页抓取` `RAG` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L209: 针对上述问题，本项目设计并开发了一套基于大语言模型（Large Language Model，LLM）的 AI 求职助手系统，通过 LLM 的语义理解与推理能力，实现从 “用户画像—职业规划—岗位采集—人岗匹配—数据分析” 的一
> L213: 本项目主要利用 Python、Streamlit、LangChain、DrissionPage、Pandas、Seaborn 等技术，构建一个集用户画像、职业规划、岗位采集、智能匹配与数据可视化于一体的 AI 求职助手系统。
> L220: 4. **人岗智能匹配评分系统**：利用 LLM 对用户画像与岗位数据进行语义层面的深度匹配，并从能力、职责、发展、背景及潜力五个维度进行综合评分；

## 星数曲线

```mermaid
xychart-beta
    title "ZhishaBai-web/help-you-find-job 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26", "2026-10-28"]
    y-axis "stars" 58 --> 62
    line [59, 60, 61, 61]
```

2026-10-18 59 → 2026-10-28 61（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b8d7a7bdfee9` · [字段定义](../../DATASET.md)*
