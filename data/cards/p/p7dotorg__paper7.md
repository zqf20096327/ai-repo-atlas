# p7dotorg/paper7

⭐ 14 · TypeScript · MIT · 推送 2026-05-22 · [GitHub](https://github.com/p7dotorg/paper7) · [官网](https://github.com/lucianfialho/paper7#install) · 个人维护

**面向 AI agent 的论文检索命令行：arXiv/PubMed/DOI 转 Markdown**

Bash/CLI 研究工具：搜索 arXiv、PubMed，解析 DOI（Crossref），经 ar5iv 抓取全文并转为保留结构的 Markdown，供 LLM/编码 agent 直接读入上下文；支持本地缓存、语义学者元数据层、本地知识库（kb）与引用管理。附带可安装的 agent 技能，教 Claude Code、Cursor、Codex 等如何调用。所有论文输出包裹在 untrusted-content 标签中以隔离提示注入，17 项注入探针测试全部通过。npm 包预构建、零外部工具依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- arXiv/PubMed/DOI 检索并转结构化 Markdown
- 为 Claude Code/Cursor/Codex 提供可安装技能
- 输出以 untrusted-content 标签包裹，含 17 项提示注入探针测试
- npm 包预构建无 install 脚本，运行时依赖仅 effect 系

## 适用场景

- 让编码 agent 在对话中检索并读取论文全文
- 把论文转为精简 Markdown 以节省上下文窗口
- 跨 arXiv/PubMed/预印本做文献调研与引用管理

## 场景标签

`科研工具` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L3:  A research command line for AI agents.
> L20: paper7 ships with an installable skill that teaches AI coding agents (Claude Code, Cursor, Codex) how to use it. On

## 星数曲线

```mermaid
xychart-beta
    title "p7dotorg/paper7 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `1f69e3bd6a1a` · [字段定义](../../DATASET.md)*
