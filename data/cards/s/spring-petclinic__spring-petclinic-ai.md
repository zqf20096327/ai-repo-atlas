# spring-petclinic/spring-petclinic-ai

⭐ 39 · Java · Apache-2.0 · 推送 2026-09-13 · [GitHub](https://github.com/spring-petclinic/spring-petclinic-ai) · 组织维护

**Spring PetClinic 示例应用的 AI 聊天助手分支**

经典 Spring PetClinic 示例应用的分支，基于 Spring AI 项目加入聊天机器人，用户可用自然语言查询宠物诊所数据（列出主人、查询兽医、为主人添加宠物等）。支持 OpenAI（默认）、Azure OpenAI 和 Ollama（部分支持）三种 LLM 提供方，通过 Maven profile 或 Gradle 依赖切换。需 Java 17+ 从源码构建运行，默认使用内存 H2 数据库，可切换 MySQL/PostgreSQL，项目本身不含 Dockerfile。面向学习 Spring Boot 与 Spring AI 集成的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Spring AI 的自然语言聊天助手，可查询与修改诊所数据
- OpenAI / Azure OpenAI / Ollama 三种 LLM 提供方按 Maven profile 切换
- 默认 H2 内存数据库，支持 MySQL/PostgreSQL 持久化配置
- 提供 Maven 与 Gradle 两种构建方式

## 适用场景

- 学习 Spring AI 将 LLM 接入 Spring Boot 应用
- 参考自然语言查询业务数据的实现方式
- 对比不同 LLM 提供方（OpenAI/Azure/Ollama）的集成配置

## 场景标签

`聊天机器人` `教程课程` · 领域:对话与助手

## 证据(README 行号)

> L7: Thanks to the work of Oded Shopen, a chatbot using **Generative AI** has been added to the famous Spring Petclinic a
> L14: Spring Petclinic integrates a Chatbot that allows you to interact with the application in a natural language. Here 

## 星数曲线

```mermaid
xychart-beta
    title "spring-petclinic/spring-petclinic-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-25 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `6a0a5ad21197` · [字段定义](../../DATASET.md)*
