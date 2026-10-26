# com-vitthalmirji/toon4s

⭐ 32 · Scala · MIT · 推送 2026-10-20 · [GitHub](https://github.com/com-vitthalmirji/toon4s) · [官网](https://toonformat.dev) · 个人维护

**TOON 数据格式的 Scala/JVM 实现：面向 LLM 的紧凑序列化**

Token-Oriented Object Notation（TOON）的 Scala 实现库，用于在 JSON 与 TOON 之间编解码。TOON 格式结合 YAML 风格缩进与 CSV 风格表头，供 LLM prompt 使用以减少 token 数量（README 称 30-60%）。面向 Scala/Java 开发者：核心库零依赖，提供 Scala 3 派生的类型化 Encoder/Decoder、纯函数式 Either 错误处理、流式 visitor（常数内存处理百万行）、Strict/Lenient 严格度模式，以及带 token 统计与分隔符优化的 CLI。通过 Maven Central 分发，支持 sbt/Maven/Gradle/Mill 等构建工具。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- JSON↔TOON 编解码，保持 JSON 兼容并减少 token 用量
- Scala 3 派生的类型化 Encoder/Decoder（无 Any）
- 零依赖核心库（<100KB），流式 visitor 常数内存处理大数据
- CLI 提供 --stats token 统计、--optimize 分隔符选择、cl100k/o200k 等 tokenizer 选项

## 适用场景

- 把结构化数据编码成 TOON 放入 LLM prompt 以节省 token
- 校验 LLM 返回的 TOON/JSON 数据（行数校验、Strict 模式）
- 在 Scala/Java 项目中以类型化 API 序列化与反序列化数据
- CI/CD 中用 CLI 统计 token 节省情况

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L11: `toon4s` is the idiomatic Scala implementation
> L13: a compact, LLM-friendly data format that blends YAML-style indentation with CSV-like tabular efficiency.
> L206: ## Using TOON in LLM prompts
> L233: For response validation, decode the model output using `Toon.decode` (if the LLM responds in TOON) or rehydrate JS

## 星数曲线

```mermaid
xychart-beta
    title "com-vitthalmirji/toon4s 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-26 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `e265d7f87b3d` · [字段定义](../../DATASET.md)*
