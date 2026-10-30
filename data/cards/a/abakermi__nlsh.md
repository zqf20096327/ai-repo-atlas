# abakermi/nlsh

⭐ 18 · Go · MIT · 推送 2026-02-02 · [GitHub](https://github.com/abakermi/nlsh) · 个人维护

**把自然语言指令转换为 shell 命令并执行的 CLI 工具**

用 Go 编写的命令行工具：用户以自然语言描述操作意图，nlsh 调用 LLM 生成对应的 shell 命令并执行，支持 OpenAI GPT 与 Google Gemini 两种后端，也可通过 base_url 接入 Ollama/vLLM 等本地 OpenAI 兼容模型。提供交互式与单命令两种模式，内置危险命令确认、允许/拒绝清单与模式过滤等安全机制，通过 ~/.nlshrc（TOML）配置。安装方式含 curl 脚本、go install 与源码手动安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言转 shell 命令并执行
- 支持 OpenAI GPT 与 Google Gemini 双后端
- 可通过 base_url 接入 Ollama/vLLM 等本地 OpenAI 兼容模型
- 危险命令确认、允许/拒绝清单与模式过滤等安全检查

## 适用场景

- 不熟悉 shell 语法时用自然语言完成文件等操作
- 交互式会话中反复以自然语言驱动命令行
- 配合本地模型离线使用命令生成能力

## 场景标签

`代码生成` `AI 助手` · 领域:编码与开发

## 证据(README 行号)

> L7: A command-line tool that converts natural language instructions into shell commands using AI. Simply describe what y
> L12: - 🤖 Multiple AI backends: OpenAI GPT and Google Gemini

## 星数曲线

```mermaid
xychart-beta
    title "abakermi/nlsh 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `4e4ac7ae5a6b` · [字段定义](../../DATASET.md)*
