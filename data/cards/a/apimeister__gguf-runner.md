# apimeister/gguf-runner

⭐ 16 · Rust · MIT · 推送 2026-10-28 · [GitHub](https://github.com/apimeister/gguf-runner) · 个人维护

**本地 GGUF 模型运行器：CPU 推理，终端问答/视觉/转录**

Rust 编写的命令行工具，加载本地 .gguf 模型文件在终端生成回答。基于 mmap 与 CPU-only 推理，不受 GPU/VRAM 限制，上限取决于存储与文件系统缓存。提供 oneshot 单次提示与 REPL 交互两种模式，支持多轮对话、思考输出控制、视觉模型图像输入（含 JSONL 批量处理）以及 Qwen3-ASR 离线音频转录；内置代理层可读写文件与执行白名单 shell 命令。面向希望离线运行模型、在 shell 工作流中脚本化提示的用户。安装方式为 GitHub Releases 预编译二进制或 Cargo 源码编译。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- mmap + CPU-only 推理，不依赖 GPU，可用普通硬件运行不同规模模型
- oneshot / REPL 双模式，REPL 支持多轮对话与 slash 命令
- 内置工具代理层：文件读写、目录操作与白名单沙箱 shell 执行
- 支持视觉模型图像输入（JSONL 批量推理）与 Qwen3-ASR 离线音频转录

## 适用场景

- 在没有 GPU 的机器上离线运行 GGUF 模型并保持数据本地
- 在脚本、cron、CI 等非交互场景中调用模型生成输出
- REPL 会话中让模型借助文件与 shell 工具执行代理任务
- 用视觉模型批量提取图片信息或离线转录音频文件

## 场景标签

`推理引擎` `语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L3: `gguf-runner` is a small command-line tool that lets you run AI models on your own machine.
> L15: Under the hood, `gguf-runner` uses memory mapping (`mmap`) and CPU-only inference.
> L115: `gguf-runner` has two distinct operation modes selected with `--mode`:

## 星数曲线

```mermaid
xychart-beta
    title "apimeister/gguf-runner 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `a6824769ca04` · [字段定义](../../DATASET.md)*
