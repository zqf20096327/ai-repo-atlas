# aymara/lima

⭐ 119 · C++ · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/aymara/lima) · [官网](http://aymara.github.io/lima/) · 组织维护

**多语言 NLP 分析工具包：分词、词性标注、实体关系抽取**

CEA LIST 实验室开发的 C++ 自然语言处理工具包，MIT 许可。基于 libtorch 的神经模块提供 60 余种语言的分词、词性标注、词法特征、词还原与依存句法分析；另含 ModEx 规则机制，可在无标注数据领域抽取实体、关系与事件。面向 NLP 开发者与科研用户，支持 pip 安装 Python 包（Linux x86_64、Python≥3.7），也提供 Docker 镜像与源码编译两种途径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- libtorch 神经模块覆盖 60 余种语言的分词/词性/词还原/依存分析
- ModEx 规则机制在无标注数据领域抽取实体、关系与事件
- Python 包可 pip 安装，另提供 Docker 与源码编译

## 适用场景

- 对多语言文本做词性标注与依存句法分析
- 在缺乏标注数据的领域用规则抽取实体与关系
- 在 Linux 上以 Python 调用进行 NLP 流水线处理

## 场景标签

 · 领域:自然语言处理

## 证据(README 行号)

> L9: LIMA is a multilingual natural language processing analyzer developed by
> L13: - **Neural modules** (libtorch) for tokenization, part-of-speech tagging and

## 星数曲线

```mermaid
xychart-beta
    title "aymara/lima 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 118 --> 120
    line [119, 119]
```

2026-10-18 119 → 2026-10-27 119（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `2838ae086be9` · [字段定义](../../DATASET.md)*
