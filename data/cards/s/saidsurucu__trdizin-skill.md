# saidsurucu/trdizin-skill

⭐ 40 · Python · MIT · 推送 2026-06-27 · [GitHub](https://github.com/saidsurucu/trdizin-skill) · 个人维护

**TR Dizin 学术检索 agent 技能：自然语言查土耳其学术文献**

面向 Claude Code、Codex 等 AI agent 的技能包，封装 TR Dizin（土耳其国家学术索引）的开放 JSON API：支持按关键词与多过滤条件的论文检索、按字段（标题/摘要/ORCID/DOI 等）与 AND/OR/NOT 的高级检索、期刊/作者/机构三类实体检索，以及开放获取论文的 PDF 转文本。结果以 JSON 返回并保留原始标识（DOI、ID）。无需浏览器、登录或 API key；非 MCP 服务器，由 agent 直接执行脚本。限定个人使用，API 无文档且可能随时变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 关键词/字段级高级检索（AND/OR/NOT）与 facet 过滤
- 期刊、作者、机构三类实体检索，作者结果附引文数
- 开放获取论文的 PDF 转文本
- 无浏览器/登录/API key，页面内容视为不可信数据

## 适用场景

- 让 Claude Code 或 Codex 等 agent 用自然语言检索土耳其学术文献
- 提取开放获取论文的全文文本
- 按机构、作者或 ORCID 追踪土耳其学术出版物

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L4: için bir **AI agent skill**'i (Claude Code, Codex ve benzeri). TR Dizin'in
> L13: > Bu skill bir sunucu/MCP değildir. Agent, gerekli işi senin için arka planda

## 星数曲线

```mermaid
xychart-beta
    title "saidsurucu/trdizin-skill 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 38 --> 41
    line [39, 40, 40]
```

2026-10-18 39 → 2026-10-31 40（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6286b5b06e0c` · [字段定义](../../DATASET.md)*
