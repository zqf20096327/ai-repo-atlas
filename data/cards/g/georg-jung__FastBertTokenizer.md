# georg-jung/FastBertTokenizer

⭐ 55 · C# · MIT · 推送 2026-10-21 · [GitHub](https://github.com/georg-jung/FastBertTokenizer) · [官网](https://fastberttokenizer.gjung.com/) · 个人维护

**.NET 平台的 BERT WordPiece 分词库**

面向 .NET 的 C# 分词库，实现 BERT 所用 WordPiece 分词，结果与 HuggingFace AutoTokenizer 在实际场景等效，单核吞吐约 1450 万 tokens/s。支持 Native AOT，目标框架 net10.0/net8.0/netstandard2.0。限制：不支持将两段文本编码为带分隔符与 token_type_ids 的单输入。通过 NuGet 安装，附示例工程与基准测试。

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

- WordPiece 分词，结果与 HuggingFace AutoTokenizer 实际等效
- 单核约 1450 万 tokens/s，批处理约 3530 万 tokens/s（4 vCPU）
- Native AOT 兼容，目标 net10.0/net8.0/netstandard2.0
- 单元测试与基准自动验证正确性与速度

## 适用场景

- 在 .NET 生产环境运行 BERT 类模型的分词环节
- 将 HuggingFace 分词结果迁移到 C# 工作流
- 高吞吐批量文本分词预处理

## 场景标签

 · 领域:NLP/机器学习库

## 证据(README 行号)

> L8: A fast and memory-efficient library for WordPiece tokenization as it is used by BERT. Tokenization correctness and s
> L12: * Enabling you to run your AI workloads on .NET in production.

## 星数曲线

```mermaid
xychart-beta
    title "georg-jung/FastBertTokenizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-24 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `08382ccb27be` · [字段定义](../../DATASET.md)*
