# namin/holey

⭐ 39 · Python · MIT · 推送 2026-03-05 · [GitHub](https://github.com/namin/holey) · 个人维护

**结合 SMT 与 LLM 的 Python 程序合成与符号执行库**

Python 库，通过重载执行把带 "洞" 的 Python 代码翻译为 SMTLIB 约束，交给 Z3/CVC5 求解器填充；符号求解失败时可回退到 LLM（Claude/Gemini/Ollama 等）生成或外推启发。面向解决 Python Programming Puzzles 基准（1,506 题中符号执行单独解决 42%）。需克隆源码并 pip 可编辑安装，系统需装 z3 或 cvc5，LLM 为可选通道（需各自 API key），README 标注需帮助完善符号执行器与 LLM 启发式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 重载 __bool__ 的穷举式符号执行，生成 SMTLIB 交给 Z3/CVC5
- 支持自然语言/LLM 回退启发，多 LLM 提供方并行生成成功矩阵
- 对 Python Programming Puzzles 基准的符号执行单独解决率 42%（638/1506）
- 提供 puzzle_solver.py 基准主程序与 pytest 测试

## 适用场景

- 在 Python 代码中留 "洞" 并用形式约束或自然语言规格自动填充
- 求解满足给定 sat 谓词的字符串/整数/列表谜题
- 研究符号执行与 LLM 启发结合的程序合成方法

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: A Python library for program synthesis and symbolic execution that combines SMT (Z3, CVC5, ...) constraint solving w
> L9: The solver incorporates heuristics from LLMs in addition to symbolic execution.

## 星数曲线

```mermaid
xychart-beta
    title "namin/holey 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-30 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `a5f1d940186f` · [字段定义](../../DATASET.md)*
