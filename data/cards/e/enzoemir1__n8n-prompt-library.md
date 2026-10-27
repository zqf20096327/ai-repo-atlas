# enzoemir1/n8n-prompt-library

⭐ 23 · MIT · 推送 2026-08-20 · [GitHub](https://github.com/enzoemir1/n8n-prompt-library) · 组织维护

**面向 n8n 工作流的 20 条生产级 AI 提示词库**

为 n8n AI 节点提供的系统提示词集合：20 条提示词按内容生成、数据处理、邮件、分类、客户支持、SEO 六类组织，每条 JSON 文件含系统提示词全文、推荐模型与温度设置、单次成本估算、带 {{placeholders}} 的用户提示词模板、示例输出与 n8n 集成提示。使用方式为复制粘贴到 n8n AI 节点的 System Message 字段，模型推荐以 gpt-4o-mini 为主，另列 Groq/Llama 3.1 与本地 Ollama/Mistral 方案。全部 20 条运行一次约 $0.05。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 20 条提示词覆盖 6 个类别（内容/数据/邮件/分类/支持/SEO）
- 每条含推荐模型、温度、单次成本估算与示例输出
- 用户提示词模板使用 {{placeholders}} 对接 n8n 表达式
- 提供按场景的成本估算表（日 50 次/月度成本）

## 适用场景

- 在 n8n 工作流中直接复用现成系统提示词搭建 AI 节点
- 搭建内容分发、邮件自动化或客服分流等工作流
- 评估不同工作流场景的模型调用成本

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L10:  20 production-ready AI prompts optimized for n8n workflows.
> L17: This library gives you **battle-tested system prompts** that you can drop directly into your n8n OpenAI / Anthropic

## 星数曲线

```mermaid
xychart-beta
    title "enzoemir1/n8n-prompt-library 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `d1f62f56afd9` · [字段定义](../../DATASET.md)*
