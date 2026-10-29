# wang-h/autosh

⭐ 21 · Python · 推送 2026-04-29 · [GitHub](https://github.com/wang-h/autosh) · [官网](https://wang-h.github.io/autosh/) · 个人维护 · 中文 README

**给中文程序员的终端 AI 助手：一句中文生成 shell 命令**

AutoSH（命令 ah）是集成到 zsh/bash 的终端工具：读取当前命令行缓冲区中的中文描述，发送给 AI API（DeepSeek/Kimi/MiniMax/Qwen/GLM 任选其一），将生成的 shell 命令替换回命令行。提供两种模式：Ctrl+G 直接出命令，Ctrl+/ 弹出三个候选并附中文解释。不上传命令历史，带本地常驻进程（daemon）与 doctor 环境检查。需要 Python 3.11+ 与任一提供商 API Key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取命令行缓冲区→AI 生成→替换回命令行，不上传命令历史
- 两种模式：Ctrl+G 极速直出 / Ctrl+/ 三个候选+中文解释
- 支持 5 个 AI 提供商一键切换（deepseek/kimi/minimax/qwen/glm）
- zsh 与 bash 双支持，快捷键可自定义

## 适用场景

- 忘记命令语法时用中文描述直接得到可执行命令
- 英文不熟时用中文操作 docker 等命令行工具
- 在不离开终端的情况下快速获得命令候选与解释

## 场景标签

`AI 助手` `代码生成` · 领域:编码与开发

## 证据(README 行号)

> L16: AutoSH（`ah`）是给中文程序员的终端 AI 助手。在 zsh 里写中文，按一下就出命令。
> L138: 读取当前命令行缓冲区 → 发送给 AI API → 模型生成命令 → 替换回命令行。不上传命令历史。

## 星数曲线

```mermaid
xychart-beta
    title "wang-h/autosh 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `44bfd3de6990` · [字段定义](../../DATASET.md)*
