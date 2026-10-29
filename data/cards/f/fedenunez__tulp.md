# fedenunez/tulp

⭐ 22 · Python · NOASSERTION · 推送 2026-10-22 · [GitHub](https://github.com/fedenunez/tulp) · 个人维护

**命令行 AI 管道工具：用自然语言处理与生成 shell 数据**

受 POSIX 工具启发的终端 CLI：把标准输入内容通过管道交给 LLM，按自然语言指令做过滤、摘要、改写、生成等处理并输出到 stdout，可像 sed/awk/grep 一样串联。支持 OpenAI、Anthropic、DeepSeek、Z.ai、Google Gemini、Groq、Ollama 七类提供商，通过 --model 切换。提供 -x 模式生成并执行 Python 代码（README 提示其风险），超长输入自动分块处理（默认 100 万字符）。以 pip 包安装，需 Python 3.10+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 管道式处理 stdin/stdout，可与 sed/awk/grep 类工具串联
- 支持 OpenAI/Anthropic/DeepSeek/Z.ai/Gemini/Groq/Ollama 七类提供商
- -x 模式生成、调试并执行 Python 代码完成任务
- 超大输入自动分块顺序处理（--max-chars 可配）

## 适用场景

- 在 shell 管道中用自然语言处理 CSV/文本/代码数据
- 不离开终端直接向 LLM 提问或生成代码
- 让 AI 生成 Python 程序对数据做计算并执行

## 场景标签

`数据分析` `代码生成` · 领域:效率与自动化

## 证据(README 行号)

> L3: TULP is a command-line tool inspired by POSIX utilities, designed to help you **process**, **filter**, and **create*
> L5: Pipe standard input content to TULP, provide instructions in natural language, and receive the processed output on s
> L42: 3. **Code Interpretation Mode (`-x`):** TULP attempts to **generate, debug, and execute** a Python program to fulfi

## 星数曲线

```mermaid
xychart-beta
    title "fedenunez/tulp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-29 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `e90f15f10c77` · [字段定义](../../DATASET.md)*
