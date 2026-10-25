# itsmostafa/qi

⭐ 44 · Go · MIT · 推送 2026-09-23 · [GitHub](https://github.com/itsmostafa/qi) · 个人维护

**本地混合检索 CLI：为 AI agent 与人类提供低 token 消耗的查询引擎**

用 Go 编写的命令行查询引擎：将目录或集合索引进单个 SQLite 文件（FTS5 全文 + 可选向量嵌入），提供 BM25、混合 RRF 融合两种检索模式，输出带 SHA-256 哈希、source_uri 与行号范围的检索结果供引用。面向希望把检索工作从 Agent 上下文中卸载、节省 token 的开发者和 agent 用户。完全本地离线运行，向量搜索为可选增强，未配置 provider 时 BM25 开箱即用。限制：get 读取索引快照而非实时文件，重索引前不反映修改。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- BM25（SQLite FTS5）+ 可选向量搜索的混合检索，RRF 融合排序
- 单一 SQLite 文件存储，内容寻址（SHA-256）自动去重
- 检索结果携带 hash/source_uri/行号范围，支持按片段精确引用
- 以 Claude Code 插件形式提供，可配合 Ollama/LM Studio/llama.cpp/OpenAI 嵌入

## 适用场景

- 给编码 agent 挂一个本地知识检索后端，省 token 并获得可引用出处
- 在离线环境对本地文档库做全文与语义混合搜索
- 按内容哈希与行号精确取回索引过的源文档片段

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L9: Save tokens by delegating some of your AI Agent's work to qi. Agent skills included.
> L15: - 🧩 Works with Ollama, LM Studio, Claude, OpenAI, MLX, etc.

## 星数曲线

```mermaid
xychart-beta
    title "itsmostafa/qi 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-25 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `89abe5f9967f` · [字段定义](../../DATASET.md)*
