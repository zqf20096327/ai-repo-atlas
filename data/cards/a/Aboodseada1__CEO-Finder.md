# Aboodseada1/CEO-Finder

⭐ 14 · Python · MIT · 推送 2026-11-24 · [GitHub](https://github.com/Aboodseada1/CEO-Finder) · 个人维护

**面向销售线索挖掘者的公司高管姓名自动查询 CLI 工具**

命令行工具：输入公司名称或域名，通过自托管 SearXNG 实例执行七个定向搜索查询，取前 15 条结果的标题、URL 与摘要构建提示词，调用所选 LLM 提取单一高管姓名并以 JSON 格式返回（不确定时返回 null）。支持 Gemini、OpenAI、Groq、Ollama 四个提供商与模型覆盖参数。限制：每次仅处理一家公司，无批量与缓存；作者声明结果属线索而非已确认事实。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SearXNG 七查询检索 + LLM 从结果摘要提取姓名
- 支持 Gemini/OpenAI/Groq/Ollama（本地）四个提供商与 fallback 模型列表
- 输出结构化 JSON，无法确定时返回 null

## 适用场景

- 补充 CRM 里缺失的现任高管姓名字段
- 销售线索挖掘前快速查一家公司的 CEO/创始人
- 用本地 Ollama 模型避免数据出本机

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L3: Command-line tool that identifies the CEO, president, founder or owner of a company from public web search results. 
> L20: - LLM providers: Google Gemini, OpenAI, Groq, Ollama (local). Optional model override, with a fallback list per pro


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `325d10838bdb` · [字段定义](../../DATASET.md)*
