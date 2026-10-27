# matheusml/zsh-ai

⭐ 226 · Shell · MIT · 推送 2026-09-30 · [GitHub](https://github.com/matheusml/zsh-ai) · 个人维护

**zsh 插件：输入自然语言注释即时生成 shell 命令**

zsh shell 插件：在提示符输入 `# ` 加自然语言描述，回车后在提示符处获得对应 shell 命令，可编辑后再次回车运行；也支持 `zsh-ai "..."` 直接询问。请求上下文包含目录路径、附近文件名、项目类型、git 状态与操作系统。模型来源可选托管服务商，或经 Ollama 运行本地模型，或在支持的 Mac 上经 Apfel 使用 Apple 端侧模型（免 API key）。通过 Homebrew 安装，需 zsh 5.0+、curl、perl，jq 可选。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- `# ` 触发：自然语言即时生成命令并可编辑后运行
- 请求附带目录、文件、项目类型、git 状态与 OS 上下文
- 支持 Ollama 本地模型与 Apple 端侧模型（Apfel，免 API key）
- 可用 ZSH_AI_PROMPT_EXTEND 自定义命令偏好

## 适用场景

- 不记得命令语法时用自然语言快速生成 shell 命令
- 先审阅再执行生成命令，避免误操作
- 在支持的 Mac 上离线免 API key 生成命令

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L5: Type `# ` and describe a command. Press Enter to get it at your prompt.
> L8: $ # find files larger than 100mb changed this week
> L9: $ find . -type f -size +100M -mtime -7

## 星数曲线

```mermaid
xychart-beta
    title "matheusml/zsh-ai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 224 --> 227
    line [225, 226, 226]
```

2026-10-18 225 → 2026-10-27 226（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `02ec641392e0` · [字段定义](../../DATASET.md)*
