# proyecto26/notebooklm-ai-plugin

⭐ 65 · TypeScript · MIT · 推送 2026-08-28 · [GitHub](https://github.com/proyecto26/notebooklm-ai-plugin) · 个人维护

**让 Claude Code 等 AI agent 操作 NotebookLM 的技能插件**

遵循 Agent Plugins v1.0.0 与 Agent Skills 规范的 NotebookLM 技能插件，供 Claude Code、OpenClaw 等可执行 shell 命令的 AI agent 调用。功能包括：与笔记本 AI 对话（带引用）、生成 9 类产物（幻灯片、音频/视频概览、思维导图、闪卡、测验、信息图、报告、数据表）、管理来源（URL/YouTube/文件）、快慢两档网络研究与笔记管理。机制上用 Chrome DevTools Protocol 完成 Google 登录并缓存 Cookie，之后通过 Google 内部 batchexecute RPC 直接调用；无官方 API，RPC 方法 ID 可能随 Google 变更而失效，受 NotebookLM 免费版每日额度限制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 生成 9 类产物：幻灯片、音频/视频概览、思维导图、闪卡、测验、信息图、报告、数据表
- CDP 完成一次性 Google 登录后走 batchexecute RPC，产物生成无浏览器开销
- 来源管理支持 URL、YouTube、PDF/DOCX/EPUB 等文件与粘贴文本
- 同时提供根 plugin.json（可移植）与 .claude-plugin/ 清单（Claude Code 原生安装）

## 适用场景

- 在终端里通过对话让 Claude 操作我的 NotebookLM 笔记本
- 把研究论文上传为来源并自动生成学习指南或播客式音频
- 让 agent 跑深度网络研究并自动把来源导入笔记本

## 场景标签

`知识库管理` `科研工具` · 领域:知识与检索

## 证据(README 行号)

> L8: **Bring the full Google NotebookLM experience to Claude Code, OpenClaw and any other AI agents that execute shell co
> L16: This plugin follows the Agent Plugins v1.0.0 packaging standard
> L202: **Hybrid approach:** Chrome DevTools Protocol (CDP) handles Google authentication once, then all operations use di

## 星数曲线

```mermaid
xychart-beta
    title "proyecto26/notebooklm-ai-plugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 64 --> 66
    line [65, 65]
```

2026-10-18 65 → 2026-10-29 65（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `5da0fe273406` · [字段定义](../../DATASET.md)*
