# deepanwadhwa/zink

⭐ 112 · Python · Apache-2.0 · 推送 2026-10-10 · [GitHub](https://github.com/deepanwadhwa/zink) · 个人维护

**面向开发者的零样本文本匿名化 Python 库**

Python 包，用零样本 NER 模型（GLiNER 架构的 NuNerZero）识别并匿名化非结构化文本中的敏感实体（准标识符 PII/QI）。提供 redact（替换为 [LABEL]_REDACTED）、replace（用 Faker 生成上下文相关的合成替换）、自定义替换字典、@zink.shield 装饰器（API 调用前匿名化、输出后还原）与持久化实体映射（~/.zink/mapping.json）。支持 pip/uv 安装（cpu/gpu extra，首次导入从 Hugging Face 下载约 2 GB 模型）及 Docker 镜像（内置模型与 REST API）。附 QIB 基准（1750 例、35 类准标识符）评测结果。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 零样本 NER 识别任意实体标签并执行脱敏/替换
- @zink.shield 装饰器在 LLM/API 调用前后自动匿名化与还原
- Faker 结合 GLiNER 训练数据生成上下文相关的合成替换
- Docker 镜像内置模型并暴露 REST /redact 接口

## 适用场景

- RAG 管线或外部 API 调用前对敏感文本脱敏
- 按自定义标签和替换字典做一致性匿名化
- 跨多次调用保持实体映射一致的批处理脱敏

## 场景标签

 · 领域:NLP/隐私工程

## 证据(README 行号)

> L10: ZINK is a Python package designed for zero-shot anonymization of entities within unstructured text data. It allows 
> L162: ### GLiNER
> L163: GLiNER is a Named Entity Recognition (NER) model capable of identifying any entity type using a bidirectional tran

## 星数曲线

```mermaid
xychart-beta
    title "deepanwadhwa/zink 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 111 --> 113
    line [112, 112]
```

2026-10-18 112 → 2026-10-28 112（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `19d52aa57be9` · [字段定义](../../DATASET.md)*
