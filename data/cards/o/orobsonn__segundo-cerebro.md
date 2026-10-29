# orobsonn/segundo-cerebro

⭐ 24 · TypeScript · 推送 2026-04-21 · [GitHub](https://github.com/orobsonn/segundo-cerebro) · 个人维护 · 中文 README

**自托管个人知识图谱 MCP 服务器，供 Claude 捕获与关联概念**

单用户 self-hosted 的 MCP 服务器，运行在用户自己的 Cloudflare 账号（D1/Vectorize/Workers AI，免费额度可覆盖），接入 Claude Code/Desktop/Web。机制：Claude 将对话中的想法原子化为单概念笔记，用 bge-m3 embedding（100+ 语言）跨域检索类比，创建 9 种关系类型的边并要求不少于 20 字符的理由说明；支持 OAuth 2.1 动态客户端注册。限制：不适用于 Claude Free（约 2400 token/冷请求开销），不提供离线/本地存储，拒绝随手记录式内容。部署通过 git clone + npm install + IDE agent 按 CLAUDE.md runbook 完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 笔记原子化：一概念一笔记，tldr 单句摘要（费曼测试）
- 9 种关系类型，每条边要求 ≥20 字符的机制性理由
- 跨域均衡召回，bge-m3 embedding 支持 100+ 语言
- 全部运行在用户自己的 Cloudflare 免费额度内（D1 + Vectorize + Workers AI）

## 适用场景

- 在 Claude 对话中积累跨会话的知识笔记并发现跨领域类比
- 保存设计决策、研究结论等值得长期回溯的推理过程
- 按 Munger/Luhmann 式 latticework 方法组织个人知识

## 场景标签

`知识库管理` `知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L5: **A ferramenta de pensamento latticework pra quem conversa com o Claude.** Segundo Cérebro é um grafo de conheciment
> L145: O Claude chama `recall` pra varrer o vault atrás de analogias, aí oferece salvar a nota com `save_note`, atomizand

## 星数曲线

```mermaid
xychart-beta
    title "orobsonn/segundo-cerebro 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `0f7ff3defea3` · [字段定义](../../DATASET.md)*
