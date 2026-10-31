# JunjoSick/bookforge

⭐ 16 · Rust · MIT · 推送 2026-10-29 · [GitHub](https://github.com/JunjoSick/bookforge) · 个人维护

**保留 EPUB 结构的 AI 整本书翻译工具，附浏览器界面**

用 Rust 编写的 EPUB 翻译引擎：将 EPUB 解析为经验证的 JSON 段落交给 LLM 翻译，模型不接触原始 XHTML；标记、脚注、链接与文档结构由确定性代码重组并通过 EPUBCheck 校验。面向开发者与非技术用户双路径：CLI 与本地浏览器面板（上传 EPUB、选语言/模型、估成本、审校、重试）。支持 OpenAI 兼容 API、DeepSeek/OpenRouter 预设及 Ollama/llama.cpp 本地模型；含 SQLite 断点续跑、双语输出、可选 LLM QA、TTS 有声书生成与 PDF 转 EPUB（需 poppler）。macOS/Linux/Windows 提供预构建安装器，也可 cargo 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 模型只收纯文本 JSON 段落，EPUB 结构由确定性 Rust 代码解析与重组
- SQLite 断点存储，支持暂停/停止/恢复/重试与段级缓存复用
- 本地浏览器面板：上传 EPUB→选语言与模型→估成本→翻译→审校→校验，密钥不落盘
- 可恢复的有声书生成（托管与本地 TTS），含章节切分与 .m4b 组装

## 适用场景

- 把整本 EPUB 电子书翻译成目标语言且保留原始排版结构
- 翻译中途断点续跑、失败段落单独重试
- 非开发者通过浏览器界面对书籍做翻译、审校与校验
- 将 PDF 论文转为可翻译的 EPUB 后再进行翻译

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L3: BookForge is the EPUB translation engine that keeps the LLM away from your document structure. It parses EPUBs into 
> L33: - OpenAI-compatible provider

## 星数曲线

```mermaid
xychart-beta
    title "JunjoSick/bookforge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `394117197445` · [字段定义](../../DATASET.md)*
