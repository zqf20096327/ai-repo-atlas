# seven0x16/chalklee

⭐ 3 · TypeScript · AGPL-3.0 · 推送 2026-11-25 · [GitHub](https://github.com/seven0x16/chalklee) · [官网](https://www.chalklee.com) · 个人维护 · 中文 README

**给老师用的开源本地题库与备课桌面工具**

把电脑里的 PDF（含扫描件）、Word、LaTeX 和 Markdown 转换成结构化的可编辑文档，题干、选项、答案、解析与知识点分开保存，支持直接编辑排版、跨文档搜题、选题篮组卷与 A4/A3 排版导出。AI 部分包括原稿转换、在卷面上直接改题出题的对话面板、按教材生成知识清单、把出题习惯存为 SKILL.md 技能，以及生成小工具插件；AI 服务由用户自行接入，不绑定某一家模型。数据在本机处理，面向中小学教师。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PDF 扫描件与 Word 转换为按题拆分的可编辑文档，公式与 MathType 转为可编辑公式
- 文件夹即题库：全文搜题、按年级/题型/难度/知识点筛选、选题篮组卷
- AI 改动直接写进卷面，支持相似题生成、题型改写与压缩排版
- 出题习惯可存为通用 SKILL.md 技能，并通过 MCP 供外部 AI 应用调用

## 适用场景

- 把多年积累的扫描试卷变成可编辑可检索的电子题库
- 让 AI 按教材章节和既定出题习惯批量生成练习
- 组卷后按学生版/教师版分别导出 Word 或 PDF
- 让外部 AI 应用通过 MCP 操作本机题库改题组卷

## 场景标签

`文档解析` `知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L3:  开源的本地题库与备课工具 ——把电脑里的 PDF 和 Word 变成可编辑、可搜题、可交给 AI 直接修改的试卷与讲义。
> L84: |**接入模型服务**|原稿转换、ChalkLee AI 对话|DeepSeek、Kimi、智谱、阿里云百炼、火山方舟、MiniMax、硅基流动、OpenRouter、OpenAI、Anthropic、Gemini、Ollama 
> L86: |**在 AI 应用里使用 ChalkLee（MCP）**|原稿转换、改题、组卷等|WorkBuddy、豆包工作、千问办公、Codex，以及 Cursor、Cherry Studio、Trae 等支持 MCP 的应用|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `65cbd6657171` · [字段定义](../../DATASET.md)*
