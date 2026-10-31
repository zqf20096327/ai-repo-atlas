# moatazhamada/ai-omni-skills

⭐ 14 · JavaScript · MIT · 推送 2026-09-07 · [GitHub](https://github.com/moatazhamada/ai-omni-skills) · 个人维护

**统一管理各 AI 编码工具技能的 CLI 与 MCP 服务器**

面向同时使用多个 AI 编码工具的开发者：将散落在 Claude Code、Codex、Gemini、Cursor、Kimi 等工具中的 SKILL.md 技能与指令文件聚合到单一规范仓库，通过符号链接、即时编译为目标工具格式及本地 MCP 服务器（list_skills/read_skill）同步到各工具。支持 20+ 工具的自动检测与一条命令接线，写入前自动备份，含孤儿技能检测、技能漏洞扫描（SkillSpector）、技能创建向导等管理子命令。以 npm、Homebrew 及原生二进制分发，不含技能本身，需用户自备私有技能仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单条命令将技能/指令/MCP 配置同步到 20+ AI 编码工具
- SKILL.md 即时编译为各目标工具的原生格式
- 本地 MCP 服务器暴露 list_skills / read_skill
- 写入前自动备份到时间戳目录，支持 dry-run 与会话级确认

## 适用场景

- 在多个 AI 编码工具间复用同一套技能和指令文件
- 检测并回收散落各处的孤儿技能与重复模板
- 把现有文档文件转换为标准 SKILL.md 技能
- 为接入的技能做漏洞扫描

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L14: A CLI + MCP server that takes the skills you've collected across all your AI
> L104: |Tool|Type|Config|Skills Dir|MCP|
> L106: |**Claude Code**|CLI|`~/.claude/CLAUDE.md`|✓|✓|

## 星数曲线

```mermaid
xychart-beta
    title "moatazhamada/ai-omni-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `fe8f16224225` · [字段定义](../../DATASET.md)*
