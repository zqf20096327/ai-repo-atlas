# buyukakyuz/smith

⭐ 16 · Rust · MIT · 推送 2025-12-27 · [GitHub](https://github.com/buyukakyuz/smith) · 个人维护

**终端中的开源 AI 编码 agent，读写文件并执行命令**

Rust 编写的命令行 AI 编码 agent：以当前工作目录为上下文，通过对话调用工具，支持读取/写入文件、glob/grep 搜索、列目录和执行 bash 命令。通过环境变量配置 ANTHROPIC/OPENAI/GEMINI API key，/model 命令切换模型。安装方式为 git clone 后 cargo build 从源码编译。README 标注处于重度开发中，可能有破坏性变更。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 以当前工作目录为上下文的终端 AI 编码 agent
- 工具集：读写文件、glob/grep 搜索、列目录、执行 bash 命令
- 支持通过 /model 选择多个模型，配置 Anthropic/OpenAI/Gemini API key

## 适用场景

- 在终端里让 AI 直接读写项目文件并执行命令
- 多模型切换进行代码任务
- 在项目目录内以对话方式完成编码操作

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: Smith is a fast, open-source AI coding agent that runs in your terminal.
> L42: smith can read files, write files, search with glob and grep, list directories, and execute bash commands.

## 星数曲线

```mermaid
xychart-beta
    title "buyukakyuz/smith 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `600525ff81db` · [字段定义](../../DATASET.md)*
