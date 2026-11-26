# sysid/bkmr

⭐ 269 · Rust · BSD-3-Clause · 推送 2026-11-18 · [GitHub](https://github.com/sysid/bkmr) · 个人维护

**本地优先的知识管理 CLI：存书签/片段并供 AI 代理读写记忆**

基于 Rust 与 SQLite 的命令行知识管理工具，统一存储 URL、代码片段、Shell 命令、Markdown、环境变量与本地文件，按内容类型分发动作（打开/复制/执行/渲染）。提供全文检索与混合检索（FTS + 本地 ONNX 语义向量、RRF 融合，离线无 API key）。面向开发者与 AI 代理：JSON 输出、非交互模式，`_mem_` 系统标签与 bkmr-memory 技能构成代理长期记忆的读写接口；内置 LSP 服务器与 Neovim/IntelliJ 插件。支持备份/恢复与历史回滚。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 混合检索：FTS + 本地语义嵌入（离线，无需 API key），带相似度与命中类型标注
- 面向 AI 代理的长期记忆接口：`_mem_` 标签与可安装的 bkmr-memory 技能
- 多种内容类型的上下文感知动作分发（URL/片段/脚本/Markdown/环境变量）
- JSON 输出与备份恢复机制；内置 LSP 服务器及编辑器插件

## 适用场景

- 在本地离线管理书签、代码片段与文档并按语义检索
- 为 Claude 等 AI 代理提供可持久化的项目长期记忆
- 在编辑器内通过 LSP 补全直接调用代码片段
- 脚本流水线中以 JSON 非交互方式批量读写条目

## 场景标签

`Agent 记忆` `知识库管理` `语义搜索` · 领域:Agent 开发

## 证据(README 行号)

> L10: # Beyond Bookmarks and Snippets: Knowledge Management for Humans and Agents
> L26: - **Agent-friendly**: JSON output, non-interactive mode, and `_mem_` system tag for AI agent memory
> L118: |`hsearch`|Hybrid search: FTS + semantic with RRF fusion; `--mode exact`: keywords only; `--mode semantic`: meanin

## 星数曲线

```mermaid
xychart-beta
    title "sysid/bkmr 星数(近 4 点)"
    x-axis ["2026-10-24", "2026-11-08", "2026-11-16", "2026-11-26"]
    y-axis "stars" 266 --> 270
    line [267, 268, 269, 269]
```

2026-10-24 267 → 2026-11-26 269（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `6f2d6d72cd19` · [字段定义](../../DATASET.md)*
