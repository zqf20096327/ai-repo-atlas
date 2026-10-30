# bsquang/naotab

⭐ 43 · JavaScript · MIT · 推送 2026-04-11 · [GitHub](https://github.com/bsquang/naotab) · 个人维护 · 中文 README

**把浏览器标签页转为本地个人知识库的 Chrome 扩展**

Chrome 扩展（Manifest V3），将标签页保存为带摘要、理由和标签的书签条目，全部数据存于 chrome.storage.local，无服务端。提供 D3.js 力导向图可视化（节点=书签、边=共享标签）、全文搜索列表视图、SEO meta 提取、整窗口批量保存、Obsidian Markdown 导出与 JSON 备份。AI 功能可选且默认关闭：经 OpenAI/Claude/Groq/Ollama/OpenRouter 等自动生成标签与摘要，无 API key 时回退到离线关键词标签建议。安装方式为开发者模式加载未打包目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 标签页保存附带摘要、理由与标签，全部本地存储
- D3.js 力导向图可视化，节点按共享标签连边
- AI 自动生成标签与摘要（可选、默认关闭），AI 仅读取页面 meta 约省 10 倍 token
- 导出为 Obsidian vault（ZIP 内 .md + YAML frontmatter）与 JSON 备份

## 适用场景

- 把研究/浏览中的网页按标签组织成可检索的第二大脑
- 以网络图查看书签之间的标签关联
- 用 AI 批量为已存书签生成摘要与标签

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L5: A Chrome Extension (Manifest V3) that turns your browser tabs into an organized, searchable **personal knowledge bas
> L16: - **AI integration** (optional, off by default) — auto-suggest tags and summaries via OpenAI, Claude, Groq, Ollama,
> L26: - **100% local** — all data in `chrome.storage.local`, nothing leaves your machine except optional AI API calls

## 星数曲线

```mermaid
xychart-beta
    title "bsquang/naotab 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 41 --> 44
    line [42, 43, 43]
```

2026-10-18 42 → 2026-10-30 43（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e4a0c7711f8c` · [字段定义](../../DATASET.md)*
