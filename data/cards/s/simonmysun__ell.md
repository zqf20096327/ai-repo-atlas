# simonmysun/ell

⭐ 430 · Shell · MIT · 推送 2026-09-26 · [GitHub](https://github.com/simonmysun/ell) · 个人维护

**Bash 编写的 LLM 命令行客户端，在终端提问与对话**

以纯 Bash 实现的 LLM 命令行界面：用户在终端向 LLM 提问、对话，支持管道输入、以文件或 stdin 作为提示词，以及记录终端输入输出作为上下文提问。通过后端机制适配不同 LLM API 风格，OpenAI 与 Gemini 开箱可用，可自行扩展；函数调用等能力经模板实现，另提供插件与脚本扩展点，并对敏感信息做脱敏。要求 bash-4.1+、curl 等基础工具；Windows 需在 Git Bash/MSYS2/Cygwin/WSL 下运行，Git Bash 下部分安全检查与录制功能受限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 终端内 LLM 问答、管道输入与交互式对话
- 录制终端输入输出作为提问上下文（record 模式）
- OpenAI 与 Gemini 后端开箱可用，可自定义 API 风格后端
- 模板与插件机制扩展功能（含函数调用）

## 适用场景

- 在终端直接向 LLM 提问或对话
- 把命令输出或代码文件通过管道发给 LLM 解析
- 录制终端操作后让 LLM 解释报错并给出修复建议

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3: A command-line interface for LLMs written in Bash.
> L191: A backend adapts ell to an LLM API "style" (selected with `--api-style` /

## 星数曲线

```mermaid
xychart-beta
    title "simonmysun/ell 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 429 --> 431
    line [430, 430]
```

2026-10-18 430 → 2026-10-30 430（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `f867e19704b1` · [字段定义](../../DATASET.md)*
