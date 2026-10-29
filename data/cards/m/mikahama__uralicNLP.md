# mikahama/uralicNLP

⭐ 101 · Python · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/mikahama/uralicNLP) · [官网](http://uralicnlp.com/) · 个人维护

**面向乌拉尔语系及多语的形态学 NLP Python 库**

Python 库，为芬兰语、斯科尔特萨米语、莫克沙语等乌拉尔语系语言及英语、俄语、阿拉伯语等提供词形还原、形态分析与生成、语素切分、词典查译、CoNLL-U 解析、机器翻译与分词等功能。形态工具基于 FST（有限状态转换器）与约束语法，模型经命令行按语言下载。另提供 GUI、Java/C#/JS 官方版本，支持通过 MCP 接入 LLM，并可用 LLM 做文本嵌入与语义聚类。约束语法功能需另装 VISL CG-3。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 词形还原、形态分析与生成、语素切分，覆盖 50+ 语言（含多条少数民族语言）
- FST 与约束语法（CG）驱动的形态工具，词典与翻译查询
- 支持 MCP 接入 LLM，并可用 LLM 做文本嵌入与语义聚类
- 提供 CoNLL-U 解析、分词、机器翻译等附加功能

## 适用场景

- 对芬兰语、萨米语等乌拉尔语言做形态分析与词形还原
- 通过词典功能查少数民族语言的词翻译
- 解析和检索 UD CoNLL-U 树库数据
- 把乌拉尔语言 NLP 能力通过 MCP 接入 LLM

## 场景标签

 · 领域:自然语言处理/计算语言学

## 证据(README 行号)

> L6: UralicNLP can produce **morphological analyses**, **generate morphological forms**, **lemmatize words** and **give l
> L40: UralicNLP supports a wide range of LLMs and it can even embed text in some endangered languages Check out LLMs.

## 星数曲线

```mermaid
xychart-beta
    title "mikahama/uralicNLP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 100 --> 102
    line [101, 101]
```

2026-10-18 101 → 2026-10-29 101（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `6e0b6e4fb4be` · [字段定义](../../DATASET.md)*
