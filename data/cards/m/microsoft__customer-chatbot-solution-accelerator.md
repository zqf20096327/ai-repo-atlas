# microsoft/customer-chatbot-solution-accelerator

⭐ 50 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/microsoft/customer-chatbot-solution-accelerator) · 组织维护

**面向企业的客户服务聊天机器人部署方案（Azure AI Foundry）**

微软维护的解决方案加速器：基于 Azure AI Foundry Agent Framework 构建智能客服聊天体验。包含行业场景宿主应用（电商/医疗/银行三选一部署）与可嵌入聊天组件（文本+语音），由编排 agent 将客户查询路由到目录查询与政策知识两个专用 agent，通过 Foundry IQ 混合检索保证回答有据可依。以 azd 命令部署到 Azure 订阅，依赖 Cosmos DB、App Service 等多项 Azure 服务，按用量计费；示例数据为合成数据，医疗与银行场景仅为演示。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 编排 agent 自动路由到目录/政策专用 agent
- 三行业场景包（电商/医疗/银行）按环境部署
- widget.js 可嵌入聊天组件，支持文本与语音（Voice Live）
- Foundry IQ 对目录与政策文档做语义+关键词混合检索

## 适用场景

- 快速部署行业客服聊天机器人到 Azure 订阅
- 在自有网站嵌入带目录与政策问答的聊天组件
- 作为多 agent 编排+RAG 客服架构的参考实现

## 场景标签

`聊天机器人` `多智能体` `RAG` · 领域:Agent 开发

## 证据(README 行号)

> L3: This solution accelerator empowers organizations to build intelligent, conversational customer service experiences b
> L9: Leverages Azure AI Foundry's Agent Framework, Foundry IQ, and Azure Cosmos DB to create an intelligent customer chat
> L39: - **Intelligent agent orchestration using Microsoft Agent Framework**

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/customer-chatbot-solution-accelerator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-28 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `7f23cb94e868` · [字段定义](../../DATASET.md)*
