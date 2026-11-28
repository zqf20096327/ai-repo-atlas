# OleksandrChekhovskyi/hax

⭐ 1,011 · C · MIT · 推送 2026-11-26 · [GitHub](https://github.com/OleksandrChekhovskyi/hax) · [官网](https://usehax.dev) · 个人维护

**给终端开发者的极简 C 语言编码 Agent CLI**

用 C 编写的终端编码 Agent，单个原生二进制，占用数 MB 内存。提供流式 Markdown 输出、工具调用展示、可检查的对话记录视图（Ctrl+T）与 wire protocol 追踪；支持 REPL、单次 `-p` 模式、stdin 输入，并可通过 Python CLI 伴随工具扩展 web 搜索与 MCP 工具。明确不做插件运行时、IDE 面板与逐命令权限确认，面向在终端中运行本地模型、需审计工具行为或打包发行版的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 C 二进制，依赖少，秒级启动
- llama.cpp/Ollama 本地模型自动发现，无需 provider 配置
- OpenAI/Anthropic/OpenRouter/DeepSeek 等多 provider 接入
- transcript 视图与 wire protocol 追踪可审计模型交互

## 适用场景

- 在终端里用本地模型执行编码任务
- 在资源受限环境运行编码 Agent
- 审计发送给模型的内容与回复
- 为发行版打包一个静态二进制的编码工具

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: **A minimalist, terminal-native coding agent written in C.**
> L20: - **Broad provider support** — OpenAI (+compatible), Anthropic (+compatible), Codex (via a ChatGPT
> L27: Developers who live in the terminal, run local models, audit what their tools do, package

## 星数曲线

```mermaid
xychart-beta
    title "OleksandrChekhovskyi/hax 星数(近 22 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-22", "2026-11-25", "2026-11-26", "2026-11-28"]
    y-axis "stars" 929 --> 1018
    line [937, 938, 940, 950, 951, 952, 961, 965, 936, 978, 981, 984, 991, 996, 997, 1001, 1003, 1005, 1006, 1008, 1011, 1011]
```

2026-10-26 937 → 2026-11-28 1,011（+74）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `cc4f7f314005` · [字段定义](../../DATASET.md)*
