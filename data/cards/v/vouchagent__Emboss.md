# vouchagent/Emboss

⭐ 24 · Python · Apache-2.0 · 推送 2026-10-18 · [GitHub](https://github.com/vouchagent/Emboss) · [官网](https://vouchagent.github.io/Emboss/) · 组织维护

**面向开发者的声明式 PDF 生成引擎：结构化内容转可访问、可验证 PDF**

纯 Python 的排版与 PDF 生成库：以声明式 spec 或 Markdown 描述文档，内置 Knuth-Plass 断行排版引擎，自动完成 PDF/UA 无障碍标签与完整 PDF 结构。输出确定且跨机器字节一致，可哈希校验并在 CI 中 diff。支持 PDF/A、PDF/X-4、Factur-X/ZUGFeRD 电子发票、PAdES/eIDAS 签名、按节点编辑与 redline 对比。可接收 LLM 生成内容，并提供 MCP server 供 Claude 调用生成、查询、编辑文档。唯一硬依赖为 fonttools，Python 3.10+ 可经 pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 声明式 spec / Markdown 输入，内置 Knuth-Plass 排版引擎，无需浏览器
- 输出字节级确定，可哈希校验、CI 中可 diff
- PDF/UA 无障碍标签默认生成，CI 中以 veraPDF 实测一致性
- 表格/图表可将源 CSV 以元素级附件嵌入 PDF；提供节点级 diff、redline、PAdES 签名与 MCP server

## 适用场景

- 批量生成发票、报告、合规文档并保证每次输出可复现可审计
- 将 LLM 生成内容转为带无障碍标签的印刷级 PDF
- 对两版文档做结构化 diff 与红线标注审阅
- 通过 Claude（MCP）生成、查询与编辑文档

## 场景标签

 · 领域:文档生成/PDF 工具链

## 证据(README 行号)

> L9: **Emboss turns structured or LLM-generated content into accessible, print-ready PDFs** -- describe a document once, 
> L28: 1. **Native typesetting, no browser.** Emboss is a real typesetting engine (Knuth-Plass line breaking, true font me
> L58: |**AI-native distribution**|An MCP server makes every document callable from Claude: generate, query with certainty

## 星数曲线

```mermaid
xychart-beta
    title "vouchagent/Emboss 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `3d433c751614` · [字段定义](../../DATASET.md)*
