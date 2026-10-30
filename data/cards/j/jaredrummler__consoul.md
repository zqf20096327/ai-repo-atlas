# jaredrummler/consoul

⭐ 16 · Python · Apache-2.0 · 推送 2026-01-07 · [GitHub](https://github.com/jaredrummler/consoul) · [官网](https://consoul.goatbytes.io) · 个人维护

**终端里的 AI 助手：TUI/CLI/SDK 三种方式与多模型对话**

基于 Textual 与 LangChain 构建的终端 AI 聊天界面，提供 TUI 交互界面、一次性提问的 CLI 命令（支持管道输入）与可嵌入 Python 应用的 SDK。支持 Anthropic Claude、OpenAI、Google Gemini 及 Ollama、LlamaCpp 本地模型。工具能力包括 AI 文件编辑、语义代码搜索、图片分析、Bash 命令执行（带审批流程）与网页搜索。配置采用 ~/.consoul/config.yaml 多 profile 机制，工具执行设有四级权限策略与 JSONL 审计日志。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TUI/CLI/SDK 三种使用形态，CLI 支持管道输入
- 支持 Anthropic/OpenAI/Gemini 云端模型与 Ollama/LlamaCpp 本地模型
- AI 工具集：文件编辑、代码搜索、图片分析、Bash 执行、网页搜索
- 四级权限策略与 JSONL 审计日志控制工具执行

## 适用场景

- 在终端里与多个云端或本地模型对话
- 用管道把 git diff 等输出交给 AI 生成提交信息
- 通过 SDK 在自己的 Python 程序中嵌入 AI 能力

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5: **AI-Powered Terminal Assistant** — Beautiful TUI · Powerful CLI · Flexible SDK
> L7: Bring modern AI assistance directly to your terminal. Chat with Claude, GPT-4, Gemini, and local models using a rich
> L50: print(console.chat("What is 2+2?"))

## 星数曲线

```mermaid
xychart-beta
    title "jaredrummler/consoul 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `18dc3bada176` · [字段定义](../../DATASET.md)*
