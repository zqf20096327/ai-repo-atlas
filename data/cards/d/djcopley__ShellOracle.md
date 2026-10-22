# djcopley/ShellOracle

⭐ 354 · Python · GPL-3.0 · 推送 2026-09-13 · [GitHub](https://github.com/djcopley/ShellOracle) · 个人维护

**终端 AI 工具：从自然语言描述生成 shell 命令**

ShellOracle 是面向命令行用户的 shell 命令生成工具，以 BASH/ZSH/fish 快捷键（CTRL+F）唤起，输入描述后生成命令并自动插入提示符；也支持管道方式与其他命令串联。可接入 Ollama、llmman、OpenAI、Deepseek、LocalAI、LM Studio、XAI、Google 等多种云端或本地模型提供方，通过 ~/.shelloracle/config.toml 配置，支持自托管。macOS/Linux 上运行，pipx 安装，GPLv3 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从文字描述生成 shell 命令并自动插入 shell 提示符
- 支持 Ollama/llmman/LocalAI/LM Studio 等本地运行时及 OpenAI/Deepseek/XAI/Google 云端提供方
- BASH/ZSH/fish 小组件形式，CTRL+F 唤起，支持 Unix 管道与命令历史

## 适用场景

- 在终端里用自然语言快速生成想要的 shell 命令
- 接入本地 Ollama 或云端 API 自托管生成命令
- 通过管道把任务描述传给 shor 获取命令

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L7: ShellOracle is an innovative terminal utility designed for intelligent shell command generation, bringing a new leve
> L20: * Seamless shell command generation from written descriptions
> L57: The generated command will be inserted into your shell prompt after a brief processing period.

## 星数曲线

```mermaid
xychart-beta
    title "djcopley/ShellOracle 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 353 --> 355
    line [354, 354]
```

2026-10-18 354 → 2026-10-22 354（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `7662ac94d90a` · [字段定义](../../DATASET.md)*
