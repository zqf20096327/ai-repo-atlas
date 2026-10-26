# thechandanbhagat/cv-forge

⭐ 30 · TypeScript · MIT · 推送 2025-12-19 · [GitHub](https://github.com/thechandanbhagat/cv-forge) · 个人维护

**生成 ATS 友好求职简历/求职信/邮件模板的 MCP 服务器**

面向 Claude Desktop 等 MCP 客户端的工具服务器，TypeScript 编写，经 npm 全局或本地安装后写入 claude_desktop_config.json 接入。提供 14 个工具：解析职位描述提取技能与联系人信息、按用户画像与职位要求生成定制简历内容，并输出 PDF（默认）/HTML/Markdown/文本多种格式；另含求职信生成、四类邮件模板与一键完整申请包。PDF 页面尺寸、页边距、字号等可通过环境变量配置，服务器以 stdio 方式运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 14 个 MCP 工具覆盖职位解析、简历/求职信/邮件生成
- PDF 默认输出，另支持 HTML/Markdown/文本格式
- 从职位描述自动提取邮箱与招聘经理姓名
- 环境变量配置 PDF 页面尺寸、边距与字体参数

## 适用场景

- 求职者为每个职位定制 ATS 友好的简历与求职信
- 在 Claude Desktop 中用自然语言生成完整申请材料包
- 批量按职位描述生成不同格式的简历文档

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L5: An intelligent MCP (Model Context Protocol) server that analyzes job postings and crafts perfectly-matched CVs.
> L52: To use this MCP server with Claude Desktop, you need to add it to your Claude configuration file.

## 星数曲线

```mermaid
xychart-beta
    title "thechandanbhagat/cv-forge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-26 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `f2cd10a85a20` · [字段定义](../../DATASET.md)*
