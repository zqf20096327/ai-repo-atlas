# 4pixeltechBR/Token-Saver

⭐ 16 · Go · MIT · 推送 2026-09-21 · [GitHub](https://github.com/4pixeltechBR/Token-Saver) · [官网](https://github.com/4pixeltechBR/Token-Saver) · 组织维护

**多 AI 编码助手的上下文审计与 token 优化技能，支持回滚**

以 Go 编写的可移植 skill 与 CLI 二进制：检测所在环境（Claude Code、Codex、Cursor 等 9 种 harness），审计项目指令文件的长度与重复、检测技术栈与已安装 skills，输出 JSON 供自动化。仅对 Claude Code 可应用配置变更（重开 Tool Search、添加 Modo Direto 规则），带原子写入、备份与回滚；其他 harness 仅只读审计。明确声明不测量实际 token 消耗与节省，不自动压缩会话、不改 CLAUDE.md。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 种 harness 环境检测与只读审计（指令文件、stack、skills）
- 仅 Claude Code 支持配置应用，含原子写入、备份与 rollback
- 无遥测；明确声明不测量真实 token 消耗与节省
- 预装二进制发布，无需 Python/Node，附带 CLI 与 JSON 输出

## 适用场景

- 审计 Claude Code 等编码助手项目中的长指令文件与重复内容
- 在应用优化前先生成带标识的预览并可回滚
- 以 JSON 输出集成到自动化流程做上下文体检

## 场景标签

 · 领域:开发者工具/AI 编码助手

## 证据(README 行号)

> L3: Auditoria segura de contexto para Claude Code, Codex, Antigravity, OpenCode,
> L20: |Função|Claude Code|Outros harnesses|
> L55: Baixe o ZIP da release mais recente

## 星数曲线

```mermaid
xychart-beta
    title "4pixeltechBR/Token-Saver 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-30 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `cf192ca7e9cd` · [字段定义](../../DATASET.md)*
