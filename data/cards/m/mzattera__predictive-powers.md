# mzattera/predictive-powers

⭐ 15 · Java · Apache-2.0 · 推送 2026-01-04 · [GitHub](https://github.com/mzattera/predictive-powers) · [官网](https://mzattera.github.io/predictive-powers/) · 个人维护

**Java 库：用生成式 AI 服务创建自主 agent**

面向 Java 开发者的库，封装多家 GenAI 服务接口以构建自主 agent：为不同提供商提供统一抽象层，自动处理上下文大小与聊天历史，以统一方式添加工具/函数调用（含模块化工具方案），支持多部分消息携带文件与图像、图像自动缩放缓存，另提供图像生成、STT、TTS、网页搜索等能力，以及内置的可序列化内存向量库与多种格式文档的读取/分块/嵌入。需 Java 11 以上，以 Maven 依赖引入。

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

- 多 GenAI 提供商的统一抽象层，可无缝切换接入
- 自动处理上下文大小与聊天历史，统一函数/工具调用接口
- 内置内存向量数据库与文档读取/分块/嵌入方法
- 除聊天补全外还提供图像生成、STT、TTS、网页搜索

## 适用场景

- 在 Java 项目中接入不同 GenAI 提供商构建自主 agent
- 为模型附加模块化工具实现函数调用
- 处理多格式文档并嵌入到内存向量库

## 场景标签

`Agent 框架` `图像生成` `语音合成` · 领域:Agent 开发

## 证据(README 行号)

> L3: **`predictive-powers` is a Java library to easily create autonomous agents using generative AI (GenAI) services.
> L10:  1. Adds an abstraction layer for GenAI capabilities, this allows to plug-in different providers seamlessly and red

## 星数曲线

```mermaid
xychart-beta
    title "mzattera/predictive-powers 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `611e81e82742` · [字段定义](../../DATASET.md)*
