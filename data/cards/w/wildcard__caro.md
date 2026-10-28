# wildcard/caro

⭐ 40 · Rust · AGPL-3.0 · 推送 2026-10-28 · [GitHub](https://github.com/wildcard/caro) · [官网](https://caro.sh/) · 个人维护

**自然语言生成安全 POSIX 命令的 Rust CLI（本地 LLM）**

Rust 单二进制 CLI，将自然语言任务描述转换为 POSIX shell 命令，面向开发者和运维人员。内置嵌入式模型（Apple Silicon MLX / CPU），也支持 Ollama、vLLM、Exo、Mesh-LLM、AI-Horde 等远程后端及本地脱敏+远程增强的 hybrid 模式。命令执行前经过 5 层校验（52+ 危险命令模式、CVE 规则、用户确认等），输出 JSON/YAML/Plain 多格式；支持多 shell 目标、CaroML .caro 任务文件、Claude Code skill 与 OpenAI 兼容 serve 等接入方式。可经 cargo/Homebrew/预编译二进制安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言→shell 命令生成，2 轮 agentic 迭代与平台感知（OS/架构/shell/可用命令）
- 嵌入式本地模型（MLX/CPU）单二进制分发，另有 Ollama/vLLM/Exo 等 6 种后端
- 5 层安全校验：52+ 危险模式、CVE 规则、风险分级确认
- CaroML：.caro 任务文件提交意图、生成多平台 runbook、漂移检测

## 适用场景

- 终端里用自然语言生成 shell 命令并确认执行
- 让 coder agent（如 Claude Code）经 caro 安全生成 shell 命令
- 在 .caro 文件中提交意图并生成跨平台 runbook

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L11: **caro** (formerly **cmdai**) converts natural language descriptions into safe POSIX shell commands using local LLM
> L78: - 🧠 **Local LLM inference** - Embedded models optimized for Apple Silicon (MLX) and CPU

## 星数曲线

```mermaid
xychart-beta
    title "wildcard/caro 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-28 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `5efd9c3ebe3c` · [字段定义](../../DATASET.md)*
