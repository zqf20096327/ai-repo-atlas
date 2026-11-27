# BramVanroy/spacy_conll

⭐ 81 · Python · BSD-2-Clause · 推送 2026-11-26 · [GitHub](https://github.com/BramVanroy/spacy_conll) · [官网](https://bramvanroy.github.io/spacy_conll/) · 个人维护

**spaCy 管道组件：解析结果与 CoNLL-U 格式互转**

spacy-conll 是一个 spaCy 管道组件，将已解析文档格式化为 CoNLL-U，也把 CoNLL-U 读入 spaCy Doc 对象，并提供命令行工具 parse-as-conll。它配合 spaCy 模型运行，可选 spacy-udpipe 作为后端以输出 Universal Dependencies 标签；spacy-stanza 已不再支持。通过 pip 安装，需要 Python 3.11 及以上和一个 spaCy 模型。适用于需要在 CoNLL-U 格式与 spaCy 之间转换数据的 NLP 开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-2-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将解析结果格式化为 CoNLL-U，并读取 CoNLL-U 到 spaCy Doc
- 命令行工具 parse-as-conll 直接输出 CoNLL-U
- 可选 UDPipe 后端输出 Universal Dependencies 标签
- 提供 pandas 集成（extra 选项）

## 适用场景

- 把 spaCy 解析结果导出为 CoNLL-U 供树库工具使用
- 将 CoNLL-U 标注数据加载到 spaCy Doc 处理
- 命令行批量解析文本并输出 CoNLL-U 格式

## 场景标签

 · 领域:自然语言处理/文本解析

## 证据(README 行号)

> L8: spacy-conll is a spaCy pipeline component that formats parsed documents as CoNLL-U. It also reads CoNLL-U into spaCy
> L15: pip install spacy-conll


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `0d8efc907f3c` · [字段定义](../../DATASET.md)*
