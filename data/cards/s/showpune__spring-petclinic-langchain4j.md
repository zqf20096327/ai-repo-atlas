# showpune/spring-petclinic-langchain4j

⭐ 15 · CSS · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/showpune/spring-petclinic-langchain4j) · 个人维护

**Langchain4j 集成示例：宠物诊所应用带 AI 聊天助手**

Spring PetClinic 示例应用的 Langchain4j 版本，展示在 Spring Boot 中接入 LLM 的典型五要素：Prompt、Model、Memory、本地工具（Tools）与 RAG 内容检索器。内置聊天 agent，可按宠物症状推荐兽医、协助预约并注册宠物主人；记忆使用本地存储（实例间不共享），检索器使用本地文件，初始化时导入。模型通过 Azure OpenAI 配置接入。运行需先配置 application.properties，用 Maven 打包并以 java -jar 启动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 聊天 agent 可推荐兽医、预约并注册 owner/pets
- 演示 LLM 应用五要素：Prompt/Model/Memory/Tools/RAG
- 两个本地工具函数（Vets 列表、Owner/Pets 注册）
- 多语言提问时先翻译为英文再检索内容

## 适用场景

- 学习 Langchain4j 在 Spring Boot 中的集成方式
- 参考工具调用与 RAG 的示例实现
- 在本地体验带 AI 助手的 PetClinic 演示应用

## 场景标签

`AI 助手` `RAG` · 领域:对话与助手

## 证据(README 行号)

> L1: # Spring PetClinic Sample Application With OpenAI and Langchain4j
> L46: Normally a LLM application contains 5 parts: Prompt, Model, Memory, Native Functions( tools ）and RAG (content retri

## 星数曲线

```mermaid
xychart-beta
    title "showpune/spring-petclinic-langchain4j 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `5c8446d5f679` · [字段定义](../../DATASET.md)*
