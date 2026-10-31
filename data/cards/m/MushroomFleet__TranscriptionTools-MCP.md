# MushroomFleet/TranscriptionTools-MCP

⭐ 20 · TypeScript · MIT · 推送 2026-04-07 · [GitHub](https://github.com/MushroomFleet/TranscriptionTools-MCP) · 个人维护

**面向 MCP 客户端的转录文本处理服务器：格式化、修复与摘要**

一个 MCP 服务器，为 Claude Desktop 等 MCP 客户端提供四个转录文本处理工具：repair_text 基于语义上下文修复转录错误（90% 置信度阈值，无需原始音频）、format_transcript 将带时间戳的转录转为自然格式文本（按停顿时长分段）、summary_text 按 ACE 认知方法生成摘要（支持时长/字符数/词数约束）、get_repair_log 读取修复日志。基于 TypeScript/npm 构建，支持 Smithery 一键安装或源码克隆构建，配置通过修改源码中的参数完成。

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

- 语义上下文修复转录错误，90% 置信度阈值，无需原始音频
- 时间戳转录转自然格式文本，按停顿时长（4s/8s）分段
- 摘要支持时长、字符数、词数三种约束类型
- 四个 MCP 工具暴露给客户端调用

## 适用场景

- 为我的 Claude Desktop 添加转录文本格式化与修复能力
- 将带时间戳的口述转录整理为可读文本
- 对长转录生成指定长度的摘要并留存修复日志

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L5: An MCP server providing intelligent transcript processing capabilities, featuring natural formatting, contextual rep
> L13: This MCP server exposes four powerful tools for transcript processing:

## 星数曲线

```mermaid
xychart-beta
    title "MushroomFleet/TranscriptionTools-MCP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `6dbba4b7c051` · [字段定义](../../DATASET.md)*
