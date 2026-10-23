# gmickel/memorybot

⭐ 123 · TypeScript · MIT · 推送 2026-02-15 · [GitHub](https://github.com/gmickel/memorybot) · 个人维护

**Node.js 终端 AI 聊天机器人，提供无限上下文与对话历史**

基于 Node.js 的命令行聊天机器人，接入 OpenAI API，通过 LangChain 实现：将文档（.txt/.md/.pdf/.docx/.epub/.csv 等）、网页、YouTube 字幕加入上下文向量库，可做文档问答与上下文感知内容生成；对话历史存入独立记忆向量库，按相关性检索以控制发送的上下文量。支持多项目上下文库切换、每日聊天日志、运行时命令调整检索数量。需要 OpenAI API key；README 顶部引导用户转向作者的另一项目 GNO。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文档/网页/YouTube 字幕加入上下文向量库做问答
- 对话历史持久化到独立记忆向量库，可配置检索条数
- 多上下文库管理，单命令切换项目上下文
- 支持 .txt/.md/.json/.pdf/.docx/.epub/.csv 文档类型

## 适用场景

- 基于自己的文档和资料做问答（如查财报数据）
- 带历史记忆的多轮对话内容生成
- 将网页和 YouTube 视频内容加入对话上下文

## 场景标签

`聊天机器人` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L5: Memory Bot is designed to support context-aware requests to the OpenAI API, providing unlimited context and chat his
> L7: Memory Bot can be used for a variety of purposes, including context-aware content generation, such as marketing mate

## 星数曲线

```mermaid
xychart-beta
    title "gmickel/memorybot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 122 --> 124
    line [123, 123]
```

2026-10-18 123 → 2026-10-23 123（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `3e40d895d723` · [字段定义](../../DATASET.md)*
