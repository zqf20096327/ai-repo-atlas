# kiran94/bookworm

⭐ 31 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/kiran94/bookworm) · [官网](https://pypi.org/project/bookworm_genai/) · 个人维护

**用自然语言搜索本地浏览器书签的 LLM 命令行工具**

Python CLI 工具，通过 OpenAI 嵌入将本地浏览器书签向量化存入本机向量库，支持自然语言语义搜索（如搜 Japan 命中 Osaka 相关结果）。提供 sync/ask/export 三个子命令：同步各浏览器书签、语义搜索、导出为 CSV 等格式。支持 Linux/macOS 上的 Chrome、Firefox、Brave（不支持 Windows 与 Edge），向量库存储在用户本机。以 PyPI 包分发，需设置 OPENAI_API_KEY。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 嵌入驱动的书签语义搜索
- sync/ask/export 三个子命令，支持导出 CSV
- 向量数据库存储于本机用户数据目录
- 支持 Linux/macOS 上的 Chrome/Firefox/Brave 书签同步

## 适用场景

- 书签量大又记不清位置时用自然语言找网站
- 把多个浏览器的书签统一导出为 CSV
- 定期同步后在终端里直接查询书签

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L5: > LLM-powered bookmark search engine
> L11: *In the example above, we search for the term “Japan.” While some results don’t explicitly mention the word, terms 


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `7fab34f2b43b` · [字段定义](../../DATASET.md)*
