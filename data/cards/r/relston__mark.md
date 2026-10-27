# relston/mark

⭐ 55 · Python · MIT · 推送 2025-12-26 · [GitHub](https://github.com/relston/mark) · 个人维护

**用 Markdown 与图片直接和 LLM 对话的 Python CLI 工具**

面向开发者的命令行工具：读取 Markdown 文件作为提示词，提取其中的图片引用交由多模态 LLM 做视觉识别，抓取本地/远程链接补充上下文，并将 LLM 回复直接追加写入原 Markdown 文件，从而在文档内延续对话。支持 stdin/stdout 管道、自定义系统提示词、--model 指定模型、--generate-image 生成图片。默认使用 OpenAI API，可通过 OPENAI_API_BASE_URL 指向兼容端点。网页抓取依赖 Playwright 浏览器二进制（约 100MB），安装后需运行一次 mark-setup-browsers。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 回复直接追加写入 Markdown 文件，可在文档内延续对话
- 图片引用经多模态 LLM 做视觉识别
- 本地/远程链接自动抓取为上下文
- 支持 stdin/stdout 管道与图片生成（dall-e-3）

## 适用场景

- 在 Markdown 文档中直接与 LLM 对话并把回复留在文档里
- 让 LLM 识别文档中引用的图片内容
- 通过管道把 LLM 响应接入其他命令行工具

## 场景标签

`网页抓取` `多模态` · 领域:效率与自动化

## 证据(README 行号)

> L5: **Mark lets you seamlessly use markdown, images and links to interact with LLMs**
> L50: By default, `mark` will read a markdown file, extract any context references, and send them to the LLM. The respons

## 星数曲线

```mermaid
xychart-beta
    title "relston/mark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-27 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `1967d9c2bd51` · [字段定义](../../DATASET.md)*
