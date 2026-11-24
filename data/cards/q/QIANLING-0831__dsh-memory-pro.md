# QIANLING-0831/dsh-memory-pro

⭐ 19 · JavaScript · MIT · 推送 2026-11-14 · [GitHub](https://github.com/QIANLING-0831/dsh-memory-pro) · [官网](https://github.com/QIANLING-0831/dsh-memory-plus) · 个人维护 · 中文 README

**DeepSeek Harness 的社区记忆插件集：跨会话找回旧讨论与中文检索**

面向 DeepSeek Harness（DSH）宿主的 8 包记忆插件集合：提供中文子串检索（FTS5 trigram 双表 + LIKE 回退）、同工作区跨会话搜索与按来源回读原文、跨会话持久事实注入、模型可写技能与后台反思蒸馏的自我进化。技能与记忆带来源 provenance，用户通过斜杠命令固定的内容模型改不动。通过 dsh plugin 命令安装 Release 包或源码脚本，需 Node.js 24、pnpm 与兼容版本 DSH（>=0.1.5-rc.3 <0.3.0）。不支持跨设备云同步与 Obsidian 导入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- FTS5 双 tokenizer 中文子串检索，支持中英混排与扩展汉字
- 跨会话搜索 + 原文回读，核对后续纠正后带来源继续
- 技能自我进化（skill_write + 后台反思蒸馏，请求路径零开销）
- 用户固定层 provenance 保护，模型工具一律拒绝改写并记审计日志

## 适用场景

- 新会话里找回上次讨论的方案和最终决定
- 解决中文历史会话难搜索、压缩后细节丢失的问题
- 跨会话记住项目偏好、约定与决策，无需每次重述

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L43: DSH Memory Pro 是 DeepSeek Harness 的社区记忆插件集：中文子串检索负责找内容，工作区跨会话搜索与原文回读负责找回讨论，长期事实和技能负责复用已经确认的经验。共 8 个包，可用一个独立 bundle 
> L74: |`dsh-session-query-sqlite-cjk`|中文可用的会话全文检索 provider：FTS5 双 tokenizer 双表（unicode61 + trigram），按查询是否含 CJK 自动路由|Phase
> L76: |`dsh-memory-index`|混合记忆检索服务 `ctx.memorySearch`：sqlite-vec 向量臂 + FTS5 词法臂 → RRF 融合；事件级增量嵌入；file 词条过滤|Phase 1|

## 星数曲线

```mermaid
xychart-beta
    title "QIANLING-0831/dsh-memory-pro 星数(近 2 点)"
    x-axis ["2026-11-14", "2026-11-24"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-11-14 19 → 2026-11-24 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 mid · 依据 README sha `7f4efd7b3d40` · [字段定义](../../DATASET.md)*
