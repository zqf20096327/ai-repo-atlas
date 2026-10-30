# salvy9978/pls

⭐ 66 · Python · MIT · 推送 2026-03-25 · [GitHub](https://github.com/salvy9978/pls) · [官网](https://pypi.org/project/pls-sh/) · 个人维护

**用自然语言生成终端命令并执行的 CLI 工具**

面向终端用户的 Python 命令行工具：用户用自然语言描述意图，pls 结合 OS、shell 与当前目录上下文发送给 LLM，生成 shell 命令，经确认后执行。默认通过本地 Ollama 离线运行，无需 API key；也支持 LM Studio、llama.cpp、OpenAI 兼容服务器，以及 OpenAI/Anthropic 云端模型。内置危险命令检测（如 rm -rf 高亮警示并改为默认不执行确认），提供 --explain/--dry-run/--yes 标志，配置存于 ~/.config/pls/config.toml，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言转 shell 命令，附带 OS/shell/目录上下文
- 默认 Ollama 本地离线运行，无 API key 与遥测
- 危险命令检测与可编辑确认流程
- 支持 LM Studio/llama.cpp/OpenAI 兼容服务器及 OpenAI/Anthropic

## 适用场景

- 不记得命令语法时用一句话生成并执行终端命令
- 离线环境下用本地模型完成日常 shell 操作
- 让工具解释或预览（dry-run）即将执行的命令

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L104: 1. You type what you want in plain English (or any language, really)
> L106: 3. Sends that + your request to the LLM

## 星数曲线

```mermaid
xychart-beta
    title "salvy9978/pls 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 65 --> 67
    line [66, 66]
```

2026-10-18 66 → 2026-10-30 66（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `6380889035e9` · [字段定义](../../DATASET.md)*
