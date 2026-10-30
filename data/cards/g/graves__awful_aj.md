# graves/awful_aj

⭐ 15 · Rust · CC-BY-SA-4.0 · 推送 2025-12-23 · [GitHub](https://github.com/graves/awful_aj) · [官网](https://awful-aj.awfulsec.com/) · 个人维护

**终端里的 LLM 客户端：问答/REPL/RAG/记忆，纯 Rust**

用 Rust 编写的命令行 LLM 工具，面向 OpenAI 兼容 API（默认示例指向本地 localhost:1234/v1）。提供单次问答（aj ask）、带记忆的交互式 REPL、文档 RAG（512 token 分块、128 重叠、嵌入缓存、top-k 检索）。记忆基于 HNSW 向量库与 all-MiniLM-L6-v2 嵌入，经 Candle 纯 Rust 推理自动从 HuggingFace Hub 下载模型，无 Python 依赖。配置与提示词模板均为 YAML，会话存 SQLite。经 cargo install 安装，许可证为 CC-BY-SA-4.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | CC-BY-SA-4.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- aj ask 单次问答与带记忆的交互式 REPL
- RAG：自动分块、嵌入缓存、top-k 检索注入上下文
- HNSW + all-MiniLM-L6-v2 嵌入（Candle 纯 Rust，自动下载模型）
- YAML 配置与提示词模板，会话存 SQLite

## 适用场景

- 在终端直接向 OpenAI 兼容 API 提问或持续对话
- 把本地文档作为 RAG 上下文做问答
- 用模板管理常用提示词并用会话保留上下文

## 场景标签

`AI 助手` `RAG` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L6: **Awful Jade** (aka **`aj`**) is your command-line sidekick for working with Large Language Models (LLMs).
> L25: - **Ask the AI**: Run `aj ask "question"` and get answers powered by your configured model.
> L27: - **RAG Support**: Load documents for context-aware responses with `--rag` flag. Automatic chunking, caching, and r

## 星数曲线

```mermaid
xychart-beta
    title "graves/awful_aj 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `530041edf446` · [字段定义](../../DATASET.md)*
