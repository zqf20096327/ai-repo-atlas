# Taiizor/Locale

⭐ 14 · C# · MIT · 推送 2026-10-01 · [GitHub](https://github.com/Taiizor/Locale) · [官网](https://www.vegalya.com) · 个人维护

**面向 .NET 的多格式本地化库与 CLI：扫描、校验、转换并自动翻译**

以 NuGet 库与 CLI（npm / dotnet tool）两种形式提供的本地化工具：支持 JSON、YAML、RESX、PO、XLIFF、SRT、VTT、CSV、i18next、Fluent、VB 共 11 种格式的读取与互转；提供跨文化扫描缺失/孤立键、占位符一致性校验（带 CI 退出码）、骨架文件生成与文件监视。自动翻译接入 11 个提供方，包括 Google/DeepL/Bing 等传统服务与 OpenAI/Claude/Gemini/Ollama 等 AI 模型，支持并行度与限速延迟参数。面向 .NET 开发者与本地化流程自动化场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 11 种本地化格式互转（含 SRT/VTT 字幕与 RESX）
- 6 条可配置校验规则，输出 CI/CD 退出码
- 11 个翻译提供方（含 Ollama 本地模型与 Google 免密钥通道）
- 非英语基础语言（--base）与并行翻译（--parallel/--delay）支持

## 适用场景

- 在 CI 中校验多语言资源文件的缺失键与占位符一致性
- 批量转换 JSON/YAML/RESX 等本地化格式
- 接入 AI 或免费翻译服务批量生成目标语言文件

## 场景标签

 · 领域:软件开发/本地化工具

## 证据(README 行号)

> L3:  Multi-format localization library and CLI tool for .NET
> L31: |🌐 **Translate**|Auto-translate using 11 providers including AI (ChatGPT, Claude, Gemini, Nvidia)|
> L191: |🧠 **Claude**|✅ Yes|`claude-sonnet-4-6`|Nuanced translations|

## 星数曲线

```mermaid
xychart-beta
    title "Taiizor/Locale 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `bb60692377e1` · [字段定义](../../DATASET.md)*
