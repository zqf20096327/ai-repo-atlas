# enzoemir1/autoflow-n8n-workflows

⭐ 10 · MIT · 推送 2026-08-20 · [GitHub](https://github.com/enzoemir1/autoflow-n8n-workflows) · 组织维护

**面向 n8n 用户的 8 个免费 AI 自动化工作流模板合集**

提供 8 个可直接导入 n8n 运行的 AI 自动化工作流模板，覆盖内容多平台分发、冷邮件撰写、客服聊天机器人、邮件分类、Reddit 趋势监测、客户入驻、URL 数据抽取与通话记录日志。每个工作流附成本估算、输入输出说明与 docs/ 文档指南和 examples/ 示例输出。依赖 n8n（Cloud 或自托管）与 OpenAI API（gpt-4o-mini），Google Sheets 作为通用存储，Gmail 用于部分流程。本仓库为 Lite 免费版，完整版在商业网站上提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 个 n8n 工作流模板，git clone 后导入即可运行
- 多数流程标注单次运行成本估算（约 $0.002–0.03）
- 每个工作流提供 docs/ 安装指南与 examples/ 示例输出 JSON
- 聊天机器人流程无需向量数据库，通过环境变量配置公司信息

## 适用场景

- 把一篇博客自动改写成 Twitter/LinkedIn/Instagram/Facebook 四平台内容
- 对 Gmail 收件箱按紧急/重要/信息/垃圾自动分类并记录
- 从 Reddit 热帖中识别趋势并获得内容选题建议
- 接收 Vapi/Bland 通话 webhook 并将通话记录写入表格

## 场景标签

`工作流自动化` `聊天机器人` · 领域:效率与自动化

## 证据(README 行号)

> L9:  8 free, production-ready n8n workflow templates for AI automation.
> L61: Send a blog post via webhook → AI generates optimized content for **Twitter thread + LinkedIn post + Instagram capt
> L76: Polls Gmail every 5 minutes, classifies each new email into: **urgent, important, informational, or spam**. Logs to

## 星数曲线

```mermaid
xychart-beta
    title "enzoemir1/autoflow-n8n-workflows 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-11-25"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-23 10 → 2026-11-25 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 mid · 依据 README sha `2fd33a53359e` · [字段定义](../../DATASET.md)*
