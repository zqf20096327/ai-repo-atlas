# Abyss-c0re/deepshell

⭐ 38 · Python · GPL-3.0 · 推送 2026-03-16 · [GitHub](https://github.com/Abyss-c0re/deepshell) · 个人维护

**自托管终端 AI 助手：自然语言驱动 Linux Shell 与文件分析**

基于 Ollama 的终端 AI 助手，面向在 Linux 命令行工作的用户：支持自然语言指令翻译为 shell 命令并执行（--shell 模式）、文件与文件夹分析、代码片段提取、日志与配置解读，响应以 markup 流式输出；可用 ! 前缀直接执行命令、管道传入内容。安装方式为 pip 装依赖后 ./deepshell --install，或使用内置 Ollama 的 Docker 镜像（支持 CPU/NVIDIA/ROCm），模型可通过卷持久化；另有 Neovim 插件。README 标注需先完成配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言翻译并执行 shell 命令，输出 markup 流式分析
- 文件/文件夹/代码/日志分析与异步大文件处理
- Docker 自包含部署（CPU/NVIDIA GPU/AMD ROCm 变体），模型卷持久化
- 管道输入、! 前缀直接执行命令、Neovim 插件等接入方式

## 适用场景

- 在终端用自然语言执行 shell 命令并解读输出
- 让 AI 分析本地代码库、文件与日志
- 通过 Docker 自托管一个不依赖外部服务的终端 AI 助手

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L16: - **Interactive Shell Mode** – Speak in natural language, and the AI will initiate the shell, interpreting commands
> L67: - `--shell` - Speak your intent in natural language. The AI will translate your command, summon the shell, execute 
> L99: DeepShell may be bound within a Docker vessel, self-contained and portable, with Ollama as its inner oracle.

## 星数曲线

```mermaid
xychart-beta
    title "Abyss-c0re/deepshell 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-31 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `77a8f7a1ff60` · [字段定义](../../DATASET.md)*
