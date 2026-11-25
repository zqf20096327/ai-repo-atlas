# xr843/fojin

⭐ 362 · Python · Apache-2.0 · 推送 2026-11-24 · [GitHub](https://github.com/xr843/fojin) · [官网](https://fojin.app) · 个人维护 · 中文 README

**面向佛典研究者的可溯源 AI 问答与跨语种文本平台**

聚合 660+ 数据源、10,500+ 佛教文本的平台，核心是以 RAG 驱动的问答助手 XiaoJin：基于 670K+ 嵌入段落检索，支持重排序与跨语种引用抽屉，答案带可点击的【经·卷】引文回链。配套机制包括引用白名单与逐字校验降级等防幻觉守卫、fojin.ai 的逐句经文核查、开放 /api/verify/quote 端点，以及暴露 8 个只读工具的 fojin-mcp 服务器。安装依赖 git clone 加 docker compose，首启需另行导入语料数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- RAG 问答 XiaoJin：670K+ 段落检索、可点击引文回链、防幻觉守卫
- 三语跨藏对照阅读（CBETA × SuttaCentral × 84000），LLM 校验的块级对齐
- 开放 /api/verify/quote 端点与 fojin.ai 逐句经文核查
- fojin-mcp 服务器提供 8 个只读工具，托管的 mcp.fojin.ai 无需密钥

## 适用场景

- 用自然语言向佛典提问并获得带出处引文的回答
- 粘贴一段网络流传的'佛陀说…'逐句核查是否出自汉译藏经
- 跨汉/巴利/藏三语对照研读同一经文段落
- 让 Claude 等助手通过 MCP 直接调用 FoJin 的引文语料

## 场景标签

`RAG` `文档问答` `科研工具` · 领域:知识与检索

## 证据(README 行号)

> L7: Ask a question in plain language and FoJin's assistant **"XiaoJin"** answers from the canon itself — Retrieval-Augme
> L29: **FoJin answers the question for you.** Ask in plain language; XiaoJin retrieves the relevant passages from 660+ so

## 星数曲线

```mermaid
xychart-beta
    title "xr843/fojin 星数(近 12 点)"
    x-axis ["2026-10-23", "2026-10-26", "2026-10-27", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-12", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-22", "2026-11-25"]
    y-axis "stars" 351 --> 363
    line [352, 353, 354, 355, 352, 359, 360, 361, 360, 361, 362, 362]
```

2026-10-23 352 → 2026-11-25 362（+10）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 mid · 依据 README sha `ccb2f6386165` · [字段定义](../../DATASET.md)*
