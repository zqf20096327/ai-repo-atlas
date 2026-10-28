# smadgulkar/spren-ai-terminal-assistant-rust

⭐ 20 · Rust · AGPL-3.0 · 推送 2025-12-25 · [GitHub](https://github.com/smadgulkar/spren-ai-terminal-assistant-rust) · [官网](https://smadgulkar.github.io/spren/) · 个人维护

**本地运行的自然语言转 shell 命令终端助手**

用 Rust 编写的跨平台 CLI 工具，将自然语言请求翻译为 Bash、Zsh、PowerShell 或 CMD 命令，支持命令预览、确认后执行与失败自动修复建议。内置量化为 4-bit 的 Qwen2.5-0.5B 模型，经 2 万余条 shell 命令示例微调，通过 Candle 框架在 CPU 上本地推理，无需 API key 与网络；可选切换 Anthropic/OpenAI/Gemini 云端 API。提供 REPL、TUI 与单次查询三种模式，并对危险命令要求确认。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置 Q4_K_M 量化 Qwen2.5-0.5B 模型，CPU 本地推理无需 API key
- 支持 Bash/Zsh/PowerShell/CMD，覆盖 Linux/macOS/Windows
- 感知当前目录与 git 状态生成上下文相关命令
- 危险命令标记与执行前确认，失败命令自动建议修复

## 适用场景

- 不记得命令语法时用自然语言查询对应 shell 命令
- 在无网络或注重隐私的环境中本地完成命令生成
- 命令报错后获取修复建议

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L117: Spren uses a fine-tuned Qwen2.5-0.5B model, quantized to 4-bit (Q4_K_M) for efficient CPU inference. The model was
> L125: The model runs via Candle, Hugging Face's Rust ML framework.

## 星数曲线

```mermaid
xychart-beta
    title "smadgulkar/spren-ai-terminal-assistant-rust 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `65d14c9a468f` · [字段定义](../../DATASET.md)*
