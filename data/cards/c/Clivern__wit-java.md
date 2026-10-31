# Clivern/wit-java

⭐ 15 · Java · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/Clivern/wit-java) · [官网](https://wit.ai) · 个人维护

**Wit.ai NLP 平台的 Java 客户端 SDK**

面向 Java 开发者的 Wit.ai API 封装库，通过 Maven/Gradle/SBT 添加依赖，配置 wit_api_id 与 wit_access_token 后即可调用。覆盖 Wit.ai 的 App 管理（增删改查）、句子含义提取（Message 接口）、实体及其取值与表达式的增删改查等端点，并附 Spark Java 框架下的调用示例。2018 年发布 1.0.0 初始版本，作者个人维护，Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 封装 Wit.ai 的 App、Message、Entity 三类 API 端点
- 支持 Maven/Gradle/Scala SBT 三种依赖引入方式
- 提供 Spark Java 框架下的用法示例
- API ID 与访问令牌可按请求级别覆盖

## 适用场景

- 在 Java 应用中调用 Wit.ai 做自然语言理解
- 以编程方式管理 Wit.ai 的应用与实体数据
- 为聊天机器人的 Java 后端接入 Wit.ai

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: Wit-Java Is A Java Library For Wit.ai
> L137: To extract the meaning from a sentence, based on the app data:

## 星数曲线

```mermaid
xychart-beta
    title "Clivern/wit-java 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `d484c07fbbe0` · [字段定义](../../DATASET.md)*
