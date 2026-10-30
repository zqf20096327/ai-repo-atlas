# 403errors/repomind

⭐ 291 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/403errors/repomind) · [官网](https://repomind.in) · 组织维护

**用 Agentic CAG 与公开 GitHub 仓库/开发者对话的 AI 分析平台**

基于 Next.js 的浏览器端 AI 应用：输入公开仓库名或 GitHub 用户名后，可通过对话询问架构、实现与安全问题。核心机制为 Agentic CAG——按问题选取完整相关文件作为上下文而非向量分块，配合 SHA 键文件缓存与分层使用限额（匿名/登录）。生成架构图与流程图（Mermaid），内置接入 OSV.dev 的快速/深度安全扫描。文件选择与回答生成使用不同 Gemini 模型，可自托管（需 GitHub token 与 Gemini API key）或使用托管站 repomind.in。

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

- Agentic CAG：选取完整相关文件而非向量分块作为上下文
- 生成架构图与流程图（Mermaid）辅助理解仓库
- 快速/深度安全扫描，集成 OSV.dev CVE 数据
- 区分文件选择模型与回答生成模型，聊天流式展示处理阶段

## 适用场景

- 接手新仓库时通过对话快速理解架构与实现
- 对公开项目做安全扫描并获取可执行修复建议
- 分析某个 GitHub 开发者的活跃仓库与提交轨迹

## 场景标签

`RAG` `网络安全` `聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L18: RepoMind is an open-source, AI-powered platform for understanding public GitHub repositories and developer profiles
> L48: RepoMind uses **Agentic Context-Augmented Generation (CAG)**. Instead of relying only on embeddings, it prunes and 

## 星数曲线

```mermaid
xychart-beta
    title "403errors/repomind 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 290 --> 292
    line [291, 291]
```

2026-10-18 291 → 2026-10-30 291（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `81eec31c98f5` · [字段定义](../../DATASET.md)*
