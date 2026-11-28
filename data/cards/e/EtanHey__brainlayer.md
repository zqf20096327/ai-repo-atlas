# EtanHey/brainlayer

⭐ 10 · Python · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/EtanHey/brainlayer) · [官网](https://brainlayer.etanheyman.com/) · 个人维护

**给 MCP 兼容 AI agent 提供跨会话持久记忆的本地服务器**

基于 SQLite 的 MCP 记忆服务器：单个 .db 文件本地存储，提供语义+FTS5 混合检索（RRF 融合）、知识图谱、实体与人物查询、会议记录摘要入库等 16 个工具，默认启动仅暴露 5 个核心工具以压缩载荷。写入有 STORED/DUPLICATE/MERGED/DEFERRED 等显式结果词，工具定义携带 ToolAnnotations。通过 pip 安装、macOS 另有可选 Swift BrainBar 伴生进程，无云端、无 Docker。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 16 个 MCP 工具，含语义+关键词混合检索与 MMR 去重
- 本地知识图谱：实体、关系、共现抽取与人物查询
- brain_store 返回显式结果词（STORED/DUPLICATE/MERGED/DEFERRED）
- 单 SQLite 文件本地运行，声明无云依赖

## 适用场景

- 让 Claude Code、Cursor、Zed 等 MCP 客户端跨会话记住决策与修复经验
- 多个 agent 共享同一份组织记忆，互相继承学到的结论
- 把会议记录、文档摘要入库后语义检索

## 场景标签

`Agent 记忆` `知识图谱` `语义搜索` · 领域:Agent 开发

## 证据(README 行号)

> L14: BrainLayer gives any MCP-compatible AI agent persistent memory across conversations — and gives a whole **fleet** o
> L78: The agent-facing MCP server is **BrainBar** on `/tmp/brainbar.sock`. It defines 16 tools, and


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `bb8264fd7000` · [字段定义](../../DATASET.md)*
