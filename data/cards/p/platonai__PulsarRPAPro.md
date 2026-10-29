# platonai/PulsarRPAPro

⭐ 142 · Kotlin · AGPL-3.0 · 推送 2026-06-08 · [GitHub](https://github.com/platonai/PulsarRPAPro) · [官网](https://platon.ai) · 组织维护 · 中文 README

**AI 驱动的浏览器自动化与网页数据抽取工具**

基于机器学习代理与 LLM 的浏览器自动化/网页采集方案：提供无监督 ML 的 AutoExtract 自动抽取（无 token 消耗）、自然语言指令驱动的浏览器操作（ai/command API）、LLM+X-SQL 精确抽取，以及 Web UI 与 CLI。支持协程级并发爬取、JavaScript 动态页解析、结构化数据 API、代理轮换。以可执行 JAR 或 Docker 镜像分发，需 Java 运行环境，依赖 MongoDB（27017 端口无认证），LLM 能力需配置 API key（如 DeepSeek）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无监督 ML 自动抽取，无需编码且无 token 消耗
- 自然语言指令驱动浏览器操作与数据抽取（ai/command API）
- LLM+X-SQL 精确字段级抽取（llm_extract）
- 提供 Web UI、CLI 与 Docker 镜像三种使用方式

## 适用场景

- 电商列表页批量自动抽取结构化商品数据
- 用自然语言指令自动化浏览器操作并提取信息
- 需要代理轮换的大规模网页采集任务

## 场景标签

`浏览器自动化` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L13:  * 🤖 Powered by machine learning agents — no token cost!
> L23: * 🤖 **AI Integration with LLMs** — Smarter automation driven by large language models
> L39: 👽 Extract data with machine learning agents:

## 星数曲线

```mermaid
xychart-beta
    title "platonai/PulsarRPAPro 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 141 --> 143
    line [142, 142]
```

2026-10-18 142 → 2026-10-29 142（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `128589fba40c` · [字段定义](../../DATASET.md)*
