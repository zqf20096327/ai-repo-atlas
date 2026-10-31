# romkravets/autoTestScreen

⭐ 17 · JavaScript · 推送 2026-06-24 · [GitHub](https://github.com/romkravets/autoTestScreen) · 个人维护

**面向 vseosvita.ua 教师的 AI 试题生成与自动填站工具**

面向乌克兰教育站点 vseosvita.ua 的 Node.js 命令行与 Web UI 工具：输入主题或来源（URL/PDF/DOCX），调用 LLM（默认 Claude，可选 Groq、OpenRouter、Ollama、LM Studio 等）生成 single/multiple/text 三类题目（约 50/30/20 比例），并通过 Playwright 自动登录站点、填入测试构造器。提供仅生成 JSON、生成+填站、从 JSON 填站三种模式，会话保存于本地文件，约 25 天后提示重登。设计为本地运行，Playwright 约需 1GB 内存。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从主题或 URL/PDF/DOCX 来源生成三类题型并输出 JSON
- Playwright 自动完成 vseosvita.ua 登录与测试构造器填写
- 支持 Claude/Groq/OpenRouter/Ollama/LM Studio 等多种模型提供方
- 提供 Web UI（生成、编辑题目、导入 JSON、会话状态显示）

## 适用场景

- 教师按主题快速生成测验题并自动填入 vseosvita.ua
- 从讲义 PDF/DOCX 或网页生成配套测试
- 本地用 Ollama/LM Studio 免 API key 生成题目

## 场景标签

`浏览器自动化` `AI 写作` · 领域:效率与自动化

## 证据(README 行号)

> L3: Автоматична генерація тестів для vseosvita.ua через AI + Playwright.
> L151: |`-m, --model`|generate, create|Провайдер та модель|`claude`|
> L163: |Anthropic Claude|`claude`|платно|`ANTHROPIC_API_KEY`|

## 星数曲线

```mermaid
xychart-beta
    title "romkravets/autoTestScreen 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 16 --> 19
    line [18, 17, 17]
```

2026-10-18 18 → 2026-10-31 17（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `22728cbe5634` · [字段定义](../../DATASET.md)*
