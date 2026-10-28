# hangyav/textLSP

⭐ 91 · Python · GPL-3.0 · 推送 2026-05-01 · [GitHub](https://github.com/hangyav/textLSP) · 个人维护

**文本拼写与语法检查的语言服务器（LSP），可接本地/远程 AI**

基于 LSP 协议的文本校对语言服务器，对 latex、org、markdown 及纯文本提供拼写/语法诊断与修复建议。分析器分为本地与远程两类：本地支持 LanguageTool 与 Ollama（可运行 Llama 3、Gemma、Mistral 等模型）；远程支持 OpenAI 及兼容 API（需注册付费，自行承担费用）。支持代码动作、按需段落分析、基于上下文的文本生成与补全，可配置编辑器接入，支持 TCP/SSH 远程运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- LSP 诊断与修复建议，支持 latex/org/markdown/纯文本
- 本地分析器：Ollama（多种 LLM）与 LanguageTool
- OpenAI 及兼容 API 远程分析器，文件内魔法命令触发文本生成
- 可通过 TCP 接口或 SSH 在服务器上运行

## 适用场景

- 在编辑器中获得 latex/org/markdown 文档的拼写与语法检查
- 用本地 Ollama 模型做离线文本校对
- 在算力服务器上运行校对服务，编辑器远程连接

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: Language server for text spell and grammar check with various AI tools.
> L40: - Ollama: Run LLMs efficiently on your local machine.
> L89: - OpenAI: Supports text correction as well as text

## 星数曲线

```mermaid
xychart-beta
    title "hangyav/textLSP 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-28"]
    y-axis "stars" 89 --> 92
    line [90, 91, 91]
```

2026-10-18 90 → 2026-10-28 91（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `78f2a6a3eebc` · [字段定义](../../DATASET.md)*
