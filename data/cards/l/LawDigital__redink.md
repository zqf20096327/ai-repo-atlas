# LawDigital/redink

⭐ 102 · Visual Basic .NET · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/LawDigital/redink) · [官网](https://vischer.com/redink) · 组织维护

**Windows Office 加载项：在 Word/Excel/Outlook 内接入自选 LLM API**

Red Ink 是运行于 Windows 版 Microsoft Office 的加载项（Word/Excel/Outlook），用户可自行配置任意数量的 LLM API 提供商或自托管 LLM，在文档、表格与邮件中直接获得翻译、改写、摘要、批注、Excel 公式生成、邮件回复建议、PDF 提取与批注修订、会议转写、Mini-RAG 文本数据库检索、批量化合同/条款审查、按内容自动套用样式与重命名文件等功能。另含浏览器扩展、本地聊天机器人与 web agent。分为 GA 与 Preview 两个版本；私有使用免费，商业使用收费。多数功能依赖所配置模型的能力，部分需高级模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 可自由配置任意数量的 LLM 提供商，也支持自托管 LLM
- 在 Word/Excel/Outlook 内完成生成、摘要、翻译、批注与修订标记（Outlook 中以变通方式支持标记）
- Mini-RAG 文本数据库、可自定义脚本的批量合同审查与审查报告
- 发送给 AI 前按名单自动匿名化并在结果中回填明文，含提示注入防护措施

## 适用场景

- 在 Word 里直接让 AI 起草、修订、批注合同并追踪对方改动
- 在 Excel 中让 AI 生成公式、批量填充单元格或分析大型数据表
- 一键摘要邮件链并生成建议回复，无需切换到浏览器
- 批量审查文档目录中的特定条款并输出 Excel 结果表

## 场景标签

`AI 助手` `AI 写作` `语音识别` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L1: Red Ink is an add-in for Microsoft Office on Windows that allows you to access your preferred large language models 
> L17: * You can access any number of language models (they are easy to configure), including language models with reasoni
> L45: Unlike many other products, Red Ink allows you to freely choose the AI provider you want to work with. This approac

## 星数曲线

```mermaid
xychart-beta
    title "LawDigital/redink 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 101 --> 103
    line [102, 102]
```

2026-10-18 102 → 2026-10-30 102（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `fe645d2ef696` · [字段定义](../../DATASET.md)*
