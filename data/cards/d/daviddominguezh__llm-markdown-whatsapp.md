# daviddominguezh/llm-markdown-whatsapp

⭐ 17 · TypeScript · MIT · 推送 2026-02-13 · [GitHub](https://github.com/daviddominguezh/llm-markdown-whatsapp) · [官网](https://www.npmjs.com/package/@daviddh/llm-markdown-whatsapp) · 个人维护

**把 LLM 生成的 markdown 切分为 WhatsApp 友好消息分片的库**

TypeScript 工具库，面向构建 WhatsApp 对话机器人/聊天流程的开发者：接收 LLM 输出的 markdown 文本，返回适合逐条发送的消息分片数组。机制为优先级排序的处理器链：先按结构切分（列表、商品卡、markdown 章节），再回退到语义切分（问号、句号），并保护 URL、邮箱、格式化数字等不被切断；后处理合并过小分片、规范化西语标点大小写。单一函数 splitChatText，零配置。

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

- 优先级处理器链：结构切分优先，语义切分兜底
- 保护 URL、邮箱、域名、格式化数字、缩写等不被切断
- 列表/商品卡保持完整，markdown 表格转为等宽块或按行分片
- 单函数零配置，兼容 null/undefined 输入

## 适用场景

- 把 LLM 回复拆成多条可读的 WhatsApp 消息
- 电商客服机器人按商品卡逐条发送选项
- 避免在 URL、邮箱、数字中间截断消息

## 场景标签

 · 领域:LLM 应用/消息格式化

## 证据(README 行号)

> L3:  A TypeScript library that splits LLM-generated markdown into WhatsApp-friendly chat message chunks.
> L27: This library handles all of this. One function call, zero configuration. Pass in the LLM's markdown output, get bac
> L161: - **Output:** An array of strings, each suitable for sending as an individual WhatsApp message.

## 星数曲线

```mermaid
xychart-beta
    title "daviddominguezh/llm-markdown-whatsapp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `45ad3bfead48` · [字段定义](../../DATASET.md)*
