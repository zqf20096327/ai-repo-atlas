# AriesOxO/piz

⭐ 44 · Rust · MIT · 推送 2026-04-12 · [GitHub](https://github.com/AriesOxO/piz) · 个人维护 · 中文 README

**用自然语言生成 Shell 命令的终端 CLI 助手**

Rust 编写的跨平台命令行工具：用户以自然语言描述需求，piz 调用 LLM 生成适配当前系统与 Shell 的命令，经确认后执行；附带命令解释、失败命令自动诊断修复（最多 3 轮重试）、多轮对话、多候选生成、SQLite 缓存与执行历史。支持 OpenAI/Claude/Gemini/Ollama 四类原生后端及 12 个 OpenAI 兼容供应商。安全上提供三层防护：Prompt 层拒绝非命令输入、本地正则注入检测、危险命令分级强制确认。通过 Homebrew、cargo、安装脚本与二进制包分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言转命令，支持多候选生成与缓存加速
- 命令解释与失败命令自动诊断修复（最多 3 轮）
- 三层安全防护：Prompt 拒绝、注入检测正则拦截、危险分级强制确认
- 四类原生 LLM 后端 + 12 个 OpenAI 兼容供应商，Ollama 本地模型无需 API key

## 适用场景

- 记不住具体命令时用自然语言快速得到并执行命令
- 让工具自动解释复杂命令或修复刚失败的命令
- 在脚本中通过 --pipe 模式集成命令生成

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L17: **piz** 解决一个问题：你知道想做什么，但记不住具体命令。用自然语言描述你的需求，piz 自动翻译成适合当前系统和 Shell 的命令。
> L27: - **自然语言转命令** — 描述需求，得到精确命令
> L28: - **多 LLM 后端** — 支持 OpenAI、Claude、Gemini、Ollama + 12 个 OpenAI 兼容供应商（DeepSeek、硅基流动、OpenRouter、Moonshot、智谱GLM、百度千帆、阿里

## 星数曲线

```mermaid
xychart-beta
    title "AriesOxO/piz 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-27 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `90670ac899a4` · [字段定义](../../DATASET.md)*
