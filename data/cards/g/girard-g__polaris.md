# girard-g/polaris

⭐ 26 · Rust · MIT · 推送 2026-10-06 · [GitHub](https://github.com/girard-g/polaris) · [官网](https://polarismcp.com/) · 个人维护

**给编程 Agent 用的本地 RAG/MCP 语义文档搜索服务器**

单文件 Rust 二进制，为 Claude Code、Cursor、Codex 等 MCP 兼容编程 Agent 提供项目 Markdown 文档的语义检索服务。索引 .md 文件时同时建立向量嵌入（本地 ONNX 模型，CPU 运行）与 FTS5 全文索引，查询时经 RRF 融合、标题加权与 MMR 重排输出 top-k 片段。无 API key、无云端，代码不离开本机；支持 watch 自动重建索引与 token 节省统计。限制：仅索引 Markdown，单用户串行写入，块偏移量为近似值。另提供 Rust 库 polaris-core 与付费扩展 Polaris Pro（开发中）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 混合检索：sqlite-vec 向量 KNN + BM25，RRF 融合后 MMR 重排
- 本地 ONNX 嵌入模型，无 API key、无遥测，代码不出本机
- 通过 MCP（stdio）向编码 Agent 暴露 search/index/status 工具
- watch 模式文件变更约 500ms 内自动重建索引；token 节省统计

## 适用场景

- 让 Claude Code/Cursor 等 Agent 语义检索项目文档，替代 grep 逐文件阅读
- 私有代码仓库的本地文档检索，代码不上传云端
- 文档频繁更新时通过 watch/自动钩子保持索引最新

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L8: **Polaris is a local-first RAG server that gives coding agents fast, ranked answers from your project's documentatio
> L22: - **MCP-native** — exposes `search`, `index`, `status` tools over stdio. Works with Claude Code, Cursor, Codex, and

## 星数曲线

```mermaid
xychart-beta
    title "girard-g/polaris 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-29 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `29f28f203669` · [字段定义](../../DATASET.md)*
