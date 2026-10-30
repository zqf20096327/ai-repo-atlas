# rh-java4ai-workshop/parasol-insurance

⭐ 20 · TypeScript · MIT · 推送 2025-11-20 · [GitHub](https://github.com/rh-java4ai-workshop/parasol-insurance) · 组织维护

**虚构保险理赔的 AI 聊天演示应用（Quarkus+React）**

基于 Quarkus 与 React 的演示应用，用于管理虚构的保险理赔：用户点击某个理赔后在聊天界面提问，应用将理赔上下文与用户问题一并发送给 LLM，回答展示在聊天中。需连接 OpenAI 兼容的推理服务器（如 InstructLab，默认 localhost:8000），LLM 坐标可在 application.properties 中配置。运行需 Java 21+ 与 Maven 3.9.6+（或内嵌 Maven Wrapper），通过 ./mvnw quarkus:dev 启动，应用监听 8005 端口。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将理赔上下文与用户查询一并送入 LLM 生成聊天回答
- 支持 OpenAI 兼容推理服务器（InstructLab 示例）
- LLM 主机/端口等可在 application.properties 配置
- 提供 Maven Wrapper，可免装 Maven 运行

## 适用场景

- 演示 Quarkus + React 构建的 AI 聊天应用
- 在虚构保险理赔场景中体验 LLM 问答
- 作为 Quarkus Quinoa 集成前后端的示例工程

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: A Quarkus + React AI app for managing fictitious insurance claims. Uses Quarkus Quinoa under the covers.
> L34: Open the app, click on a claim, click on the chat app, and start asking questions. The context of the claim is sent

## 星数曲线

```mermaid
xychart-beta
    title "rh-java4ai-workshop/parasol-insurance 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `1852446602bc` · [字段定义](../../DATASET.md)*
