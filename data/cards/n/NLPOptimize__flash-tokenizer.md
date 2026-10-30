# NLPOptimize/flash-tokenizer

⭐ 457 · C++ · 推送 2026-02-02 · [GitHub](https://github.com/NLPOptimize/flash-tokenizer) · [官网](https://github.com/NLPOptimize/flash-tokenizer) · 组织维护

**C++17 实现的高速 BertTokenizer 库，面向 LLM 推理服务**

用 C++17 实现的 BertTokenizer 替代库，通过 pybind11 提供 Python 接口，核心机制为 LinMax Tokenizer（线性时间）与 AC 自动机/DFA 的 Trie 结构，并使用 OpenMP 在 C++ 层做批编码并行。README 给出与 Huggingface/PaddleNLP/TensorFlow-text/Blingfire 的百万级文本基准数据，FlashTokenizer 在耗时上领先但部分场景准确率低于基线。支持 Windows/macOS/Ubuntu，提供预编译 whl 与源码编译两种安装方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- C++17 实现，pybind11 提供 Python 接口
- LinMax Tokenizer + AC Trie/DFA 实现线性时间分词
- OpenMP 支持的 C++ 层批编码并行处理
- 各 OS 提供预编译 whl 文件

## 适用场景

- 替换 LLM 推理服务中的 BertTokenizer 以降低 CPU 分词瓶颈
- 大批量文本预分词/预处理流水线
- 需要 vocab.txt 即可运行、避免安装大型框架依赖的场景

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L21: FlashTokenizer is a **high-performance tokenizer implementation in C++ of the BertTokenizer used for LLM inference*
> L48: > - This is why we developed `FlashTokenizer`. It can be easily installed via `pip` and is **developed in C++ for s

## 星数曲线

```mermaid
xychart-beta
    title "NLPOptimize/flash-tokenizer 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-30"]
    y-axis "stars" 456 --> 459
    line [458, 457, 457]
```

2026-10-18 458 → 2026-10-30 457（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `f13b8936f158` · [字段定义](../../DATASET.md)*
