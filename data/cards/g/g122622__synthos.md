# g122622/synthos

⭐ 43 · TypeScript · MIT · 推送 2026-08-31 · [GitHub](https://github.com/g122622/synthos) · 个人维护 · 中文 README

**QQ/微信聊天记录导入与 AI 摘要的自托管分析系统**

基于 Node.js/TypeScript 的 Monorepo 系统：通过旁路只读方式解密 QQ/微信本地消息数据库，经预处理（分组、上下文拼接、引用追踪）后由 LLM 生成话题摘要、兴趣度打分与每日日报，并用 Ollama + bge-m3 做向量嵌入与 RAG 问答，WebUI 提供可视化与 Agent 流式问答。面向个人用户回顾群聊与团队管理者洞察趋势。微信提取依赖私有 submodule，需申请权限；本地 LLM 路线建议内存 ≥16GB，Docker 部署标注为 WIP。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- QQ/微信本地数据库只读取取 + 全链路 Pipeline（预处理→摘要→嵌入→兴趣度打分）
- 基于 Ollama + bge-m3 的向量嵌入与 RAG 问答（Multi-Query、会话记忆）
- 兴趣度指数：按用户关键词偏好为话题打分排序，支持负向反馈
- WebUI Agent 流式问答（REST SSE）与每日日报自动生成

## 适用场景

- 回顾多个群聊的高价值讨论，代替手动阅读海量消息
- 按个人兴趣偏好筛选和排序群聊话题
- 对历史聊天记录做语义检索与问答，沉淀为个人知识库

## 场景标签

`RAG` `知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L7: Synthos 是一个基于 `Node.js` 和 `TypeScript` 构建的智能聊天记录分析系统，专注于 QQ / 微信等 IM 平台聊天记录的全链路数据处理与 AI 总结功能。项目采用现代化的 Monorepo 架构，融合
> L42: - **AI 摘要生成**：基于 云端/本地 模型生成高质量对话摘要
> L81: > - ✅ 已完成 向量嵌入与语义检索：基于 Ollama + bge-m3 生成话题向量嵌入，支持 RAG 语义搜索

## 星数曲线

```mermaid
xychart-beta
    title "g122622/synthos 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-27 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1cf3ebca7293` · [字段定义](../../DATASET.md)*
